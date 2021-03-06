from sqlalchemy.sql import select

from .database import engine
from .models import documents
from .schemas import DocumentCreate


connection = engine.connect()


def create_document(item: DocumentCreate):
    document = documents.insert().values(**item.dict())
    result = connection.execute(document)
    id = result.inserted_primary_key[0]
    date = result.last_inserted_params()["date"]
    return {**item.dict(), "date": date, "id": id}


def get_document(document_id: int):
    s = select(documents).where(documents.c.id == document_id)
    result = connection.execute(s)
    document = result.fetchone()
    if document is None:
        return None
    return document


def delete_document(document_id: int):
    document = documents.delete().where(documents.c.id == document_id)
    result = connection.execute(document)
    return result
