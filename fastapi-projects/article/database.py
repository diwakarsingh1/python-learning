from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_sum _thread": False})


SessionLocal = sessionmaker(bind=engine, autoCommit=False, autoflush=False)
Base = declarative_base()

