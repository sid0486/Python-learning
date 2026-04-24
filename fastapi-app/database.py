from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# database.py
db_url = "postgresql://postgres:sid0402@localhost:5432/fastapi_db"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False,autoflush= False,bind = engine)
