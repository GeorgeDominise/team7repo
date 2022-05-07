from app import myapp_obj
from app import forms
from flask import Flask, render_template, request, url_for
from flask import flash, redirect, render_template, request
from app import db
from app.models import User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()
login_manager.init_app(myapp_obj)

@login_manager.user_loader
def load_user(username):
	return User.get(username)
#from flask_login import LoginManager



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


@myapp_obj.route("/signin", methods=["GET","POST"])
def signin():
	global login_status
	form=forms.LoginForm()
	if form.validate_on_submit():
		user= User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password_hash, form.password.data):
				#login_user(user, remember=form.remember_me.data)
				login_status=True
				return redirect('/')
			else:
				return 'Invalid password'
		else:
			return 'Invalid username'
	return render_template("signin.html", login_status=login_status, form = form)

@myapp_obj.route("/register", methods = ['GET', 'POST'])
def register():
	form = forms.RegistrationForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		u = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
		db.session.add(u)
		db.session.commit()
		print(f"Congrats! Account Successfully Created!")
		return redirect ("/signin")
	return render_template("register.html", login_status=login_status, form=form)

@myapp_obj.route("/deleteaccount", methods=["GET","POST"])
def deleteaccount():
    global login_status
    deleteform = forms.DeleteForm()
    print("byebye")
    if deleteform.validate_on_submit():
        u= User.query.filter_by(username=deleteform.username.data).first()
        db.session.delete(u)
        db.session.commit()
        login_status = False
        print(f"Account Successfully Deleted!")
        return redirect("/")
    print("Delete Account Ends Here!")
    return render_template("deleteaccount.html", deleteform=deleteform)


@myapp_obj.route("/faqs")
def faqs():
	return render_template("faqs.html", login_status=login_status)

@myapp_obj.route("/about")
def about():
	return render_template("about.html", login_status=login_status)


@myapp_obj.route("/settings")
#@login_required
def settings():
	#form =forms.SettingsForm()
	#form.username.data = username
	#form.email.data = email
	#form.password_hash.data = password_hash
	#user = user(username=form.username.data, email=form.email.data, password_hash= form.password_hash.data)
	#db.session.commit()
	return render_template("settings.html", login_status=login_status)

@myapp_obj.route("/sell", methods=["GET", "POST"])
def sell():
#	form = SellForm()
#	if form.validate_on_submit():
#		flash("Item put up for sale under name {}".format(form.name.data))
#		return redirect("{{  url_for('home') }}")
	return render_template("sell.html", login_status=login_status, form=form)

@myapp_obj.route('/logout')
def logout():
	logout_user()
	login_status=False
	return render_template("home.html", login_status=login_status)

