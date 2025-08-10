from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from typing import TypedDict, Annotated, Optional, Literal
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city person belong to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions() }
)

"""
prompt = template.invoke({'place': 'indian'})

print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)
"""

"""write above using chain"""

chain = template | model | parser
final_result = chain.invoke({'place': 'indian'})
print(final_result)