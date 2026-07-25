import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain.chat_models import chatOpenAI

import streamlit as st
# from dotenv import load_dotenv

os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{question}")
]
)
# streamlit framework
st.title('LLM-GEMINI PROJECT')
input_text=st.text_input("How may i hepl you")

#llm
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=1
)


parser = StrOutputParser()

chain = prompt | llm | parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
