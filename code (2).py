# app/services/rag_chain.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.config import settings
from app.services.vector_store import vector_manager

RAG_PROMPT_TEMPLATE = """
You are a precise technical document assistant. 
Answer the user's question using ONLY the provided context below.
If the answer cannot be deduced from the context, state clearly that you cannot find the answer in the provided document.

Context:
{context}

Question: {question}

Answer:
"""

class RAGPipeline:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            openai_api_key=settings.OPENAI_API_KEY
        )
        self.prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)
        self.output_parser = StrOutputParser()

    def query(self, question: str, top_k: int = 3):
        retriever = vector_manager.get_retriever(top_k=top_k)
        retrieved_docs = retriever.invoke(question)

        # Format context from retrieved documents
        context_str = "\n\n".join([doc.page_content for doc in retrieved_docs])
        
        # Run execution chain
        chain = self.prompt | self.llm | self.output_parser
        response_text = chain.invoke({"context": context_str, "question": question})

        # Format citations
        sources = [
            {
                "page_content": doc.page_content[:200] + "...",
                "page_number": doc.metadata.get("page", 0) + 1
            }
            for doc in retrieved_docs
        ]

        return {"answer": response_text, "sources": sources}

rag_pipeline = RAGPipeline()