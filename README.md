# DocuMind AI — PDF Research & RAG Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-1C3C3C.svg)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-FF6F00.svg)
![OpenAI](https://img.shields.io/badge/Model-GPT--4o--mini-412991.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**DocuMind AI** is a production-ready, asynchronous **Retrieval-Augmented Generation (RAG)** engine designed to extract, chunk, embed, and query complex PDF documents. Built with **FastAPI**, **LangChain**, and **ChromaDB**, DocuMind AI delivers precise, context-aware answers paired with page-level citations to eliminate LLM hallucinations.

---

## 🔗 Interactive Demo & Repository Links

* **GitHub Repository:** [https://github.com/mrinalshaurya/documind-ai](https://github.com/mrinalshaurya/documind-ai)
* **Interactive API Playground:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) *(Access Swagger UI locally when server is running)*

---

## 🌟 Key Features & Technical Highlights

* **📄 Semantic PDF Processing:** Extracts structured text from multi-page PDFs using `PyPDF` and partitions it with `RecursiveCharacterTextSplitter` (~1,000 character chunks with 200-character overlap) to preserve contextual continuity.
* **⚡ Vector Similarity Search:** Generates high-dimensional embeddings via OpenAI (`text-embedding-3-small`) and stores them in a local, persistent **ChromaDB** instance for sub-second vector search.
* **🎯 Zero-Hallucination Q&A:** Employs LangChain Expression Language (LCEL) and `gpt-4o-mini` with strict system prompting to ensure answers are strictly backed by document context.
* **📍 Page-Level Citations:** Automatically returns exact page numbers and original text snippets alongside answer payloads for verifiable research.
* **🚀 Production REST Architecture:** Fully asynchronous FastAPI backend equipped with strict Pydantic data schemas, automated request validation, and OpenAPI integration.

---

## 🏗️ System Architecture & Working Workflow

```text
┌────────────────┐     1. Upload PDF     ┌────────────────────────┐
│  Client / UI   │ ────────────────────► │   FastAPI (/upload)    │
└────────────────┘                       └───────────┬────────────┘
        │                                            │
        │ 4. Query & Cited Response                  │ 2. Text Extraction & Chunking
        ▼                                            ▼
┌────────────────┐     3. Top-K Chunks   ┌────────────────────────┐
│ OpenAI GPT-4o  │ ◄──────────────────── │  ChromaDB Vector Store │
└────────────────┘                       └────────────────────────┘