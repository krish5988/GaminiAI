from langchain.prompts import PromptTemplate,ChatPromptTemplate,HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from langchain.chains import LLMChain,SimpleSequentialChain
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = (
    PromptTemplate.from_template("Tell me a joke about {topic}")
    + ", make it funny"
    + "\n\nand in {language}"
)
prompt.format(topic="sports", language="bengali")
llm1=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3, convert_system_message_to_human=True)
chain=LLMChain(llm=llm1,
               prompt=prompt,
               verbose=True)
print(chain.run(topic="sports", language="bengali"))

prompt2 = ChatPromptTemplate.from_messages([
     SystemMessage(content="You are a pirate"),
    # MessagesPlaceholder(variable_name="chat_hist"),
    HumanMessagePromptTemplate.from_template("give short story about- {content}")
    
])
prompt2.format_messages(content="I said hi")
chain=LLMChain(llm=llm1,
               prompt=prompt2,
               verbose=True)
print(chain.run({'content':"looting bank"}))

