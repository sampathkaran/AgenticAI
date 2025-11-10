# Travel Recommender with State Memory
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from typing import TypedDict, Dict, Optional, List
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv

load_dotenv()

llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# define the schema for graph

class AgentState(TypedDict):
    """
    input: latest user inpit
    summary: rolling summary
    messages: ordered chat history
    """
    messages: List[BaseMessage] # list of base message objects
    input: str 
    summary: Optional[str] # optional means it can be value of str or none

# ingest user


#adding human message to state.messages
def ingest_user(state: AgentState) ->AgentState:
    messages = list(state.get("messages", [])) # list ensure it is a list
    user_text = state['input']
    messages.append(HumanMessage(content=user_text))
    return {"messages" : messages}

# # Validation
# state = {
#     "messages": [],
#     "input": "Hello there!",
#     "summary": None
# }


#Chat node - where message and summarization as system message are passed to LLM and the 
# llm aimessage is appended to the messages
def chat_node(state: AgentState) -> AgentState:
    messages = list(state.get("messages", []))
    summary = state.get("summary", "")
    complete_message : List[BaseMessage] = []
    if summary:
        complete_message.append(SystemMessage(content=f"This is the current conversation summary : {summary}"))
    complete_message.extend(messages)
    response = llm_gemini.invoke(complete_message)
    messages.append(AIMessage(content=response.content))
    return {"messages" : messages}

#summarization node - 
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a exeprt creating consice summaries of conversation"),
    ("human", "give th following conversation histroy, provide concise summary focussing on key fact and preferences"
    "and deisions:\n\n{conversation_history}")])

threshold = 2 # max no.of messages before summarize

def summarization_node(state:AgentState) -> AgentState:
    messages = list(state.get("messages", []))
    summary = state.get('summary', "")
    if len(messages) < threshold:
        return {"summary" : summary} # no update
    
    # generate new summary  
    conversation_text = "\n".join(f"{msg.type}:{msg.content}" for msg in messages)
    prompt = summary_prompt.format_prompt(conversation_history = conversation_text).to_messages()
    response = llm_gemini.invoke(prompt)
    generated_summary = response.content
    
    return{"summary" : generated_summary}

# Build the graph
graph = StateGraph(AgentState)
graph.add_node("ingest_user",ingest_user)
graph.add_node("chat_node",chat_node)
graph.add_node("summarization_node",summarization_node)

graph.add_edge(START, "ingest_user")
graph.add_edge("ingest_user", "chat_node")
graph.add_edge("chat_node","summarization_node")
graph.add_edge("summarization_node", END)


checkpointer = MemorySaver()
app= graph.compile(checkpointer=checkpointer)
app.get_graph().draw_mermaid_png(output_file_path="memoryhandson.png")

def run_turn(user_input: str, thread_id: str):
    result = app.invoke(
        {"input" : user_input},
        config = {"configurable":{"thread_id": thread_id}}
        )
    return result

if __name__=="__main__":
    thread_id=1
    user_input = "I am planning a trip to coimbatotre" 
    s1 = run_turn(user_input, thread_id)

    print("After turn 1:")
    print(s1['messages'][-1].content)


    user_input = "how is the weather there "
    s2 = run_turn(user_input, thread_id)

    print("After turn 2:")
    print(s2['messages'][-1].content)
  


    user_input = "Suggst me some top restaurants "
    s3 = run_turn(user_input, thread_id)

    print("After turn 3:")
    print(s3['messages'][-1].content)
  




