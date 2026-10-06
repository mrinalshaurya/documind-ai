# app/services/pdf_loader.py
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List

def process_pdf(file_bytes: bytes, filename: str) -> List[Document]:
    """Saves uploaded bytes to a temp file, extracts text, and chunks it into semantic blocks."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file_bytes)
        tmp_path = tmp_file.name

    loader = PyPDFLoader(tmp_path)
    raw_docs = loader.load()

    # Split text into 1,000 character chunks with 200 character overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_documents(raw_docs)

    # Attach original filename into metadata
    for chunk in chunks:
        chunk.metadata["source_file"] = filename

    return chunks