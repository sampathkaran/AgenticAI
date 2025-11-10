what is AI?
- becuase of data and computation resources AI has emerdge now
- compute and data is the 2essential elements that make up AI

Foundations of AI:

- AI can do anaylsis and  some ability to toake action
- based on historical data it will learn the pattern and solve problem
- Natural Language Understanding -  a languague used by humans- the system that has ability to proces natural language is NLP
- AI can niterpret, understand and respond to human language, like chatgpt
- modalities - the type dataa like text, image, video, strcutred data of AI

ML:

- ML is a subset of AI
- it can do only analysis and cannot take action
- we use various ML models to find patterns

Deep Learning:
- subset of ML
- we use make use of specialized architecture called neural network

all the above helping in predictive analysis

for the above the data should be strucutured format

the aobve models were working with rules

with arch like transformers we get to generative AI where it can create new contet
based on the past like GPT

To work with Chatbot we need Generative AI

gen Ai is a type of AI

These are the arch used before in Generative AI
GeneratiVe Adversarial Networks (GAN)
Variational Autoenoders(VAES)
- data compression technique
- challenge - time taken was more
Synthetic Data Generation


Large Language Model :
- understand contxt by natural language
- can produce relevant and coherent(inline) with user input
- most of LLMs work with text data
- uses language modellig tehnique
- language modelling task is to find relationship between works in input 
- it creates vector maps to group the reatlionship between words

corpus ==> collection of text data


is no. of token = no.of words


Agentic AI

- work autonomoisly without human interaction 
- FM are the LLMs that are used to perform tasks such as text classification, langugate translation etc
- LLM can understand interpret NLU
- LLMs are context aware and it can perform really well


Agent - is a AI enbled sysyem which has ability to take decision based on certain input

Types of Agent:
- Business- Task Agent - automate predefine business workflow eg RPA, Microsoft Power Automate, Zapier APP integration. Here there is no thinking it has just rules
- Conversational Agent - Chatbots, customer service agents, engage user with NLB interface, has thinkinh
- Research Agents - good in gathering info, summarizing data eg scan docs, scan Knowledgebases and provide structured output eg preplexity AI 
- Alanlytics Agents - powerBi copilot/glean, focus on interpret structured datasets, insights dashboard and reports
- Developer Agents - tools like cusor, winsurf, gitub copilot, assit developers generation of code ?
- Domain Specific Agents - agents specialief for medical, legal 
- Browser using agents
- voice agents
- video agents

agents that use modality of text/code is commonly used 


traditional AU vs Agentic Ai


does no.of agents combine to form an agentic AI system ?
In AI agent system when the LLM does not have the data and get the data from duck duck go does it get trained in realtime as well while sending response to user ie when someone ask the same question again it coms from LLM?

Principles of Agentic AI

- Modulairty
- Scalablility
- Interoperability
- Reinorcement learning 

Frameworks for orchestration:

- Lang graph
   - pros 
      - supports modular orchestration
      - supports graph like structure
   - Tradeoff - required custom logic for advanced planning & mmeory
   - suited f-r: building single/multi agent systems
- Autogen
 - pros: powerful multiagent orchestration, multiple role assigment, 
 - tradeoff: complex for simple usecases
 - suited for : research base systems

 - CrewAI
  - pros: easy to learn ad use
  - TradeoffL limited customization
  - suited for: develop for started quick

- OpenAI agents SDL
- pros _ integration with openAi tool
- tradeoff


Langchain:

- each and evey model provider will provide an API
- common framework used for all models, so if we change the model later it is easier
- lc comes with prebuilt common pattern such for tool calling, chain of though, RAG
- building block approach ie for llm a block, tool a block etc


https://github.com/manifoldailearning/agentic-bootcamp/tree/main/1-foundations-langchain


Output format:

- When using template the system message is somewhat fixed
- we template the human messages in most of the time
- we difne a schema ie to decide waht outout filds should we see by specifying keys

MCP and A2A agent to agent:

MCP:

Basically an Agent uses tools to work with external appplication through api calls. The structure of apis exposed different for every application so we need a common protocol 


MCP is a communication fraemwork that definers how ythe agents connect and exchange data with external systems

every agent will have a mcp.conf file

- MCP works in a client server model


- A2A is bsaically agent to agent where the original agent will communicate with sub agent for a specific task.

- 
Chatcompletion is openAI's conversational API


# Week 2 notes - 25102025

- LLMs are pwoerful but hard to control in prod, that is where framework like lanchain will help.

- 3 Benefits of Langchain 
   - modularity
   - composability - it is like lego that will connect multiple blocks 
   - observability - tracking and monitoring agent

- Core Buliding Block that makes up Agentic AI system
   - Models: LLMs
   -  Prompts: Message, Templates and parametrized inputs
   - Memory - help agent to be context aware
   - Tools - External helpers like api intergations
   - Chains - Sequence of call to connect multiple steps like a pipeline
   - Agents - decision makers that select which tool to use

- LCEL - LangChain Expression Language
    purpose: Build readable and composable pipelines
    Fopr eg we connect multiple blocks using the | symbol (prompt|llm|output parser)



Langchain Core concepts 

why langchain ?
the llms are powerful models
to control llms in prod we use langchain library
provide strucutred way to biuid ai apps


Benefits 
- modularity
- composability - connect multiple blocks to work as a pipeline
- obserbvvability - track, debug the agent

core buidling blocks
- Models: LLMs,ChatModels 
- prompt: template, messages, parametrizzed inputs
- Memory: Short-term, long-term ,episodic
- Tools : seerachenginer, api integrations etc
- Chains: Sequence of calls combinig prompt, models ,tools
- Agents - decision makes that select which tools to use

LCEL - Langchain Expression Language
- creating composable pipelines


Ecosystem Layers-

- langchain is not library it is a ecosystem, it has 5 layers 



Json outpout SchemaL
keep fileds s mall and simple
add desc fior fields
alwats indcude addtonal instr
validate output and retry if invalid 


Comoom pitfalls and fixes:
- invsaliod JSON error - fix enforce valid json only and parser retires
- missing fields or wrongf data tyoes
- overlong outputs
- hallucinatios - fix alow unknown, forbid fabrications


Prompt Template vs Chatprompttemplate

the prompt template was used for older non chat like text based model
the latest gpt models is uses the chatprompttemplate and instead of single message we can send strucitrd messages like system, human, assistant etc


JSON output format

- We wil use pyndatic output parser to get the json output


Week 2 - 26102025

Memmory concepts in LLM

Concepts:
- when we ask followp quesion sometimes the LLM 

What is an Agent?
LLM by default is stateless -- ie it not context aware by default

Agent has to dynamic decision making
Agent decide what to do next base on context

LangChain Layers 

1. Core-Model, Prompts, memory
2. Orchestration - Chains, Agents, Langgraph
3. Integrations - Api,Database, VectorStores
4. Deployment: Docker, cloud functions, k8s
5. Monitoring: Langsmith, Traceloop , Prometheus


# Dynamic Prompt Template:
this is to send prompt template where we have placeholders that can be parameterized

Few shot prompt

we will add examples to the prompt 

Structured Output:

Schema design tips:
- keep the fields small and explicit
- define which fields are require and which are optional
- 

- Add a instruction to force the LLM to send a structured output

Insturction: Return only Valid Json, no extra text
setup validation and retry if invalid

Pitfall in output
- invalid json - the fix is to enforce valid JSON only + parser retry
- hallucination - Fix: allow unknown

Questions:
1. Ask assignment 1 where to add the instructions whether to system or human message ?
2. LCEL not used in the code 
3. No mardown frences


Lanchain Memory:

By default the LLMs are not context aware 
llm by default stateless
so we use memory to provide context
Ability for agent to remmber prevous conversation turns


Types of Langchain Memory

- ConversationBufferMemory - 
     This will store the entire full history
     But it can grow to larger
     best for short and simple chats

- ConvesationBufferWindowMemory 
    Last "N" exchange, eg where N=5 it  remembers last 5 conversation
    more efficient and avoid token overflow
    great for recent context only

- ConversationSummaryMemory 
    It usmmarizes the past interaction into keypoints and requires less memory.
    good for long chat

- Entoty Memory - 
         remember structured facts about people, place etc
         enable personalization across turns

Challenges:
- context can go large and hit the toekn limit and cause issues
- model might hallucinate
- need balance between retention and summarization



Which one to use


What is Agent?
We need agent ot dynamically do decsiion  making
agents decies what to do based on the context

Tools = it is the skill the agent can call

Agent loops
- send prompt to llm
- llns reasons about what to od
- agent will atomacticaly call the required rools
= agent will recive response from tool
- produce final answer



Questions:
The memory is native ot langchain, what they for creawi 


1/11/2025 class

LangGraph Library:

 - Orchestrating and memory is langgraph
 - Decision  grpah - giving capability to AI to make decision

Why Langgraph ?
LC was good at prototyping
when it comes to using tools LC was breaking
problems 
  - chained flows - linear and harfd to debug
  - no native state persistence

Building blokces of Langgraph
- nodes - atomic unit of langraph (llm call, tool call or simple python function)
- edges - define data flow and decision routes
- graph state - shared context that lives between nodes 
- checkpointers -  save state and helps us to rollback
- Memorysaver/redis saver - persistent state stores

what is the differenct from kc and kf
is node = agent 
what is diff working memenoy and agenrt memorty

         Langgrpah vs         Langchain
execution graph               linear
memory     statetful checpoint  traisent
debug       easy                hard


Understand graph stea:

graph state acts as memory of the agent
every nodes can read n or write in the state


LamngGraph Memory:

state schema

checpinters 

1- memory saver
2- in memory saver
3 redis saver/external stores

Type Annotations:

These type annotations will help to delcare the expected data types of the variables, function parameters and return value

eg

name: str = "sam"
age: int = 29

def greet(name: str) -> str:
      return f"Hello {name}"


Dictonaries 

movie = {"name" : "avengers, "year": 2019}
problem with dictonary is that it desont chek the data is correct type or not

to solve this we use a typed dictonary and we will use this to define state in langgraph

from typing import TypedDict
class Movie(TypedDict):
   name: str
   year: int
movie = Movie(name="avengers",year=2019)

===

LangGraph Peristence

Langraph has built in persistence layer implementted though checkpoints
When we compile the graph along with the checkpointer it saves a checkpoint
The chekpoint


do we need to use get() and typedict at same time 


Checkpointers:

- perist state per thread/run id

3 types of checkpointers used

- MemorySaver - in process 
- InMemorySaver - much more lightwrigt
- redissaver/externalstores - for prod

we specify the checkpoint in the compile method





State Schema:


We are going to setup

START -> Ingest_user -> chat -> summarize_if_long -> END



Typed Dict:
- to ensure the data is in partuclar sturcture we used typed dict

Union:L
Allows to declare a value of more than one type

Optional:

Itcan be of data type or nonw
Any:

cabn be any data typr


LambdaA:



State:

- it is a shared data strcuture that hold current information or context of the application
- it is like app mempry
- amalogy white bosrd is state and participants are nodes

Nodes:

- node are indicutin functions that perform specific task
- it has a input (current state) and process it and producrs and output or updated state

Graph:

- A graph is structure to map how nodes and connected and executed
- think of a roadmap 

Edges:

are the connection between the nodes that determine the flow of exectuion

Tools
tools are specialized functions or utilities that node can utilize

Toolnode:
it job is to run tool

Stategraph:

Build and comile graph structure
- manages nodes ,edgews and overall state

Messages:

Humanamessage
AI message -respinse frok kll
system emssage: used to proviude untrctions orcontet
Toool message: used fopr sp[ecfic tool 
Fction message: represent the result of function casll


Tools:

To make the AI perofrm an action we have to provide it with tools

we wil include a calcuator or a text modifier


Loop 
inpout --> resoning --> decide to call tool or genetate output and then contuniue reasongin again and loop unitl it is satisfied

we will use a node call tool node by using @tool
use a tool for single purprose function

Then biding the tools to the LLM




Q
deos the llm recoginzes the tools by its logical function name ?
is the annotated metadata for llm



