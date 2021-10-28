from fastapi import FastAPI, HTTPException

import database
import crud
import schemas


database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    except:
        db.close()


@app.post("/api/documents/", status_code=201, response_model=schemas.Document)
def create_document(item: schemas.DocumentCreate):
    return crud.create_document(item)


@app.get("/api/documents/{document_id}/", response_model=schemas.Document)
def get_document(document_id: int):
    document = crud.get_document(document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found") 
    return document


@app.delete("/api/documents/{document_id}/", status_code=204)
def delete_document(document_id: int):
    document = crud.delete_document(document_id)
    return document
