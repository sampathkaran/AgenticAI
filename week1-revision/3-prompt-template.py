from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import PromptTemplate

load_dotenv() # take env variable

llm = ChatOpenAI(
    model = "gpt-5-nano",
    temperature = 0.5,
    max_tokens = None,
    timeout = None,
    max_retries =2
)

prompt = PromptTemplate.from_template(
    "you are an english to tamil translator"
    "how to say {verb} in {language}")

chain = prompt | llm 

response = chain.invoke(
    {
        "language": "tamil",
        "verb" : "Welcome",
    }
)

print(response.content)
