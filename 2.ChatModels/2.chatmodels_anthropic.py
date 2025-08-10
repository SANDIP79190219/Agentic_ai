from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

model = ChatAnthropic(model='')

result = model.invoke("What is the Capital of India")

print(result)


