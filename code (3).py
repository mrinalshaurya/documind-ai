# app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException, status
from app.schemas import QueryRequest, QueryResponse
from app.services.pdf_loader import process_pdf
from app.services.vector_store import vector_manager
from app.services.rag_chain import rag_pipeline

app = FastAPI(
    title="DocuMind AI - PDF RAG Engine",
    description="Production-ready REST API for indexing and querying complex PDFs using RAG.",
    version="1.0.0"
)

@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    file_bytes = await file.read()
    chunks = process_pdf(file_bytes, filename=file.filename)
    vector_manager.add_documents(chunks)

    return {
        "message": f"Successfully indexed '{file.filename}'",
        "chunks_created": len(chunks)
    }

@app.post("/query", response_model=QueryResponse)
async def query_document(request: QueryRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    
    result = rag_pipeline.query(question=request.question, top_k=request.top_k)
    return result

@app.get("/health")
def health_check():
    return {"status": "online"}