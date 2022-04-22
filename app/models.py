from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	items = db.relationship("Item", backref="author", lazy="dynamic")

	def __repr__(self):
		return "<User {}>".format(self.username)

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index=True)
	price = db.Column(db.Integer, index=True)
	image_url = db.Column(db.String(256))

	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

	def __repr__(self):
		return "<Item {}>".format(self.name)
