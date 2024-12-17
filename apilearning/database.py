from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABSE_URL = 'postgresql:/postgres:Bladehunter09@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABSE_URL)
        
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

