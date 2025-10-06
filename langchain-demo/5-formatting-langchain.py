# we can format the output in required format using json format
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# first we define schema for output, we will include the schema along with prompt

#to define schema we use pydantic library

from pydantic import BaseModel, Field

# create a class inherting the basemodel class

class Engine(BaseModel):
    engine_hp: str = Field(description = "the horsepower of engine")
    engine_torque: str = Field(description = "the torque of engine")

model = ChatOpenAI(model = "gpt-5-nano", temperature = 0.5).with_structured_output(Engine)

response = model.invoke("explain about the honda ivtec engine")

print(response)


