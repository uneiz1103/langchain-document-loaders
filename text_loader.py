from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

loader = TextLoader('cricket.txt' , encoding='utf-8')

docs = loader.load()

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

chain = prompt | model | parser

result = chain.invoke({'poem': docs[0].page_content})

print(result)

# print(type(docs))

# print(len(docs))

# print(type(docs[0]))

# # print(docs[0].page_content)
# print(docs[0].metadata)

