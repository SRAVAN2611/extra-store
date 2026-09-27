import ollama

print("🚀 Qwen AI Test Started...\n")

while True:
    try:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("👋 Exiting...")
            break

        print("\n⏳ Thinking...\n")

        response = ollama.chat(
            model="qwen:1.8b",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        print("AI:", response['message']['content'], "\n")

    except Exception as e:
        print("❌ Error:", e)