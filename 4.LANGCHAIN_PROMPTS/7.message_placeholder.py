from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

# Chat_template
chat_template=ChatPromptTemplate([
    ('system', 'you are a helpful assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])
# load chat history
chat_history = []
with open('chat_history.txt') as f:
    for line in f:
        chat_history.append(line)
 
# create prompt 
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'where is my refund'})

print(prompt)

