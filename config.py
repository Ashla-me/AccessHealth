from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Config:
    SECRET_KEY = 'ae3ecc52f525b916cb484cd7cc74c077c7ab04f0651206d6'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Define the database connection parameters
    db_user = 'ASHLA'
    db_password = 'ASHla1212!'
    db_host = 'localhost'
    db_name = 'bite'
  
    # Creates the database URI
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
    
    # Creates the engine
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
    
    # Creates a configured "Session" class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Creates a base class for our class definitions
    Base = declarative_base()

    # Dependency to get DB session
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
