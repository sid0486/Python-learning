from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.config import settings

engine = create_engine(settings.database_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)