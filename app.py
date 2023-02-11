import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    # home page
    return render_template("home.html")


@app.route("/cuisine")
def cuisine():
    # render cuisine as home page
    return render_template("cuisine.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("cuisine.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/starters")
def starters():
    starters = mongo.db.starter.find()
    return render_template("starters.html", starters=starters)


@app.route("/add_starters", methods=["GET", "POST"])
def add_starters():
    # add starters in the database
    if request.method == "POST":
        starter = {
            "starter_names": request.form.get("starter_names"),
            "starter_tools": request.form.get("starter_tools"),
            "starter_description": request.form.get("starter_description"),
            "starter_ingredients": request.form.get("starter_ingredients"),
            "starter_directions": request.form.get("starter_directions"),
            "created_by": session["user"]
            }
        mongo.db.starter.insert_one(starter)
        return redirect(url_for("starters"))

    return render_template("add_starters.html")


@app.route("/edit_starters/<starter_id>",  methods=["GET", "POST"])
def edit_starters(starter_id):
    # edit starters in the database
    if request.method == "POST":
        edited_starter = {
            "starter_names": request.form.get("starter_names"),
            "starter_tools": request.form.get("starter_tools"),
            "starter_description": request.form.get("starter_description"),
            "starter_ingredients": request.form.get("starter_ingredients"),
            "starter_directions": request.form.get("starter_directions"),
            "created_by": session["user"]
            }
        mongo.db.starter.update({"_id": ObjectId(starter_id)}, edited_starter)
        flash("Starter Successfully Updated")

    starter = mongo.db.starter.find_one({"_id": ObjectId(starter_id)})
    return render_template("edit_starters.html", starter=starter)


@app.route("/delete_starters/<starter_id>")
def delete_starters(starter_id):
    # delete starters from the database
    mongo.db.starter.remove({"_id": ObjectId(starter_id)})
    flash("starter Successfully Deleted")
    return redirect(url_for("starters"))


@app.route("/mains")
def mains():
    # main course 
    mains = mongo.db.main.find()
    return render_template("mains.html", mains=mains)


@app.route("/add_mains", methods=["GET", "POST"])
def add_mains():
    # add main course to the database
    if request.method == "POST":
        main = {
            "main_names": request.form.get("main_names"),
            "main_tools": request.form.get("main_tools"),
            "main_description": request.form.get("main_description"),
            "main_ingredients": request.form.get("main_ingredients"),
            "main_directions": request.form.get("main_directions"),
            "created_by": session["user"]
            }
        mongo.db.main.insert_one(main)
        return redirect(url_for("mains"))

    return render_template("add_mains.html")


@app.route("/edit_mains/<main_id>",  methods=["GET", "POST"])
def edit_mains(main_id):
    # edit mains in the database
    if request.method == "POST":
        edited_main = {
            "main_names": request.form.get("main_names"),
            "main_tools": request.form.get("main_tools"),
            "main_description": request.form.get("main_description"),
            "main_ingredients": request.form.get("main_ingredients"),
            "main_directions": request.form.get("main_directions"),
            "created_by": session["user"]
            }
        mongo.db.main.update({"_id": ObjectId(main_id)}, edited_main)
        flash("Main Courses Successfully Updated")

    main = mongo.db.main.find_one({"_id": ObjectId(main_id)})
    return render_template("edit_mains.html", main=main)


@app.route("/delete_mains/<main_id>")
def delete_mains(main_id):
    # delete mains from the database
    mongo.db.main.remove({"_id": ObjectId(main_id)})
    flash("Main course Successfully Deleted")
    return redirect(url_for("mains"))


@app.route("/desserts")
def desserts():
    # Desserts 
    desserts = mongo.db.dessert.find()
    return render_template("desserts.html", desserts=desserts)


@app.route("/add_desserts", methods=["GET", "POST"])
def add_desserts():
    # add desserts to the database
    if request.method == "POST":
        dessert = {
            "dessert_names": request.form.get("dessert_names"),
            "dessert_tools": request.form.get("dessert_tools"),
            "dessert_description": request.form.get("dessert_description"),
            "dessert_ingredients": request.form.get("dessert_ingredients"),
            "dessert_directions": request.form.get("dessert_directions"),
            "created_by": session["user"]
            }
        mongo.db.dessert.insert_one(dessert)
        return redirect(url_for("desserts"))

    return render_template("add_desserts.html")


@app.route("/edit_desserts/<dessert_id>",  methods=["GET", "POST"])
def edit_desserts(dessert_id):
    # edit desserts in the database
    if request.method == "POST":
        edited_dessert = {
            "dessert_names": request.form.get("dessert_names"),
            "dessert_tools": request.form.get("dessert_tools"),
            "dessert_description": request.form.get("dessert_description"),
            "dessert_ingredients": request.form.get("dessert_ingredients"),
            "dessert_directions": request.form.get("dessert_directions"),
            "created_by": session["user"]
            }
        mongo.db.dessert.update({"_id": ObjectId(dessert_id)}, edited_dessert)
        flash("Desserts Successfully Updated")

    dessert = mongo.db.dessert.find_one({"_id": ObjectId(dessert_id)})
    return render_template("edit_desserts.html", dessert=dessert)


@app.route("/delete_desserts/<dessert_id>")
def delete_desserts(dessert_id):
    # delete desserts from the database
    mongo.db.dessert.remove({"_id": ObjectId(dessert_id)})
    flash("Desserts Successfully Deleted")
    return redirect(url_for("desserts"))




    


@app.route("/drinks")
def drinks():
    # drinks 
    drinks = mongo.db.drink.find()
    return render_template("drinks.html", drinks=drinks)


@app.route("/add_drinks", methods=["GET", "POST"])
def add_drinks():
    # add drinks to the database
    if request.method == "POST":
        drink = {
            "drink_names": request.form.get("drink_names"),
            "drink_tools": request.form.get("drink_tools"),
            "drink_description": request.form.get("drink_description"),
            "drink_ingredients": request.form.get("drink_ingredients"),
            "drink_directions": request.form.get("drink_directions"),
            "created_by": session["user"]
            }
        mongo.db.drink.insert_one(drink)
        return redirect(url_for("drinks"))

    return render_template("add_drinks.html")


@app.route("/edit_drinks/<drink_id>",  methods=["GET", "POST"])
def edit_drinks(drink_id):
    # edit desserts in the database
    if request.method == "POST":
        edited_drink = {
            "drink_names": request.form.get("drink_names"),
            "drink_tools": request.form.get("drink_tools"),
            "drink_description": request.form.get("drink_description"),
            "drink_ingredients": request.form.get("drink_ingredients"),
            "drink_directions": request.form.get("drink_directions"),
            "created_by": session["user"]
            }
        mongo.db.drink.update({"_id": ObjectId(drink_id)}, edited_drink)
        flash("Drinks Successfully Updated")

    drink = mongo.db.drink.find_one({"_id": ObjectId(drink_id)})
    return render_template("edit_drinks.html", drink=drink)


@app.route("/delete_drinks/<drink_id>")
def delete_drinks(drink_id):
    # delete drink from the database
    mongo.db.drink.remove({"_id": ObjectId(drink_id)})
    flash("Drink Successfully Deleted")
    return redirect(url_for("drinks"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)