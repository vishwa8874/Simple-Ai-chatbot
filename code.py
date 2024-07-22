from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_community.llms import Ollama


import os

os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANCHAIN_TRACING_V2"] = "True"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a assistant. provide response to the user"),
        ("user","question:{question}")
    ]
)


st.title('lanchain simple chatbot')
input_text = st.text_input("search the topic")

llm = Ollama(model = "phi3")
OutputParser = StrOutputParser()
chains = prompt|llm|OutputParser

if input_text:
    st.write(chains.invoke({'question':input_text}))