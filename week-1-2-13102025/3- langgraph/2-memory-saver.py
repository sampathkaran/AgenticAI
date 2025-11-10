from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph
from typing import TypedDict, Dict
from dotenv import load_dotenv

load_dotenv()

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# define schema for graph

class AgentState(TypedDict):
    prompt: str
    response: str


# create the node
def prompter_node(state: AgentState) -> AgentState:
    state['prompt'] = f"My prompt is {state['prompt']}"
    # print("prompt before modification:",state['prompt'])
    # print("response before modification:",state.get('response', ''))
    response = llm_gemini.invoke(state['prompt'])
    state['response'] = response.content
    # print("prompt after modification:",state['prompt'])
    # print("response after modification:",state['response'])
    return state 
   
user_input = {"prompt": "give me the tourist places in singapore in 2 sentence"}


graph = StateGraph(AgentState)
graph.add_node("prompter",prompter_node )
graph.set_entry_point("prompter")
graph.set_finish_point("prompter")

app = graph.compile()

app.get_graph().draw_mermaid_png(output_file_path="memory.png")

result = app.invoke(user_input)
print(result)