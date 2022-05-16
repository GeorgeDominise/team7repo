from dataclasses import dataclass
from operator import length_hint
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.validators import DataRequired, InputRequired, Email, Length

class SellForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	price = FloatField("Price", validators=[DataRequired()])
#	description = StringField("Description")
#	image_url = StringField("Image URL", validators=[DataRequired()])
	submit = SubmitField("Sell Item")

class RegistrationForm(FlaskForm):
	username = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class DeleteForm(FlaskForm):
	username = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Delete Account")

class ContactForm(FlaskForm):
	FirstName = StringField("First Name: ", validators=[DataRequired()])
	LastName = StringField("Last Name: ", validators=[DataRequired()])
	Message = StringField("Message: ", validators=[DataRequired()])
	submit = SubmitField("Submit")

class ReviewForm(FlaskForm):
	Username = StringField('Username: ', validators=[DataRequired()])
	Product = StringField("Product Name: ", validators=[DataRequired()])
	Review = StringField("Review: ", validators=[DataRequired()])

