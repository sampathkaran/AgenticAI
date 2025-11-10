from typing import TypedDict
from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate 

load_dotenv() # take env variable

llm_gemini= ChatGoogleGenerativeAI(model="gemini-2.5-flash", temnperature=0.5)

class AgentState(TypedDict):
    input: str
    output: str


def llm_node(state: AgentState)-> AgentState:
    user_input = state.get("input", "")
    response = llm_gemini.invoke(user_input)
    return {
        "input": state['input'],
        "output": response.content}


graph = StateGraph(AgentState)
graph.add_node("llm", llm_node)
graph.add_edge(START, "llm")
graph.add_edge("llm", END)

app = graph.compile()

input_state = {"input": "Hello, how are you ?"}
result = app.invoke(input_state)
print(result['output'])
