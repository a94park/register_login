from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from config import Config

app = Flask(__name__)

CORS(app, supports_credentials=True)

bcrypt = Bcrypt(app)

#CONFIGS
app.config.from_object(Config)

db = SQLAlchemy(app)

import routes

if __name__ == "__main__":
    app.run(debug=True)