from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

# 1.prompt -> detailed report 
template1 = PromptTemplate(
    template='write a detailed report on topic {topic}',
    input_variables=['topic']
)
# 2.prompt -> summary
template2 = PromptTemplate(
    template='write a five line summary on following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)

