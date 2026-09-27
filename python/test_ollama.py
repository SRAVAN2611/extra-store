import ollama

def ask_model(model_name, prompt):
    try:
        print(f"\n👉 Sending request to {model_name}...\n")

        response = ollama.chat(
            model=model_name,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        print("✅ Response received!\n")

        return response['message']['content']

    except Exception as e:
        print("❌ Error:", e)
        return None


if __name__ == "__main__":
    print("🚀 Starting test...\n")

    # Test CodeLlama
    code_output = ask_model("codellama:7b", "Write a Python function to check prime number")

    if code_output:
        print("💻 CodeLlama Output:\n")
        print(code_output)

    print("\n" + "="*50 + "\n")

    # Test Llama3
    general_output = ask_model("llama3:8b", "Explain REST API simply")

    if general_output:
        print("🧠 Llama3 Output:\n")
        print(general_output)