from langchain_ollama import ChatOllama

model = ChatOllama(model="qwen3:8b", base_url="http://127.0.0.1:11434", temperature=0.7)

response = model.invoke("Write a short haiku about AI.")
print(response)
