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
    # main course to the database
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
    # edit mains to the database
    if request.method == "POST":
        edited_starter = {
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)