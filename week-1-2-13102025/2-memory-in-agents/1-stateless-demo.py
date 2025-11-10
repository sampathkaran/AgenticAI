# this to understand why we need memory

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate 
import argparse
load_dotenv() # take env variable


llm_gemini= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt= ChatPromptTemplate.from_messages([
    ("system", "You are a concise assistant. answer as briefly as possible"),
    ("human", "{user_input}")
])

chain = prompt | llm_gemini

print("Stateles Demo. Type exit to quit")

while True:
    user_input = input("You:")
    if user_input.lower() == "exit":
        print("Exiting")
        break
    else:
        variables = {"user_input": user_input}
        response = chain.invoke(variables)
        print("bot", response.content)
        