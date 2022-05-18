# VANILUXE 
- Kyo Lee (@DetectiPhoenix), Team Lead
- Maryia Sakharava (@maryiasakharava)
- George Dominise (@GeorgeDominise)
- Rohan Maheshwari (@rmhsh8)
- Jaskaran Singh (@jazSingh5) 

# Introduction
Welcome to VANILUXE! The newest shopping website for all of your luxurious needs. You can trust us to not scam you. Jokes aside, this project is run by a group of five students just trying to learn how to work together.

# How To Run The Project
To run the project navigate into the project directory and run "python3 run.py" command. Once the command executes, you need to copy the address of the website, and paste it into you browser.

# How To Use The Website
- UI is interactive. "Settings" and "Log Out" can be found in the dropdown menu below "Account" (assuming you have logged in).
- In order to sell an item (currently), use ipython3 and follow these steps: 
-    from app import db
-    from app.models import User, Item
-    // If already created user, find user with User.query.all(). If not, create user using Register button.
-    i = Item(name="name", price=0, description="description", image_url="image url", author=user)
-    db.session.add(i)
-    db.session.commit()

# Libraries Needed To Run The Project
- flask
- flask-login
- flask-msearch
- flask-wtf

# Responsibilities
Kyo Lee
- Buy Item
- Sell Item
- Add Pictures to Item
- Splash page
- Search Items

Maryia Sakharava
- Sign In
- Sign Out
- Add Items to Cart (NOT COMPLETE)

George Dominise
- See all Seller's Items
- Contact Form
- Reviews Form

Rohan Maheshwari
- Create Account
- Delete Account
- Wishlist

Jaskaran Singh
- User settings
