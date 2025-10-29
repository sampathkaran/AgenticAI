from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate 

load_dotenv() # take env variable


llm_gemini= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

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
    "topic" : "Quantum Consulting",
    "audience": "for scientists",
    "style" : "engaging", 
    "length" : "150 words"
}

response = chain.invoke(variables)
print(response)
