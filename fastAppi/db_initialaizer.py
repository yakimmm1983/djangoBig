from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'postgresql+psycopg2://postgres:1@localhost:5432/postgres'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()