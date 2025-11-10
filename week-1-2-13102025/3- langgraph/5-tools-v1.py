from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from typing import TypedDict, Dict, Optional, List, Annotated
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages
import numexpr

from dotenv import load_dotenv

load_dotenv()



@tool
def calculator(query: str) -> str:
    """
    A simple calculator tool, input is mathmaical expression
    """
    return str(numexpr.evaluate(query))

search_tool = DuckDuckGoSearchResults()
# create the collection of tools

tools = [search_tool, calculator]


llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1).bind_tools(tools)

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

def llm_node(state: AgentState) -> AgentState:
    # print("Messages passed to LLM:")
    # print(state["messages"])
    response = llm_gemini.invoke(state['messages'])
    # print("Intermediate reulst from llm:")
    # print(response)
    return {"messages" : response}

graph = StateGraph(AgentState)
graph.add_node("llm_node", llm_node)
graph.add_node("tools", ToolNode(tools))
graph.add_edge(START, "llm_node")
graph.add_conditional_edges("llm_node", tools_condition)
graph.add_edge("tools", "llm_node")
graph.add_edge("llm_node", END)

app = graph.compile()
app.get_graph().draw_mermaid_png(output_file_path="tools-graph.png")
result = app.invoke(
    {"messages": "what is the fixed deposit rate in SBI bank 2025 and also calculate 450-50 is ?"}
)
# print(result)
print(result['messages'][-1].content)