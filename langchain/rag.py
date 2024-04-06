from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain import hub
from langchain_core.prompts import PromptTemplate

template = """Based on the following pieces of context you will assume you understood the content and use it to answer the question.
If you don't know the answer, please only state that 'You don't know' without trying to elaborate further.
Use three sentences maximum and keep the answer as concise as possible.
Always say "thanks for asking!" at the end of the answer.

Context: {context}

Question: {question}

Helpful Answer:"""
rag_prompt = PromptTemplate.from_template(template)

llm = Ollama(model="llama2")
loader = WebBaseLoader(
    "https://www.bbc.com/news/world-us-canada-68737365"
##  "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html"
)
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OllamaEmbeddings())
retriever = vectorstore.as_retriever()
rag_chain = (
    {"context": retriever, "question": input}
    | rag_prompt
    | llm
    | StrOutputParser()
)
response = rag_chain.invoke("Ready to answer your question! \n")
print(response)