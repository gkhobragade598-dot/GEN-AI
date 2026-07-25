import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Replace with your Gemini API Key
os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{question}")
])

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=1
)


parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke({
    "question": "Who won fifa 2026?"
})

print(response)