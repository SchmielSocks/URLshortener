"""
The flask application package.
"""

from flask import Flask
from FlaskWebProject1.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.create_all()

from FlaskWebProject1.urlModels import *
import FlaskWebProject1.views
from FlaskWebProject1.urlGen import *
