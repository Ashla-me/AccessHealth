import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://username:password@localhost:3306/docaccess')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', 'your_twilio_account_sid')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', 'your_twilio_auth_token')

