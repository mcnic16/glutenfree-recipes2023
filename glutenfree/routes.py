from flask import render_template
from glutenfree import app, db
from glutenfree.models import Starter, Main, Dessert, Drink


@app.route("/")
def home():
    return render_template("base.html")