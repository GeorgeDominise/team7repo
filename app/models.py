from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	registered = db.Column(db.Boolean)

	items = db.relationship("Item", backref="author", lazy="dynamic")

	""" def __init__(self, username, email, password_hash):
		self.username = username
		self.set_password(password_hash)
		self.email = email
		self.public = True

	def get_id(self):
		return self.id
		
	def set_password(self, password_hash):
		self.password_hash = generate_password_hash(password_hash)

	def check_password(self, password_hash):
		return check_password_hash(self.password_hash, password_hash)

	@staticmethod
	def check_valid_credentials(username, email, password_hash):
		credentials_valid = True
        # what if pass is incorrect?
		# credentials_valid=False """

	def __repr__(self):
		return "<User {}>".format(self.username)

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index=True)
	price = db.Column(db.Integer, index=True)
	description = db.Column(db.String(2048))
	image_url = db.Column(db.String(256))

	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

	def __repr__(self):
		return "<Item {}>".format(self.name)
