from app import myapp_obj
from app import forms
from flask import flash, redirect, render_template, request
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
	return render_template("signin.html", login_status=login_status)

@myapp_obj.route("/register")
def register():
	return render_template("register.html", login_status=login_status)
	""" 	form = forms.RegistrationForm()

	if (form.validate_on_submit()): 
		username = form.username.data
		email = form.email.data
		password = form.password.data
		credentials_check = User.check_valid_credentials(username=username, email=email, password=password)

		if(credentials_check == False):
			flash('Please try again.')
			return redirect("/register")
			
		user = User(username=username, email=email, password=password)
		db.session.add(user)
		db.session.commit()
		flash("Account is now created. You may log in now.")
		return redirect("/login")
		
	return render_template("login.html", form=form) """

@myapp_obj.route("/faqs")
def faqs():
	return render_template("faqs.html", login_status=login_status)

@myapp_obj.route("/about")
def about():
	return render_template("about.html", login_status=login_status)


@myapp_obj.route("/settings")
def settings():
	return render_template("settings.html", login_status=login_status)


@myapp_obj.route("/sell", methods=["GET", "POST"])
def sell():
#	form = SellForm()
#	if form.validate_on_submit():
#		flash("Item put up for sale under name {}".format(form.name.data))
#		return redirect("{{  url_for('home') }}")
	return render_template("sell.html", login_status=login_status, form=form)

@myapp_obj.route("/contact", methods = ['GET', 'POST'])
def contactform():
	form = forms.ContactForm()
	if form.validate_on_submit():
		FirstName=form.FirstName.data
		LastName=form.LastName.data
		Message=form.Message.data
		flash("Thank you for submitting a contact form! We'll get back with you as soon as we can.")
		return redirect ("/contact")
	return render_template("contact.html", login_status=login_status, form=form)

#@myapp_obj.route("/findItems", )