import ollama

def ask_ai(question):
    response = ollama.chat(
        model="gemma3:4b",
        messages=[{"role": "user", "content": question}]
    )
    return response["message"]["content"]
