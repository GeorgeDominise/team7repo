from dataclasses import dataclass
from operator import length_hint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SellForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
#	price = IntegerField("Price", validators=[DataRequired()])
	description = StringField("Description")
	image_url = StringField("Image URL")
	submit = SubmitField("Submit")

class RegistrationForm(FlaskForm):
	username = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")

class ContactForm(FlaskForm):
	FirstName = StringField("First Name: ", validators=[DataRequired()])
	LastName = StringField("Last Name: ", validators=[DataRequired()])
	Message = StringField("Message: ", validators=[DataRequired()])	
	submit = SubmitField("Submit")