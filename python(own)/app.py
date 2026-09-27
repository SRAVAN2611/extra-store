# sentineltwin.py
# SentinelTwin: AI-Driven Cybersecurity Digital Twin Platform
#
# NOTE:
# - Run with: streamlit run sentineltwin.py
# - This is a single-file, educational "lab-style" implementation.
# - It simulates data and behavior so you can demonstrate all concepts
#   without needing a real enterprise environment.

import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    f1_score
)

# -------------------------------------------------------------------
# 1. GLOBAL SETTINGS & UTILS
# -------------------------------------------------------------------

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)


# Simple utility to generate timestamps
def random_timestamp(start_date, end_date):
    """
    Generate a random timestamp between start_date and end_date.
    """
    delta = end_date - start_date
    total_seconds = int(delta.total_seconds())
    if total_seconds <= 0:
        return start_date  # fallback if no range
    random_second = random.randrange(total_seconds)
    return start_date + datetime.timedelta(seconds=random_second)




# -------------------------------------------------------------------
# 2. SIMULATED LOG GENERATOR (USER / SYSTEM BEHAVIOR)
# -------------------------------------------------------------------

def generate_simulated_logs(num_days=30, base_date=None):
    """
    Generate synthetic logs for a single workstation/user over 'num_days'.

    Events simulated:
    - login (success/failure)
    - file_access (read/write/delete)
    - app_usage (open, duration)
    - network_access (domain, bytes)

    Some days will be marked "abnormal" with heavier malicious-looking behavior.
    """
    if base_date is None:
        base_date = datetime.date.today() - datetime.timedelta(days=num_days)

    rows = []
    abnormal_days = set(random.sample(range(num_days), k=max(1, num_days // 5)))  # ~20% abnormal days

    for d in range(num_days):
        day_date = base_date + datetime.timedelta(days=d)
        day_is_abnormal = d in abnormal_days

        # Number of each type of event can vary
        num_logins = random.randint(2, 5)
        if day_is_abnormal:
            num_logins += random.randint(3, 10)

        num_file_ops = random.randint(10, 40)
        if day_is_abnormal:
            num_file_ops += random.randint(30, 100)

        num_apps = random.randint(3, 10)
        if day_is_abnormal:
            num_apps += random.randint(5, 15)

        num_net = random.randint(5, 20)
        if day_is_abnormal:
            num_net += random.randint(20, 50)

        start_dt = datetime.datetime.combine(day_date, datetime.time(8, 0))
        end_dt = datetime.datetime.combine(day_date, datetime.time(23, 0))

        # Login events
        for i in range(num_logins):
            ts = random_timestamp(start_dt, end_dt)
            success = 1
            if day_is_abnormal and random.random() < 0.4:
                success = 0
            rows.append({
                "timestamp": ts,
                "event_type": "login",
                "success": success,
                "file_path": "",
                "operation": "",
                "app_name": "",
                "duration": 0,
                "domain": "",
                "bytes": 0,
                "is_honeypot": 0,
                "day_abnormal_label": int(day_is_abnormal)
            })

        # File events (including honeypot files)
        for i in range(num_file_ops):
            ts = random_timestamp(start_dt, end_dt)
            ops = ["read", "write", "delete"]
            op = random.choice(ops)
            # Normal files
            base_files = [
                "/docs/report.docx",
                "/docs/notes.txt",
                "/pics/image.png",
                "/work/code.py",
                "/work/design.pdf"
            ]
            # Honeypot files
            honeypot_files = [
                "/secret/salary_2025.xlsx",
                "/keys/prod.key",
                "/leaks/client_data.csv"
            ]
            if day_is_abnormal and random.random() < 0.3:
                fp = random.choice(honeypot_files)
                is_hp = 1
            else:
                fp = random.choice(base_files)
                is_hp = 0

            rows.append({
                "timestamp": ts,
                "event_type": "file_access",
                "success": 1,
                "file_path": fp,
                "operation": op,
                "app_name": "",
                "duration": 0,
                "domain": "",
                "bytes": 0,
                "is_honeypot": is_hp,
                "day_abnormal_label": int(day_is_abnormal)
            })

        # App usage
        for i in range(num_apps):
            ts = random_timestamp(start_dt, end_dt)
            apps = ["chrome", "vscode", "word", "excel", "spotify", "terminal", "mail"]
            app = random.choice(apps)
            duration = random.randint(5, 120)  # minutes
            rows.append({
                "timestamp": ts,
                "event_type": "app_usage",
                "success": 1,
                "file_path": "",
                "operation": "",
                "app_name": app,
                "duration": duration,
                "domain": "",
                "bytes": 0,
                "is_honeypot": 0,
                "day_abnormal_label": int(day_is_abnormal)
            })

        # Network access
        for i in range(num_net):
            ts = random_timestamp(start_dt, end_dt)
            domains = [
                "google.com", "youtube.com", "github.com", "mail.com",
                "bank.com", "corp.internal", "updates.os.com"
            ]
            malicious_domains = ["malicious.cn", "phish.xyz", "ransom.io"]
            if day_is_abnormal and random.random() < 0.25:
                dom = random.choice(malicious_domains)
                b = random.randint(10000, 1000000)
            else:
                dom = random.choice(domains)
                b = random.randint(1000, 200000)

            rows.append({
                "timestamp": ts,
                "event_type": "network_access",
                "success": 1,
                "file_path": "",
                "operation": "",
                "app_name": "",
                "duration": 0,
                "domain": dom,
                "bytes": b,
                "is_honeypot": 0,
                "day_abnormal_label": int(day_is_abnormal)
            })

    df = pd.DataFrame(rows)
    df.sort_values("timestamp", inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


# -------------------------------------------------------------------
# 3. FEATURE ENGINEERING (DIGITAL TWIN INPUT)
# -------------------------------------------------------------------

def build_daily_features(logs: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate raw logs into per-day features used by the digital twin model.
    """
    df = logs.copy()
    df["date"] = df["timestamp"].dt.date

    # Initialize per-day stats
    groups = df.groupby("date")

    feature_rows = []
    for date, g in groups:
        # Basic counts
        num_logins = (g["event_type"] == "login").sum()
        num_failed_logins = ((g["event_type"] == "login") & (g["success"] == 0)).sum()
        num_file_reads = ((g["event_type"] == "file_access") & (g["operation"] == "read")).sum()
        num_file_writes = ((g["event_type"] == "file_access") & (g["operation"] == "write")).sum()
        num_file_deletes = ((g["event_type"] == "file_access") & (g["operation"] == "delete")).sum()
        num_honeypot_access = ((g["event_type"] == "file_access") & (g["is_honeypot"] == 1)).sum()
        num_apps_used = g.loc[g["event_type"] == "app_usage", "app_name"].nunique()
        total_app_duration = g.loc[g["event_type"] == "app_usage", "duration"].sum()
        num_network_events = (g["event_type"] == "network_access").sum()
        total_bytes = g.loc[g["event_type"] == "network_access", "bytes"].sum()
        num_malicious_domains = g.loc[
            (g["event_type"] == "network_access") &
            (g["domain"].isin(["malicious.cn", "phish.xyz", "ransom.io"]))
        ].shape[0]

        # Time-based features: how many events at "odd hours" (e.g., 00:00–05:00)
        g["hour"] = g["timestamp"].dt.hour
        odd_hour_events = g[(g["hour"] < 6)].shape[0]

        # Label for supervised models
        # If ANY event in that day has day_abnormal_label = 1, treat day as abnormal
        day_label = int(g["day_abnormal_label"].max())

        feature_rows.append({
            "date": date,
            "num_logins": num_logins,
            "num_failed_logins": num_failed_logins,
            "num_file_reads": num_file_reads,
            "num_file_writes": num_file_writes,
            "num_file_deletes": num_file_deletes,
            "num_honeypot_access": num_honeypot_access,
            "num_apps_used": num_apps_used,
            "total_app_duration": total_app_duration,
            "num_network_events": num_network_events,
            "total_bytes": total_bytes,
            "num_malicious_domains": num_malicious_domains,
            "odd_hour_events": odd_hour_events,
            "label_abnormal": day_label
        })

    feat_df = pd.DataFrame(feature_rows)
    return feat_df


# -------------------------------------------------------------------
# 4. DIGITAL TWIN MODEL (ANOMALY + CLASSIFICATION)
# -------------------------------------------------------------------

def train_digital_twin_models(feat_df: pd.DataFrame):
    """
    Train:
    - Anomaly detection model (IsolationForest)
    - Supervised classifier (RandomForest) using the abnormal label

    Returns models and scaler.
    """
    feature_cols = [
        "num_logins",
        "num_failed_logins",
        "num_file_reads",
        "num_file_writes",
        "num_file_deletes",
        "num_honeypot_access",
        "num_apps_used",
        "total_app_duration",
        "num_network_events",
        "total_bytes",
        "num_malicious_domains",
        "odd_hour_events"
    ]
    X = feat_df[feature_cols].values
    y = feat_df["label_abnormal"].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # IsolationForest for anomaly detection
    iso = IsolationForest(
        n_estimators=200,
        contamination=0.2,
        random_state=RANDOM_SEED
    )
    iso.fit(X_scaled)

    # RandomForest for classification
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=RANDOM_SEED, stratify=y
    )
    clf = RandomForestClassifier(
        n_estimators=200,
        random_state=RANDOM_SEED
    )
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    report_str = classification_report(y_test, y_pred, output_dict=False)
    cm = confusion_matrix(y_test, y_pred)

    return {
        "feature_cols": feature_cols,
        "scaler": scaler,
        "iso_model": iso,
        "clf_model": clf,
        "clf_acc": acc,
        "clf_f1": f1,
        "clf_report": report_str,
        "clf_cm": cm
    }


def compute_risk_scores(models, feat_df: pd.DataFrame):
    """
    Use the digital twin models to compute:
    - anomaly_score (from IsolationForest)
    - clf_prob (from RandomForest)
    - combined risk score
    """
    feature_cols = models["feature_cols"]
    X = feat_df[feature_cols].values
    X_scaled = models["scaler"].transform(X)

    # IsolationForest anomaly score: lower means more anomalous.
    anomaly_scores = models["iso_model"].decision_function(X_scaled)
    # Convert to [0, 1] (approx) risk style: higher -> riskier
    # Do a simple min-max normalization
    a_min, a_max = anomaly_scores.min(), anomaly_scores.max()
    # invert sign so that originally low (anomalous) becomes high risk
    anomaly_risk = -anomaly_scores
    ar_min, ar_max = anomaly_risk.min(), anomaly_risk.max()
    if ar_max - ar_min == 0:
        anomaly_risk_norm = np.zeros_like(anomaly_risk)
    else:
        anomaly_risk_norm = (anomaly_risk - ar_min) / (ar_max - ar_min)

    # Classification probability of abnormal (class=1)
    clf_proba = models["clf_model"].predict_proba(X_scaled)[:, 1]

    # Combined risk (simple average)
    combined_risk = (anomaly_risk_norm + clf_proba) / 2.0

    feat_df = feat_df.copy()
    feat_df["anomaly_risk"] = anomaly_risk_norm
    feat_df["clf_prob_abnormal"] = clf_proba
    feat_df["combined_risk"] = combined_risk

    return feat_df


# -------------------------------------------------------------------
# 5. RANSOMWARE SPREAD SIMULATION (GRAPH)
# -------------------------------------------------------------------

def build_network_graph():
    """
    Build a simple demo network using networkx.
    Nodes represent hosts/assets.
    """
    G = nx.Graph()
    nodes = [
        "UserPC",
        "FileServer",
        "DBServer",
        "BackupServer",
        "DevMachine",
        "HRMachine",
        "FinanceMachine"
    ]
    G.add_nodes_from(nodes)

    edges = [
        ("UserPC", "FileServer"),
        ("UserPC", "DBServer"),
        ("UserPC", "DevMachine"),
        ("DevMachine", "DBServer"),
        ("DBServer", "BackupServer"),
        ("FileServer", "BackupServer"),
        ("HRMachine", "FileServer"),
        ("FinanceMachine", "DBServer"),
    ]
    G.add_edges_from(edges)

    # Assign some "security levels" (0 to 1, 1=more secure)
    security_levels = {
        "UserPC": 0.4,
        "FileServer": 0.6,
        "DBServer": 0.7,
        "BackupServer": 0.9,
        "DevMachine": 0.5,
        "HRMachine": 0.6,
        "FinanceMachine": 0.7
    }
    nx.set_node_attributes(G, security_levels, "security")

    return G


def infection_probability(G, src, dst, global_risk_factor=0.5):
    """
    Compute probability of infecting dst from src.
    global_risk_factor can be derived from digital twin risk if desired.
    """
    # Lower security -> higher infection probability
    sec_dst = G.nodes[dst].get("security", 0.5)
    base_p = 0.6 * (1 - sec_dst)  # 1 - security
    # Blend with global risk factor
    p = base_p * (0.5 + global_risk_factor / 2)
    # clamp
    p = max(0.0, min(1.0, p))
    return p


def simulate_ransomware_spread(G, initial_infected, steps=5, global_risk_factor=0.5):
    """
    Simple simulation: at each step, each infected node may infect neighbors
    with infection_probability.
    """
    infected = set(initial_infected)
    history = [set(infected)]

    for t in range(steps):
        newly_infected = set()
        for node in infected:
            for neigh in G.neighbors(node):
                if neigh not in infected:
                    p = infection_probability(G, node, neigh, global_risk_factor)
                    if random.random() < p:
                        newly_infected.add(neigh)
        infected |= newly_infected
        history.append(set(infected))

    return history


def draw_infection_step(G, infected_nodes, ax=None):
    """
    Draw the network highlighting infected nodes.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(4, 4))
    pos = nx.spring_layout(G, seed=RANDOM_SEED)

    node_colors = []
    for node in G.nodes():
        if node in infected_nodes:
            node_colors.append("red")
        else:
            node_colors.append("green")

    nx.draw(G, pos, with_labels=True, node_color=node_colors, ax=ax)
    return ax


# -------------------------------------------------------------------
# 6. AUTONOMOUS ATTACK AGENT (SIMPLE RULE-BASED)
# -------------------------------------------------------------------

def autonomous_attack_plan(feat_df: pd.DataFrame):
    """
    Very simple rule-based "attack agent" that decides which attack type
    would be worth simulating based on current features.

    This is not real hacking; it's simulation logic.
    """
    latest_day = feat_df.iloc[-1]

    actions = []

    # If failed logins are low but total logins and risk are high -> brute force attempt
    if latest_day["num_failed_logins"] < 3 and latest_day["num_logins"] > 5:
        actions.append("Simulated brute-force login attack")

    # If many file operations, simulate ransomware-like encryption
    if latest_day["num_file_writes"] + latest_day["num_file_deletes"] > 50:
        actions.append("Simulated mass file encryption attempt (ransomware)")

    # If many malicious domains, simulate C2 communication
    if latest_day["num_malicious_domains"] > 2:
        actions.append("Simulated C2 communication and data exfiltration")

    # If honeypot access happened, mark it as high-severity incident
    if latest_day["num_honeypot_access"] > 0:
        actions.append("High severity alert: Honeypot access detected")

    if not actions:
        actions.append("No critical attacks simulated (low-risk behavior)")

    return actions


# -------------------------------------------------------------------
# 7. ADVERSARIAL ML: SIMPLE PERTURBATION ATTACK + DEFENSE
# -------------------------------------------------------------------

def generate_adversarial_samples(feat_df: pd.DataFrame, models):
    """
    Create synthetic adversarial samples for days labeled abnormal.
    Approach:
    - Slightly modify features to mimic more 'normal'-like behavior
    - See if classifier is fooled into predicting normal (0).

    NOTE: This is a simple heuristic, not full FGSM.
    """
    feature_cols = models["feature_cols"]
    clf = models["clf_model"]
    scaler = models["scaler"]

    X = feat_df[feature_cols].values
    y = feat_df["label_abnormal"].values
    X_scaled = scaler.transform(X)

    # Choose abnormal samples
    abnormal_idx = np.where(y == 1)[0]
    if len(abnormal_idx) == 0:
        return None

    chosen_idx = np.random.choice(abnormal_idx, size=min(5, len(abnormal_idx)), replace=False)
    X_abnormal = X_scaled[chosen_idx]

    # We'll craft adversarial examples by nudging features
    # towards the mean of normal samples
    normal_idx = np.where(y == 0)[0]
    if len(normal_idx) == 0:
        return None
    X_normal = X_scaled[normal_idx]
    normal_mean = X_normal.mean(axis=0)

    eps = 0.2  # small step
    X_adv_scaled = X_abnormal + eps * (normal_mean - X_abnormal)
    # Predictions before and after
    y_pred_before = clf.predict(X_abnormal)
    y_pred_after = clf.predict(X_adv_scaled)

    # Map back to original feature space just for reference (approx)
    X_adv = scaler.inverse_transform(X_adv_scaled)

    adv_data = {
        "original_idx": chosen_idx,
        "X_original_scaled": X_abnormal,
        "X_adv_scaled": X_adv_scaled,
        "X_adv": X_adv,
        "y_true": y[chosen_idx],
        "y_pred_before": y_pred_before,
        "y_pred_after": y_pred_after
    }
    return adv_data


def adversarial_training(feat_df: pd.DataFrame, models, adv_data):
    """
    Very simple adversarial training:
    - Add adversarial samples labeled as abnormal (their true label)
    - Retrain classifier
    """
    feature_cols = models["feature_cols"]
    scaler = models["scaler"]
    base_clf = models["clf_model"]

    X = feat_df[feature_cols].values
    y = feat_df["label_abnormal"].values
    X_scaled = scaler.transform(X)

    if adv_data is None:
        return {
            "clf_model_adv": base_clf,
            "clf_acc_adv": models["clf_acc"],
            "clf_f1_adv": models["clf_f1"],
            "clf_report_adv": models["clf_report"],
        }

    X_adv_scaled = adv_data["X_adv_scaled"]
    y_adv = adv_data["y_true"]

    X_aug = np.vstack([X_scaled, X_adv_scaled])
    y_aug = np.concatenate([y, y_adv])

    X_train, X_test, y_train, y_test = train_test_split(
        X_aug, y_aug, test_size=0.3, random_state=RANDOM_SEED, stratify=y_aug
    )

    clf_adv = RandomForestClassifier(
        n_estimators=200,
        random_state=RANDOM_SEED
    )
    clf_adv.fit(X_train, y_train)

    y_pred = clf_adv.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    report_str = classification_report(y_test, y_pred, output_dict=False)

    return {
        "clf_model_adv": clf_adv,
        "clf_acc_adv": acc,
        "clf_f1_adv": f1,
        "clf_report_adv": report_str
    }


# -------------------------------------------------------------------
# 8. STREAMLIT DASHBOARD
# -------------------------------------------------------------------

def main():
    st.set_page_config(page_title="SentinelTwin", layout="wide")
    st.title("SentinelTwin: AI-Driven Cybersecurity Digital Twin Platform")

    st.markdown("""
    **SentinelTwin** is a prototype cyber-defense lab that demonstrates:
    - Digital twin of user/system behavior using ML
    - Anomaly and risk scoring
    - Autonomous attack simulation
    - Ransomware spread on a network graph
    - Honeypot personas (fake assets)
    - Simple adversarial ML attacks & defense
    """)

    # Sidebar
    st.sidebar.header("Controls")
    num_days = st.sidebar.slider("Number of simulated days", min_value=10, max_value=60, value=30, step=5)

    # Generate logs
    st.header("1. Simulated Logs")
    logs = generate_simulated_logs(num_days=num_days)
    st.write("Sample of raw logs:")
    st.dataframe(logs.head(20))

    # Feature engineering
    st.header("2. Digital Twin Features")
    feat_df = build_daily_features(logs)
    st.write("Per-day aggregated features:")
    st.dataframe(feat_df)

    # Train models
    st.header("3. Digital Twin Models")
    models = train_digital_twin_models(feat_df)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Classification Performance (Abnormal vs Normal)")
        st.text(f"Accuracy: {models['clf_acc']:.3f}")
        st.text(f"F1-score: {models['clf_f1']:.3f}")
        st.text("Detailed report:")
        st.text(models["clf_report"])

    with col2:
        st.subheader("Confusion Matrix")
        fig_cm, ax_cm = plt.subplots()
        sns.heatmap(models["clf_cm"], annot=True, fmt="d", cmap="Blues", ax=ax_cm)
        ax_cm.set_xlabel("Predicted")
        ax_cm.set_ylabel("True")
        st.pyplot(fig_cm)

    # Risk scores
    st.header("4. Risk Scoring (Digital Twin Output)")
    feat_with_risk = compute_risk_scores(models, feat_df)
    st.write("Features with risk scores:")
    st.dataframe(feat_with_risk)

    fig_risk, ax_risk = plt.subplots(figsize=(8, 4))
    ax_risk.plot(feat_with_risk["date"], feat_with_risk["combined_risk"], marker='o')
    ax_risk.set_title("Combined Risk Score Over Time")
    ax_risk.set_xlabel("Date")
    ax_risk.set_ylabel("Risk (0-1)")
    plt.xticks(rotation=45)
    st.pyplot(fig_risk)

    # Attack agent
    st.header("5. Autonomous Attack Agent (Simulation)")
    actions = autonomous_attack_plan(feat_with_risk)
    st.write("For the latest day, the agent proposes the following simulated actions:")
    for a in actions:
        st.markdown(f"- {a}")

    # Ransomware simulation
    st.header("6. Ransomware Spread Simulation (Network Graph)")
    G = build_network_graph()
    # Global risk factor: average risk from digital twin
    global_risk_factor = float(feat_with_risk["combined_risk"].mean())
    init_infected = ["UserPC"]

    steps = st.slider("Ransomware simulation steps", min_value=1, max_value=10, value=5)
    history = simulate_ransomware_spread(G, initial_infected=init_infected,
                                         steps=steps, global_risk_factor=global_risk_factor)

    st.write(f"Global risk factor (from digital twin): **{global_risk_factor:.3f}**")
    st.write("Ransomware spread over time:")

    # Show each step
    for t, infected_nodes in enumerate(history):
        st.markdown(f"**Step {t}: Infected nodes: {', '.join(sorted(infected_nodes))}**")
        fig_g, ax_g = plt.subplots(figsize=(4, 4))
        draw_infection_step(G, infected_nodes, ax=ax_g)
        st.pyplot(fig_g)

    # Honeypot alerts
    st.header("7. Honeypot Persona / Fake Assets Alerts")
    hp_access_days = feat_with_risk[feat_with_risk["num_honeypot_access"] > 0]
    if hp_access_days.empty:
        st.write("No honeypot file access detected in this simulation.")
    else:
        st.write("Days with honeypot access (high severity incidents):")
        st.dataframe(hp_access_days[["date", "num_honeypot_access", "combined_risk"]])

    # Adversarial ML
    st.header("8. Adversarial ML – Attacking and Hardening the Model")

    adv_data = generate_adversarial_samples(feat_with_risk, models)
    if adv_data is None:
        st.write("Not enough abnormal samples to generate adversarial examples.")
    else:
        y_true = adv_data["y_true"]
        y_before = adv_data["y_pred_before"]
        y_after = adv_data["y_pred_after"]

        st.subheader("8.1. Simple Adversarial Attack")
        st.write("True labels vs predictions before and after adversarial perturbation:")
        table_rows = []
        for i in range(len(y_true)):
            table_rows.append({
                "Sample_Index": int(adv_data["original_idx"][i]),
                "True_Label": int(y_true[i]),
                "Pred_Before": int(y_before[i]),
                "Pred_After": int(y_after[i])
            })
        st.dataframe(pd.DataFrame(table_rows))

        fooled = sum((y_true == 1) & (y_before == 1) & (y_after == 0))
        st.write(f"Number of abnormal samples originally detected as abnormal but misclassified after attack: **{fooled}**")

        st.subheader("8.2. Adversarial Training (Defense)")
        adv_def_results = adversarial_training(feat_with_risk, models, adv_data)
        st.text(f"Original Accuracy: {models['clf_acc']:.3f}, After Adversarial Training: {adv_def_results['clf_acc_adv']:.3f}")
        st.text(f"Original F1-score: {models['clf_f1']:.3f}, After Adversarial Training: {adv_def_results['clf_f1_adv']:.3f}")

        st.write("Classification report after adversarial training:")
        st.text(adv_def_results["clf_report_adv"])

    st.markdown("---")
    st.markdown("© SentinelTwin – Academic Prototype for Cybersecurity + AI + Digital Twin Research")


if __name__ == "__main__":
    main()
