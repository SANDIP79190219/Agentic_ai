from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is a Capital of India",
    "Kolkatta is a Capital of West Bangal",
    "Paris is a Capital of France"
]
result = embedding.aembed_documents(documents)

print(str(result))

