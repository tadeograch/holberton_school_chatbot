#!/usr/bin/env python

import xmltodict
import requests
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from fastapi import FastAPI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from langchain_core.runnables import RunnablePassthrough

# Initialize FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# Fetch and parse the sitemap to get URLs
sitemap_url = 'https://holbertonschool.uy/wp-sitemap-posts-page-1.xml'
site_map = xmltodict.parse(requests.get(sitemap_url).text)
urls = [url["loc"] for url in site_map["urlset"]["url"]]

# Load and process documents from URLs
web_loader = UnstructuredURLLoader(urls=urls)
data = web_loader.load()

text_splitter = RecursiveCharacterTextSplitter()
docs = text_splitter.split_documents(data)

# Initialize embeddings and vector store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)
retriever = vector_store.as_retriever()

# Define the prompt template for the chatbot
template = """
You are a chatbot that only provides final answers to questions about Holberton School in Uruguay based on the following context: {context}.

If you feel that you don't have enough information, just answer "I'm sorry, I don't have that information".

If you feel that the question has nothing to do with Holberton School, just answer "I can only answer questions about Holberton School".

Remember that you are likely answering someone trying to apply to Holberton School; be as helpful as possible.

Question: {question}

Helpful Answer:
"""

# Create the prompt template and output parser
chat_prompt = PromptTemplate.from_template(template)
output_parser = StrOutputParser()

# Initialize the language model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Define a function to format documents for context
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Create the chain 
chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | chat_prompt
    | llm
    | output_parser
)

# Add routes to the FastAPI app
add_routes(
    app,
    chain,
    path="/holberton_school_chatbot",
    enable_feedback_endpoint=True,
    enable_public_trace_link_endpoint=True,
    playground_type="default"
)

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)