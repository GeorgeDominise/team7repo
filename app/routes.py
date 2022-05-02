from app import myapp_obj
from app import forms
from flask import flash, render_template, request
from app import db
from app.models import User

login_status = False # Temporary variable to test redirects based on whether user is logged in or not
username = "Team7 Shared Account"

@myapp_obj.route("/")
@myapp_obj.route("/home")
def home():
	return render_template("home.html", login_status=login_status)

@myapp_obj.route("/featured")
def featured():
	return render_template("featured.html", login_status=login_status)

@myapp_obj.route("/purchase")
def purchase():
	return render_template("purchase.html", login_status=login_status)

@myapp_obj.route("/signin")
def signin():
	#create a form
        # if form inputs are valid
        # search database for username
        # user = User.query.filter_by(...)
        # check the password
        # if password matches
        # login_user(user)
	return render_template("signin.html", login_status=login_status)

@myapp_obj.route("/register")
def register():
	#form = request.form
	#u = User(
	#	username = form['name'],
	#	email = form['email-address'],
	#	password = form['password']
	#)
	#user.password_hash(form['password'])
	#db.session.add(u)
	#db.session.commit()
	return render_template("register.html", login_status=login_status)

@myapp_obj.route("/faqs")
def faqs():
	return render_template("faqs.html", login_status=login_status)

@myapp_obj.route("/about")
def about():
	return render_template("about.html", login_status=login_status)

@myapp_obj.route("/sell", methods=["GET", "POST"])
def sell():
#	form = SellForm()
#	if form.validate_on_submit():
#		flash("Item put up for sale under name {}".format(form.name.data))
#		return redirect("{{  url_for('home') }}")
	return render_template("sell.html", login_status=login_status, form=form)
