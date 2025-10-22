from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field


load_dotenv()

llm = ChatOpenAI(model = "gpt-5-nano", temperature=0.5)

# single input request
single_response = llm.invoke("what is speedometer in 2 sentence")
print(single_response.content)

# batch input request
batch_response = llm.batch([
    "who is valentino rossi in 2 sentence"
    "I love my father karunakaran"
    "what is meaning of Idhal"])

for i, response in enumerate(batch_response):
    print(f"Response{i} +1: {response}")
