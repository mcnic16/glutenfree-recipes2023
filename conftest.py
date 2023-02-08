from app import add_starters
import pytest


@pytest.fixture
def add_starters():
    if request.method == "POST":
        starter = {
            "starter_names": request.form.get("starter_names"),
            "starter_tools": request.form.get("starter_tools"),
            "starter_description": request.form.get("starter_description"),
            "starter_ingredients": request.form.get("starter_ingredients"),
            "starter_directions": request.form.get("starter_directions"),
            }
        mongo.db.starter.insert_one(starter)
        return redirect(url_for("starters"))

    return render_template("add_starters.html", starters=starters)