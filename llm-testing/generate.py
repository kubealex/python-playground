import ollama

response = ollama.generate(model="llama2", prompt="What is an LLM?", stream=False)
print(response["response"])
