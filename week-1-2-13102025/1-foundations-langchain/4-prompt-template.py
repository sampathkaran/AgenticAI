# ChatOpenAI is the class we use to work with LLM models
#https://python.langchain.com/docs/integrations/chat/openai/
#https://python.langchain.com/docs/integrations/providers/google/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate 

load_dotenv() # take env variable

llm_openai = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

llm_gemini= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template = PromptTemplate.from_template(
    """ You are a religious advisor
    question : {question} """  # here treat the question as a key 
)

template_object = template.invoke(
    {"question" : "what to do if I am stressed out"}
)

response_openai = llm_openai.invoke(template_object)
response_gemini = llm_gemini.invoke(template_object)

print(f" Response from OpenAI: {response_openai.content}")
print(f" Response from Gemini: {response_gemini.content}")