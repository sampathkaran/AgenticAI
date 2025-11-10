from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchResults
from langgraph.prebuilt import ToolNode
load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

search_tool = DuckDuckGoSearchResults(max_result=2)
tools = [search_tool]

llm_gemini= ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm_with_tools = llm_gemini.bind_tools(tools=tools)



def chatbot_node(state: AgentState)-> AgentState:
    return {
        "messages" : llm_with_tools.invoke(state['messages'])
    }

def tool_router(state: AgentState) -> AgentState:
    last_message = state['messages'] [-1]

    if hasattr(last_message, "tool_calls") and (len(last_message.tool_calls) > 0):
        return "tool_node"
    else:
      return END
    
tool_node = ToolNode(tools=tools)
    
graph = StateGraph(AgentState)
graph.add_node("chatbot", chatbot_node)
graph.add_node("tool_node", tool_node)
graph.set_entry_point("chatbot")
graph.add_conditional_edges("chatbot", tool_router)
graph.add_edge("tool_node", "chatbot")

app=graph.compile()

while True:
    user_input = input("User:")
    if user_input in ["exit", "end"]:
        break
    else:
        result = app.invoke({
            "messages" : [HumanMessage(content=user_input)]
        })
       
    print(result)