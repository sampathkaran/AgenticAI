from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model = "gpt-5-nano", temperature=0.5)

system_message  = SystemMessage("you are a helpful airpilot assistance")
human_message = HumanMessage(" what is the use of flaps?")

# response

response = model.invoke([system_message, human_message])
print(response.content)