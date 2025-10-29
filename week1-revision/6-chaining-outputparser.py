from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
load_dotenv()

# Define schema and fields for the desired output
class Album(BaseModel):
    title_album: list[str] = Field(description="The name of the album")
    composition_year: list[int] = Field(description="The year the album is released")
    
# instatiate the parser and define the format instrcutions
parser = PydanticOutputParser(pydantic_object=Album)
format_instructions = parser.get_format_instructions()

# Create the prompt and the format instructions
prompt_template = ChatPromptTemplate.from_messages([("system", "You are an assistant that ONLY outputs valid JSON according to the given schema."),("human", "list the iconic/popular 10 albums composed by Michael Jackson {format_instructions}")])

# # update the prompt with the placeholder, we dont format messages as this will convert template to str and chain does to not accept str
# final_prompt_template = prompt_template.format_messages(format_instructions = format_instructions)

# define the LLM
llm = ChatOpenAI(model = "gpt-5-nano",temperature = 0.5)

# Create the chain
chain = prompt_template | llm | parser

# Generate response
response = chain.invoke({"format_instructions" : format_instructions})
print(response)