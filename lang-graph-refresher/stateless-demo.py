from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver
import json
from dotenv import load_dotenv

load_dotenv()

memory = MemorySaver()

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Create schema for graph

class Agentstate(TypedDict):
     messages: Annotated[list, add_messages]

# create a node

def first_node(state: Agentstate)-> Agentstate:
     return {"messages" : llm_gemini.invoke(state['messages'])}

# create a graph
graph = StateGraph(Agentstate)
graph.add_node("first_node", first_node)
graph.set_entry_point("first_node")
graph.set_finish_point("first_node")

app = graph.compile(checkpointer=memory)

config = {"configurable": {
     "thread_id": 1
}}

# r1 = app.invoke({"messages": HumanMessage(content="Hello my name is Sam")}, config=config)


# r2 = app.invoke({"messages": HumanMessage(content="What is my name")}, config=config)
# # print(r1)
# # print("\n")
# # print(r2)
# print(app.get_state(config=config))



while True:
     user_input = input("You:")
     if user_input in ["exit", "end"]:
          print("Exiting the conversation,bye")
          break
     else:
        r = app.invoke({"messages": user_input}, config=config)
        print("AI Response:", r['messages'][-1].content)
          
     