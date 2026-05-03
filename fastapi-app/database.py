import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = os.getenv(
    "DATABASE_URL",
    "postgresql://siddhi:sid0402@localhost:5432/fastapi_db"
)

engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)