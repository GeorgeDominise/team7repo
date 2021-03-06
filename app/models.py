from app import db
from flask_login import UserMixin, LoginManager
from datetime import datetime

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	registered = db.Column(db.Boolean)

	items = db.relationship("Item", backref="author", lazy="dynamic")

	def is_authenticated(self):
        	return self.authenticated

	def __repr__(self):
		return "<User {}>".format(self.username)

class Item(db.Model):
	__searchable__ = ["name", "description"]

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index=True)
	price = db.Column(db.Integer, index=True)
#	stock = db.Column(db.Integer)
	description = db.Column(db.String(2048))
	image_url = db.Column(db.String(256))

#	timestamp = db.Column(db.DateTime, default=datetime.utcnow)

	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

	def __repr__(self):
		return "<Item {}>".format(self.name)
