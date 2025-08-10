from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core import output_parsers

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

prompt1 = template1.invoke({'topic':'Black hole'})

result  = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result2 = model.invoke(prompt2)

print(result2.content)
