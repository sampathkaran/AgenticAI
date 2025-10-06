# prompts are going to be dynamic so we use prompt template
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model = "gpt-5-nano", temperature=0.5)


# Method 1 - creating prompt template via the construtor - PromptTemplate is the contructor

template = """
        You are expert storage administrator
        Explain about the {keyword} in brief                                
 """

prompt = PromptTemplate(
    input_variables = ["keyword"],
    template = template
)

response = model.invoke(prompt.format(keyword = "wwpn"))
print(response.content)
print("------------------------------")

# Method2 - Creating Prompt template with variables

prompt_template = PromptTemplate.from_template(
    "Tell me the hours of flight between {source} and {destination}"
)

response = model.invoke(prompt_template.format(source = "CJB", destination = "SIN"))
print(response.content)
