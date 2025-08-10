from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings()

documents = [
    "Virat ..................",
    "Ms Dhoni -----------------------",
    "Sachin xxxxxxxxxxxxxxxxxxxxx"
]

query = "tell me about virat"

doc_embedding = embedding.aembed_documents(documents)
query_embedding = embedding.aembed_query(query)

print(cosine_similarity([query_embedding], doc_embedding))
