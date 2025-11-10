from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from typing import TypedDict, Dict, Optional, List, Annotated
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages
from wikipedia import summary as wiki_summary

import numexpr
from dotenv import load_dotenv

load_dotenv()

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.1)

# define tools

@tool

#wikipedia tool
def wikipedia_tool(topic: str) -> str:
 """
 wikipedia search tool, input is a string value and output is a string value
 """
 try:
  return wiki_summary(topic, sentences=8, auto_suggest=False, redirect=True)
 except Exception as e:
  return f'Could not fetch from Wikipedia for {topic}. Error: {e}'

#Gemini Summarizer tool
def summarization_tool(text: str)-> str:
 """
 This is a summarization tool that provides summary of thegiven input string
 """
 if not text or "Could not fetch" in text:
  return f"There is no context to summarize"
 prompt = PromptTemplate.from_template.from_template([
  ("system" , "You are an text summarization assistant"),
  ("human", "Summarize the following text in 4-6 lines"
            "/n {context}"
            "/n Summary:")])
 chain = prompt | llm_gemini
 out = chain.invoke()


# #define schema for graph

# class WorflowState(TypedDict):
#     """
#     summary: will be rolling summary
#     """
#     query: str
#     context: Annotated[str, 'text fetched from wikipedia']
#     summary: Annotated[str, 'LLM generated']



# # Research Agent

# def research_agent(state:WorflowState)->WorflowState:
#     query = state.get('query', "")



# # Summarizer Agent


