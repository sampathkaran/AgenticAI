from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI


load_dotenv()
messages = [(
    "system",
    "you are help assistant translate from english to tamil"
),
(
    "human", "I love programming in python"
)
]

# initialize the chat model
model = ChatOpenAI(model = "gpt-3.5-turbo", temperature = 0.5)

# Response
response = model.invoke(messages)
print(response.content)

response = model.invoke("what is the lastest new in tamilnadu")
print(response.content)