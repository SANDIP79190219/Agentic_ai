from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

model = ChatGoogleGenerativeAI(model='')

result = model.invoke("What is the Capital of India?")

print(result)

