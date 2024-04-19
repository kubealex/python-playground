from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain.prompts.chat import ChatPromptTemplate

llm = Ollama(model="llama3")
chat_model = ChatOllama()

template = (
    "You are a great assistant that translates {input_language} to {output_language}."
)
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        ("human", human_template),
    ]
)

messages = chat_prompt.format_messages(
    input_language="English", output_language="Italian", text="I love programming."
)

response = chat_model.invoke(messages)
print(response)
