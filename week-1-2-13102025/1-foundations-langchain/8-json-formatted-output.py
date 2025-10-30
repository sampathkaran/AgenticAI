# product information extractor
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate 
import json
import argparse 
# pyndatic is a library to define the schema
from pydantic import BaseModel, Field, ValidationError
from typing import Optional, List
from langchain.output_parsers import PydanticOutputParser
load_dotenv() # take env variable

# Run LLM --> Parse --> Validate
# we will retry if invalid, include error hint
# define schema with fields

class ProductInfo(BaseModel):
    name: str = Field(description="Name of the product"),
    description: str = Field(description="Description of the product, eg 'laptop', 'smartphone'"),
    price_estimate: Optional[float] = Field(description="Estimate the priceof the product in number. USe null if unknown")
    pros: List[str] = Field(description= "List the pros of product in bullet points")
    cons: List[str] = Field(description="List the cons of product in bullet points")


parser = argparse.ArgumentParser(description="JSON formatted output with pydantic")
parser.add_argument("--name", type=str, required=True, help="The name of hte product")
parser.add_argument("--description", type=str, required=True, help="The description of the product")
parser.add_argument("--max_retries", type=int, default=2, required=False, help="The category of hte product")
args = parser.parse_args()

llm_gemini= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

output_parser = PydanticOutputParser(pydantic_object=ProductInfo)
format_instructions = output_parser.get_format_instructions()
print(format_instructions)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         """ You are an information extraction assistant. Extract product information from user input
         If the field is unknown for provided text, set it to string null.
         Never fabricate the facts """),
         ("user",
          """
          Extract the product informatio from the text below and format is as per insturctions
          Name = {name}\n
          Description = {description}\n
          Follow the format insteuctions carefully\n
          1. Return ONLY VALID JSON that adheres to the format instructions.
          2. Do not include any commentary or markdown fences
          3. Adhere to JSON schema and field descriptions
          {format_instructions}
          """
          )
    ]
)

variables = {
    "name" : args.name,
    "description" : args.description,
    "format_instructions" : format_instructions
}

# print(prompt.messages)
# formatted_prompt = prompt.format_messages(**variables) 
# response = llm_gemini.invoke(formatted_prompt)
# print(response.content)

# Retry logic

last_error_hint = ""

for attempt in range(args.max_retries + 1):
    if attempt == 0:
        formatted_prompt = prompt.format_messages(**variables)# ** denotes to treat each key as seperate variable
        # print("Formatted prompt for attempt 1")
        # print(formatted_prompt)
    
    else:
        # retry logic with error hint appended to user message
        retry_prompt = ChatPromptTemplate.from_messages(
                 [
                    *prompt.messages,
                    ("user",
                     """ 
                     The previous output was invalid JSON, refere to 
                     Please correct the output to adhere to the format in(structions.
                     Please return ONLY the correct JSON that follows the exact schema.
                     Do not include any extra text
                     {last_error_hint}
                     """)])
        formatted_prompt = retry_prompt.format(**variables)
        print(formatted_prompt)
    # invoke the model
    response = llm_gemini.invoke(formatted_prompt)
    # print(f"The response from Gemini model for Attempt{attempt + 1}")
    # print (response.content)
    
    #convert the output to the json string
    raw_output = response.content.strip() #.content.strip() → removes extra spaces/newlines
    #print(raw_output)
    if raw_output.startswith("```") or raw_output.endswith("```"):
        # remove the markdown fences
        cleaned_output = "\n".join(raw_output.split("\n")[1:-1])
        #print(cleaned_output)
        # Adding try and exception logic
        try:
            _ = json.loads(cleaned_output)

        except Exception as e:
            last_error_hint = f"JSON Parsin Error: {str(e)}"
            print("validation Error", last_error_hint)
            if attempt == args.max_retries:
                 print("Max Retries Reached, Exiting")
                 break
            else:
                continue
    print("\nParsed Product Information:")
    print(cleaned_output)
    break



