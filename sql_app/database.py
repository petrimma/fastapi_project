import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

SQLALCHEMY_DATABASE_URL = (f"postgresql://{os.environ.get('POSTGRES_USER')}:"
                           f"{os.environ.get('POSTGRES_PASSWORD')}@"
                           f"{os.environ.get('DB_HOST')}/"
                           f"{os.environ.get('DB_NAME')}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
