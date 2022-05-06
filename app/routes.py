from app import myapp_obj, forms
from app.models import User, Item
from flask import flash, render_template

login_status = False # Temporary variable to test redirects based on whether user is logged in or not

# Pernament variables
users = User.query.all()
items = Item.query.all()

@myapp_obj.route("/")
@myapp_obj.route("/home")
def home():
	return render_template("home.html", login_status=login_status)

@myapp_obj.route("/featured")
def featured():
	return render_template("featured.html", login_status=login_status)

@myapp_obj.route("/purchase")
def purchase():
        return render_template("purchase.html", users=users, items=items, login_status=login_status)

@myapp_obj.route("/purchase/<id>")
def purchaseItem(id=0):
        return render_template("purchaseItem.html", users=users, login_status=login_status, item=items[int(id)-1])
def addToCart(id=0):

        item = Item.query.filter(Item.id == id)
        cart_item = CartItem(item=item)
        db.session.add(cart_item)
        db.session.commit()

        return render_template("purchaseItem.html", users=users, login_status=login_status, item=items[int(id)-1])

@myapp_obj.route("/purchase/buynow/<id>")
def buyNow(id=0):
        return render_template("buyNow.html", users=users, login_status=login_status, item=items[int(id)-1])

@myapp_obj.route("/signin")
def signin():
	return render_template("signin.html", login_status=login_status)

@myapp_obj.route("/register")
def register():
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
