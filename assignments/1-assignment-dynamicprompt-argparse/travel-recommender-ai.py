from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import argparse

#load the env variables
load_dotenv()

# define the command line user input arguments using argparse
parser = argparse.ArgumentParser(description="This is a Travel Recommender AI")
# adding the positional argument
parser.add_argument("--city", type=str, required=True, help="Specify the destination city")
parser.add_argument("--days", type=int, required=True, help="The trip duration for travel")
parser.add_argument("--budget", type=str, choices=["low", "moderate", "high"], required=True, help="The budget range for your travel")
parser.add_argument("--traveller_type", type=str, choices=["solo", "family", "adventure", "luxury"], required=True, help="The type of traveller")
#To parse these arguments
args = parser.parse_args()

#construct the prompt template
prompt_template = ChatPromptTemplate.from_messages([("system", "You are a travel recommender assistant"),
                                      ("human", """
                                        I need a travel plan itenary to {city} city.
                                        The travel duration is for {days} days.
                                        I am looking for a budget level of {budget}.
                                        The traveller type is {traveller_type}.
                                        Opener - 1-2 line intro about the city \n
                                        Itinerary - Day by Day plan matching the number of days \n
                                        Tips - 2-3 short suggestion tailored to budget and traveller type \n
                                        Provide concrete travel suggestions not vague description
                                        Limit the output to 200 words
                                       """)])

# Dynmaically pass the values to the placeholders
variables = {
    "city" : args.city,
    "days" : args.days,
    "budget" : args.budget,
    "traveller_type" : args.traveller_type
    }

# initialization of the llm model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# create a chain to link the prompt and the llm
chain = prompt_template | llm

# pass the template to the llm model
response = chain.invoke(variables)

print(response.content)