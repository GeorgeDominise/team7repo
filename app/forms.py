from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SellForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
#	price = IntegerField("Price", validators=[DataRequired()])
	description = StringField("Description")
	image_url = StringField("Image URL")
	submit = SubmitField("Submit")

	
class RegisterForm(FlaskForm):
#Allows users to make a new account
    username = StringField("Enter your username:", validators=[DataRequired()])
    email = StringField("Enter an email:", validators=[DataRequired()])
    password = PasswordField("Enter a password:", validators=[DataRequired()])
    password_ver = PasswordField("Please verify your password:", validators=[DataRequired()])
    submit = SubmitField("Submit form")
