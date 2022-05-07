from operator import length_hint
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, Length

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

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class DeleteForm(FlaskForm):
	username = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")

