# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from pydantic import BaseModel, Field


# load_dotenv()

# class Vehicle(BaseModel):
#     engine_cylinder: int = Field(description = "the no.of cyclinders in engine")
#     transmission: str = Field(description = "the gear transmission type")

# llm = ChatOpenAI(model = "gpt-5-nano",temperature = 0.5).with_structured_output(Vehicle)

# response = llm.invoke("what is the technical specification of honda city generation 4")

# print(response)

# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
# from dotenv import load_dotenv
# load_dotenv()

# from langchain.output_parsers import PydanticOutputParser
# from pydantic import BaseModel, Field  # to create pdantic object and the datatypes to be declared

# llm = ChatOpenAI(model = "gpt-5-nano",temperature = 0.5)

# # Define output data types within the class and intialize a parser

# class Players(BaseModel):
#     values: list = Field(description='python list of dictonaries containing playername and nationality')
#     city: str = Field(description='Give me the most popluar country across the list')
# parser = PydanticOutputParser(pydantic_object=Players)
# # check the format instructions
# # print(parser.get_format_instructions())

# # Setup the Request 
# # we define the prompt template first
# human_prompt = HumanMessagePromptTemplate.from_template("{request}\n{format_instructions}")
# chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

# request = chat_prompt.format_prompt(
#     request = "Give me facts about top 10 cricket players",
#     format_instructions = parser.get_format_instructions()
# ).to_messages()

# results = llm(request)
# print(results)
# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# from dotenv import load_dotenv
# from pydantic import BaseModel, Field
# from langchain.output_parsers import PydanticOutputParser

# load_dotenv()

# # define the output schema and initialize the parser

# class Movies(BaseModel):
#     movie_title : str = Field(description="The title of the movie")
#     movie_genre : list[str] = Field(description="The genre of movie in list")
#     movie_rating : float = Field(description="The rating of the movie")

# llm = ChatOpenAI(model = "gpt-5-nano",temperature = 0.5).with_structured_output(Movies)

# # response = llm.invoke("share me the details of movie dark night")

# # print(response)

# pydanticParser = PydanticOutputParser(pydantic_object=Movies)

# # print(pydanticParser.get_format_instructions)

# prompt = ChatPromptTemplate.from_messages([("human", "Give me the details of movie American Hustle {format_instructions}")])
# # print(prompt)
# # print("-------------------")
# # print(prompt.format_prompt)

# response = llm.invoke(prompt.format(format_instructions = pydanticParser.get_format_instructions()))
# print(response)

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
load_dotenv()

# define the schema and fields
class CarExpert(BaseModel):
    brand: str = Field(description="The brand of car")
    model: str = Field(description="model name of car")
    country: str = Field(description="coUntry of sales")

# Create Parser using schema above
parser = PydanticOutputParser(pydantic_object=CarExpert)

# Generate format instructions for LLM
format_instructions = parser.get_format_instructions
# print(format_instructions)

# Create a prompt template including the format instructions
template = ChatPromptTemplate.from_messages([("human","give me the top 10 cars in {country} {format_instructions}")])

# Dynamically update the promt with the actual contents from placeholder
final_prompt = template.format_messages(country = "India", format_instructions=format_instructions)

# Send the prompt ot the LLM
llm = ChatOpenAI(model = "gpt-5-nano",temperature = 0.5)
response = llm.invoke(final_prompt)

# Parse the output
parsed_output = parser.parse(response.content)
print(parsed_output)