from langgraph.graph import StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from typing import TypedDict, Dict, Optional, List
from dotenv import load_dotenv


# load_dotenv()

# llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class AgentState(TypedDict):
    messages: str

def first_node(messages: str) -> str:
    messages = user_input['messages'] + "from node 1"
    return {"messages": messages}

def second_node(messages: str) -> str:
    messages = user_input['messages'] + "I am from node 2"
    return {"messages": messages}

workflow = StateGraph(AgentState)
workflow.add_node("first_node",first_node)
workflow.add_node("second_node",second_node)
workflow.add_edge("first_node", "second_node")
workflow.set_entry_point("first_node")
workflow.set_finish_point("second_node")

user_input = {"messages" : "hello"}

app = workflow.compile()
result = app.invoke(user_input)
print(result)


