from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mariadb+pymysql://root:@localhost:3306/newcommentsdb"
    CORS_HEADERS = "Content-Type"