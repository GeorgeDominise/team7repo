from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__)
login = LoginManager(myapp_obj)

myapp_obj.config.from_mapping(
	SECRET_KEY = "yayaya",
	SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
)

db = SQLAlchemy(myapp_obj)

from app import routes, models
