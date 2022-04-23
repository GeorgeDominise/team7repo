from app import myapp_obj
from flask import flash, render_template

@myapp_obj.route("/")
@myapp_obj.route("/home")
def home():
	return render_template("home.html")
