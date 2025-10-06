from dotenv import load_dotenv # laod the environmental variables
from langchain_openai.chat_models import ChatOpenAI # to work with chatcompletion api

#load env variables

load_dotenv()

# construct messages - we specify role and specify the text
messages = [(
             "system",
             "you are helpful that translates from English to Tamil" 
            ),
            ("human", "I miss you Appa")

]

# initialize the chat model

model = ChatOpenAI(
    model = "gpt-5-nano", temperature = 0.5
)

# to get the response

response = model.invoke(messages)
print(response.content)

# or we can execute the message directly

response = model.invoke("coimbatore is ")
print(response.content)