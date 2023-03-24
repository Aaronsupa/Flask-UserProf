from flask import Flask, render_template, request
from data import recipes, types, suggestions
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"

class SuggestionForm(FlaskForm):
    sugg = StringField("What would you like to see added to this page? ")
    sub = SubmitField("Submit")

@app.route("/", methods = ["GET", "POST"])
def home():
    new_id = len(recipes)
    if len(request.form) > 0:
        new_recipe = request.form['newRec']
        new_description = request.form['newDesc']
        recipes.update({new_id: new_recipe})
        types.update({new_id: new_description})
    return render_template("home.html", recipes = recipes, types = types)

@app.route('/content', methods = ["GET", "POST"])
def content():
    new_id = len(suggestions) + 1 
    my_form = SuggestionForm()
    if len(request.form) > 1:
        new_sugg = my_form.sugg.data
        suggestions.update({new_id: new_sugg})

    return render_template("content.html", my_form = my_form, suggestions = suggestions)