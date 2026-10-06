# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    question: str
    top_k: Optional[int] = 3

class SourceDocument(BaseModel):
    page_content: str
    page_number: int

class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceDocument]