from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Config:

    # Database configuration
    DATABASE_USERNAME = 'root'
    DATABASE_HOST = 'localhost'
    DATABASE_NAME = 'records'

    SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{DATABASE_USERNAME}@{DATABASE_HOST}/{DATABASE_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

    # Create a configured "Session" class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create a base class for our class definitions
    Base = declarative_base()

    # Dependency to get DB session
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
