from fastapi import FastAPI, HTTPException

from . import crud
from .database import Base, engine
from .schemas import Document, DocumentCreate


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/api/documents/", status_code=201, response_model=Document)
def create_document(item: DocumentCreate):
    return crud.create_document(item)


@app.get("/api/documents/{document_id}/", response_model=Document)
def get_document(document_id: int):
    document = crud.get_document(document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@app.delete("/api/documents/{document_id}/", status_code=204)
def delete_document(document_id: int):
    document = crud.delete_document(document_id)
    return document
