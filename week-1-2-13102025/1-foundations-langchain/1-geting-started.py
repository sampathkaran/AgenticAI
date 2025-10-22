# ChatOpenAI is the class we use to work with LLM models
#https://python.langchain.com/docs/integrations/chat/openai/
#https://python.langchain.com/docs/integrations/providers/google/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv() # take env variable

llm_openai = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

llm_gemini= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

message= "what is the captial of Singapore"
response_openai = llm_openai.invoke(message)
response_gemini = llm_gemini.invoke(message)
print(f" Response from OpenAI: {response_openai.content}")
print(f" Response from Gemini: {response_gemini.content}")