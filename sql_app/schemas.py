from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class DocumentBase(BaseModel):
    name: str
    content: str


class DocumentCreate(DocumentBase):
    pass


class Document(DocumentBase):
    id: int
    date: Optional[datetime]
