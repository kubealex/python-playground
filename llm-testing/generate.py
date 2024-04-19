import ollama

response = ollama.generate(model="llama3", prompt="What is an LLM?", stream=False)
print(response["response"])
