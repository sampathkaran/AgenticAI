from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv() # take env variable

llm = ChatOpenAI(
    model = "gpt-5-nano",
    temperature = 0.5,
    max_tokens = None,
    timeout = None,
    max_retries =2
)

message = "what is the capital singapore"

response = llm.invoke(message)

print(response.content)
