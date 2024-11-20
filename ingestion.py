import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

# Load the document
loader = PyPDFLoader("data/impact_of_generativeAI.pdf")
document = loader.load()

# Split the document into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(document)
print(f"created {len(texts)} chunks")

embeddings = OpenAIEmbeddings(openai_api_type=os.environ.get("OPENAI_API_KEY"))
PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ.get("INDEX_NAME"))