from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-5-nano", temperature=0.5)

""" chat promt template has 3 messages
- System Message: This is used to baseline the AI assistant to set the mood or behaviouf of your assistant
- Human Messsage: Human input prompt
- AI Message: This stores the response from LLM
"""

template = ChatPromptTemplate([
    ("system", "you are helpful assistant where you answers are humourous"),
    ("human", "hey how are you ?"),
    ("ai", "I am good, thankyou"),
    ("human", "{userinput}")
    ])

prompt_value = template.format_messages(userinput = "tell me a joke about singlish")

response = model.invoke(prompt_value)
print(response.content)