from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__)

db = SQLAlchemy(myapp_obj)

from app import routes, models
