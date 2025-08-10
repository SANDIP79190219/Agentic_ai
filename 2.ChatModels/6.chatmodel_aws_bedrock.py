from langchain_aws import ChatBedrockConverse
 
llm = ChatBedrockConverse(
        model="us.anthropic.claude-3-7-sonnet-20250219-v1:0" 
        )

response = llm.invoke("Your prompt goes here.")
print(response.content)