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
from langgraph.checkpoint.memory import MemorySaver

import numexpr
from dotenv import load_dotenv

load_dotenv()

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.1)\


class Agentstate(TypedDict):
 query: str
 context: Annotated[str, 'text fecthed from wikipedia']
 summary: Annotated[str, 'summarized text from llm-generated']
 formatted_summary: Annotated[str, 'Formatted sunnary from llm-generated']

# define tools

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
 prompt = PromptTemplate.from_template("You are an text summarization assistant"
      "Summarize the following text in 4-6 lines"
            "/n {context}"
            "/n Summary:")
 chain = prompt | llm_gemini
 out = chain.invoke({'context': text})
 return out.content

#Formatter tool
def formatter_tool(summary: str) -> str:
 """
 This is a formatter tool that formates the summary as below 
 """
 if not summary:
  return "There is no summarty to format"
 prompt = PromptTemplate.from_template(""" 
  Summarized format for <query>:

 - Point 1

 - Point 2

 - Point 3
 {summary}                                    
 """)
 
 chain = prompt | llm_gemini
 out = chain.invoke({'summary': summary})
 return out.content


# Research Node

def research_node(state:Agentstate) -> Agentstate:
 query = state['query']
 if not query:
  state['context'] = "no query provided"
  return state
 context = wikipedia_tool(query)
 state['context'] = context
 return state

# Summary Node

def summarizer_node(state:Agentstate) -> Agentstate:
 context = state.get('context', "")
 summary = summarization_tool(context)
 state['summary'] = summary
 return state

# Formatter Node
def formatter_node(state:Agentstate)-> Agentstate:
 summary = state.get('summary', "")
 formatted_summary = formatter_tool(summary)
 state['formatted_summary'] = formatted_summary
 return state

graph = StateGraph(Agentstate)
graph.add_node("research_node", research_node)
graph.add_node("summarizer_node", summarizer_node)
graph.add_node("formatter_node", formatter_node)
graph.add_edge(START, "research_node")
graph.add_edge("research_node", "summarizer_node")
graph.add_edge("summarizer_node", "formatter_node")
graph.add_edge("formatter_node", END)

checkpointer = MemorySaver()
app = graph.compile(checkpointer=checkpointer)
initial_state = {'query': 'NVIDIA'}
final_state = app.invoke(initial_state, config={"configurable" : {'thread_id': "demouser1"}})
print(initial_state)
print("==========================")
# print(final_state)
print('\nContext:\n', final_state.get('context'))
print('\nSummary:\n', final_state.get('summary'))
print('\nFormatted_summary:\n', final_state.get('formatted_summary'))