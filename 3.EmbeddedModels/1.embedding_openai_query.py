from langchain_openai import OpenAIEmbeddings
import asyncio
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
#result =  embedding.aembed_query("Delhi is a Capital of India")

async def main():
    result = await embedding.aembed_query("Delhi is a Capital of India")
    print(str(result))

asyncio.run(main())

