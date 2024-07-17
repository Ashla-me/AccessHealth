from flask_sqlalchemy import SQLAlchemy, db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import JWTManager

class Config:
    SECRET_KEY = 'ae3ecc52f525b916cb484cd7cc74c077c7ab04f0651206d6'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = '861af9062c612f4352007ea17eb8c1545857418b3007e36b024daec9bf7861c5'
    
    # Define the database connection parameters
    db_user = 'root'
    db_password = 'ASHla1212!'
    db_host = 'localhost'
    db_name = 'bite'
  
    # Creates the database URI
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://'bite:ASHla1212!@localhost/mydatabase'
    
    # Creates the engine
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
    
    # Creates a configured "Session" class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Creates a base class for our class definitions
    Base = declarative_base()

    # Dependency to get DB session
    def get_db():
        db = SessionLocal() # type: ignore
        try:
            yield db
        finally:
            db.close()
