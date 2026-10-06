# app/services/vector_store.py
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from app.config import settings

class VectorStoreManager:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        self.vector_db = Chroma(
            persist_directory=settings.CHROMA_DB_DIR,
            embedding_function=self.embeddings
        )

    def add_documents(self, documents):
        self.vector_db.add_documents(documents)

    def get_retriever(self, top_k: int = 3):
        return self.vector_db.as_retriever(search_kwargs={"k": top_k})

vector_manager = VectorStoreManager()