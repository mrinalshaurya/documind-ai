from fastapi import FastAPI

app = FastAPI(title="DocuMind AI - RAG Engine")

@app.get("/")
def read_root():
    return {"message": "DocuMind AI is running smoothly!"}