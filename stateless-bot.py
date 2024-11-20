import os

from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

embeddings = OpenAIEmbeddings()
vectorstore = PineconeVectorStore(
        index_name=os.environ["INDEX_NAME"], embedding=embeddings
)

chat = ChatOpenAI(verbose=True, temperature=0, model_name="gpt-3.5-turbo")

qa = RetrievalQA.from_chain_type(
    llm=chat, chain_type="stuff", retriever=vectorstore.as_retriever()
)    

res = qa.invoke("What are the applications of generative AI according the the paper? Please number each application.")
print(res) 

res = qa.invoke("Can you please elaborate more on application number 2?")
print(res)