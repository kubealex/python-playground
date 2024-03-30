import ollama

response = ollama.chat(
    model="llama2",
    messages=[
        {
            "role": "user",
            "content": "Why is the sky blue?",
        },
    ],
)
print(response["message"]["content"])

print(ollama.generate(model="llama2", prompt="What is an LLM?"))
