from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from configparser import ConfigParser
import configparser
from flask_msearch import Search
from flask_login import LoginManager
from flask_migrate import Migrate
import os


basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__)
myapp_obj.config.from_mapping(
	SECRET_KEY = "yayaya",	SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db"))
db = SQLAlchemy(myapp_obj)

search = Search(db=db)
search.init_app(myapp_obj)
search.create_index(update=True)
MSEARCH_INDEX_NAME = os.path.join(basedir, "msearch")
MSEARCH_PRIMARY_KEY = "id"
MSEARCH_ENABLE = True

login_manager = LoginManager()
login_manager.init_app(myapp_obj)
login_manager.login_view = 'singin'

from app import routes, models

