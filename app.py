from flask import Flask, render_template, request
from data import recipes, types

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"

@app.route("/", methods = ["GET", "POST"])
def home():
    new_id = len(recipes)
    if len(request.form) > 0:
        new_recipe = request.form['newRec']
        new_description = request.form['newDesc']
        recipes.update({new_id: new_recipe})
        types.update({new_id: new_description})
    return render_template("home.html", recipes = recipes, types = types)