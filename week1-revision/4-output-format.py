from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field


load_dotenv()

class Vehicle(BaseModel):
    engine_cylinder: int = Field(description = "the no.of cyclinders in engine")
    transmission: str = Field(description = "the gear transmission type")

llm = ChatOpenAI(model = "gpt-5-nano",temperature = 0.5).with_structured_output(Vehicle)

response = llm.invoke("what is the technical specification of honda city generation 4")

print(response)
