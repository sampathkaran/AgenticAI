from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate 
import argparse
load_dotenv() # take env variable


llm_gemini= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# define the input argparse

args = argparse.ArgumentParser(description="The dynamic prompt template with argprase")
args.add_argument("--topic", type=str, required=True, help="Topic of the explainer")
args.add_argument("--audience", type=str, required=True, help="Target the audience")
args.add_argument("--style", type=str, required=True, help = "Style of the explainer")
args.add_argument("--length", type=str, required=True, help="Length of the explainer")
parsed_args = args.parse_args()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         """you are expert asssitant. Adapt explanatuions to audience and style
         prefer short and concrete examples"""),
         ("user",
          """Write a {style} explainer on topic of {topic} for {audience} audience"
          Keep it {length}    
          Format: \n
          Opener: 1-2 lines \n
          Core: 2-3 bullet points \n
          Bottom Line: Single sentence starting with 'Bottom Line'
          """
          )
    ]
)
# lcel composition

chain = prompt | llm_gemini

variables = {
    "topic" : parsed_args.topic,
    "audience": parsed_args.audience,
    "style" : parsed_args.style, 
    "length" : parsed_args.length
}

response = chain.invoke(variables)
print(response.content)