## RAG Chatbot tutorial

https://medium.com/@suraj_bansal/build-your-own-ai-chatbot-a-beginners-guide-to-rag-and-langchain-0189a18ec401

1. Sign up and retrieve API keys for: OpenAI and Pinecone and store in `.env` file. Note the `.env.example`
1. Create index in Pinecone and store index name in `.env`
1. Create virtual environment `python3 -m venv .venv` and activate `source .venv/bin/activate`
1. Install packages `pip install -r requirements.txt`
1. Run `python ingestion.py` to ingest PDF and store vector embeddings in Pinecone store
1. Run `python stateless-bot.py` for example of stateless Q&A
1. Run `python stateful-boy.py` for example of Q&A with chat history in context
