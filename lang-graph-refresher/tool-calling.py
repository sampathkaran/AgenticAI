from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.tools  import DuckDuckGoSearchRun, DuckDuckGoSearchResults 
from langgraph.checkpoint.memory import MemorySaver
import json
from dotenv import load_dotenv

load_dotenv()


# define the schema

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# create a tool
search_tool = DuckDuckGoSearchRun(max_results=2)
tools = [search_tool]


llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm_gemini_with_tools = llm_gemini.bind_tools(tools=tools)
#result = llm_gemini.invoke([HumanMessage(content="what is the weather now in singapore, give me in celcius")])
# result = llm_gemini_with_tools.invoke([HumanMessage(content="what is the weather now in singapore, give me in celcius")])
# print(result)


# Create a node

def chatbot(state: AgentState) -> AgentState:
    return {"messages" : llm_gemini_with_tools.invoke(state['messages'])}


