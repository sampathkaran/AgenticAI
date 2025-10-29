# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.messages import SystemMessage,HumanMessage
# from langchain_core.prompts import PromptTemplate

# load_dotenv() # take env variable

# llm = ChatOpenAI(
#     model = "gpt-5-nano",
#     temperature = 0.5,
#     max_tokens = None,
#     timeout = None,
#     max_retries =2
# )

# prompt = PromptTemplate.from_template(
#     "you are an english to tamil translator"
#     "how to say {verb} in {language}")

# chain = prompt | llm 

# response = chain.invoke(
#     {
#         "language": "tamil",
#         "verb" : "Welcome",
#     }
# )

# print(response.content)
from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate ## this is used for newer gtp mpoodels
from dotenv import load_dotenv

load_dotenv()
# template = PromptTemplate.from_template("""
# You are python programming expert
# {query}
# """)

# prompt_template = template.invoke({"query": "write a fibbanoci series program"})
# # print(prompt_template)

llm = ChatOpenAI(
    model = "gpt-5-nano",
    temperature = 0.5,
    max_tokens = None,
    timeout = None,
    max_retries =2
)

# response = llm.invoke(prompt_template)
# print(response.content)

template = ChatPromptTemplate.from_messages([
    ("system", "you are a matchmaking expert"),
    ("human", "I am loking for a parter of a {gender}")
])

prompt_template = template.format_messages(gender="female")

response = llm.invoke(prompt_template)
print(response.content)