# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.messages import SystemMessage,HumanMessage

# load_dotenv() # take env variable

# llm = ChatOpenAI(
#     model = "gpt-5-nano",
#     temperature = 0.5,
#     max_tokens = None,
#     timeout = None,
#     max_retries =2
# )

# # message = [("system", "you are helpful assistant who is a movie buff"),
# #            ("human", "who is illayaraja. give me in 2 sentence")]

# # response = llm.invoke(message)

# # print(response.content)


# #https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html

# system_message = SystemMessage(content="you are a humuorous assistant")
# human_message = HumanMessage(content="exaplin about world war 2 in 2 sentence")

# message = [system_message, human_message]

# response = llm.invoke(message)

# print(response.content)


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

# message = "who is the best motogtp rider in world in 2 sentence"
system_message = SystemMessage(content="you are  a travel planner")
human_message = HumanMessage(content="i want to go to bali from singapore")
llm = ChatOpenAI(model="gpt-5-nano")

message = [system_message, human_message]

response = llm.invoke(message)

print (response.content)