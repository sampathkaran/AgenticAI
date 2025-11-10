from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict, Dict
from dotenv import load_dotenv

load_dotenv()

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# create the schema for state

class AgentState(TypedDict):
    prompt: str
    response: str

def prompter_node(state: AgentState) -> AgentState:
    response = llm_gemini.invoke(state["prompt"])
    state['response'] = response.content
    return {
        "prompt" : state['prompt'],
        "response" : state['response']
    }

user_input = {"prompt": "Give me similar framework like langgraph"}
checkpointer = MemorySaver()

# create the graph
graph = StateGraph(AgentState)
graph.add_node("prompter", prompter_node)
graph.set_entry_point("prompter")
graph.set_finish_point("prompter")
app = graph.compile(checkpointer=checkpointer)

config = {"configurable" : {"thread_id": "1"}}


#invoke the graph
result = app.invoke(user_input, config=config)
# print(result['response'])

snapshot = app.get_state(config)
print(snapshot.values)