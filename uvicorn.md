# DocuMind AI — PDF Research & RAG Engine

A high-performance Retrieval-Augmented Generation (RAG) backend API built with FastAPI, LangChain, and ChromaDB. It processes technical documents, extracts vector embeddings, and delivers context-aware, cited answers via LLMs.

## Key Features
- **Semantic Text Chunking:** Converts dense PDFs into overlapping text chunks optimized for vector similarity search.
- **Embedded Vector Database:** Persists vector embeddings locally using ChromaDB.
- **Cited Q&A Engine:** Generates hallucination-free answers mapped directly to source page numbers.
- **Async REST API:** Built on FastAPI with automatic Swagger UI documentation.

## Tech Stack
- **Language:** Python 3.10+
- **Framework:** FastAPI, Uvicorn
- **Orchestration:** LangChain / LangChain Expression Language (LCEL)
- **Vector DB:** ChromaDB
- **LLM Engine:** OpenAI `gpt-4o-mini`

## Quickstart

1. **Clone & Install:**
   ```bash
   git clone [https://github.com/your-username/documind-ai.git](https://github.com/your-username/documind-ai.git)
   cd documind-ai
   python -m venv venv && source venv/bin/activate
   pip install -r requirements.txt