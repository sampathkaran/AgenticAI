from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

message = "Explain about coimbatore city in 2 sentence"

response = llm.invoke(message)

print(response.content)