import datetime

from sqlalchemy import Column, DateTime, Integer, String

from .database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(DateTime(timezone=True), default=datetime.datetime.now)
    content = Column(String, nullable=False)


documents = Document.__table__
