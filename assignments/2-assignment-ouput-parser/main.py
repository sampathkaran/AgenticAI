from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from enum import Enum
from pydantic import BaseModel, Field
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from typing import Optional, List
import argparse
import json

load_dotenv()

parser = argparse.ArgumentParser(description="Specify the food review")
parser.add_argument("--review", type=str, required=True, help = "Restaurant food review")
parser.add_argument("--max_retries", type=int, required=True, help = "Max retries")
args = parser.parse_args()

class PriceRangeEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
class Restuarant(BaseModel):
    name: str = Field(description="The name of the restaurant")
    cuisine: str = Field(description="The type of cuisine eg Indian, Japanese etc")
    city: str = Field(default="", description="The city of Restaurant")
    rating: Optional[float] = Field(ge=0.0, le=5.0, description="The rating of restaurant")
    price_range: PriceRangeEnum = Field(description="The price range of menu")


parser = PydanticOutputParser(pydantic_object=Restuarant)
format_instructions = parser.get_format_instructions()

prompt = ChatPromptTemplate.from_messages([
                              ("system", "You are a restuarant information extractor"),
                              ("human",
                              """
                            #   You need to extract restaurant name, cuisine, city, rating, price_range from the review input
                            #   Output must be ONLY valid JSON(no mardown fences, no prose)\n
                            #   Do not fabricate facts. If the data is missing leave it empty or null as specified\n
                            #   Extract only what is present, never fabricate facts
                            #   {format_instructions}

                            You will receive a restaurant review.  
Extract the following (and only the following) information in ONE single JSON object:
- name (restaurant name, if mentioned)  
- cuisine (type of cuisine, if mentioned)  
- city (if mentioned; if not, output "")  
- rating (between 0.0 and 5.0, if mentioned; if not, output null)  
- price_range (low, medium, or high; based on inexpensive/moderate/expensive language)

Return ONLY valid JSON (no markdown fences and no explanatory text).  
Here are the JSON schema & instructions:  
{format_instructions}

Review: {review}
 """)])

llm_gemini= ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

variables = {
    "review" : args.review,
    "format_instructions" : format_instructions
} 

last_error_hint = ""

for attempt in range(args.max_retries + 1):
    if attempt == 0:
        prompt_prepared = prompt.format(**variables)
    else:
        retry_prompt = ChatPromptTemplate.from_messages([
            *prompt.messages,
            ("user",
               """ 
                     The previous output was invalid JSON, refere to 
                     Please correct the output to adhere to the format in(structions.
                     Please return ONLY the correct JSON that follows the exact schema.
                     Do not include any extra text
                     {last_error_hint}
                     """)
        ])
        prompt_prepared = retry_prompt.format(**variables)
    # invoke the model
    response = llm_gemini.invoke(prompt_prepared)
    content = response.content.strip() # remove new lines
    try:
        _ = json.loads(content)
    except Exception as e:
        last_error_hint = {str(e)}
        if attempt == args.max_retries:
            print("Reached max retries, exiting")
        else:
           continue
    print(f"The response from Gemini model on attempt ({attempt + 1})")
    print(response.content)
    break