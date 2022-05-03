import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
        SECRET_KEY = "a74161293d644d8f1ccca5be3f034df8" #MD5 Hash for "team7"
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
        SQLALCHEMY_TRACK_MODIFICATIONS = False
