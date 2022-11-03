from flask import Flask
from datetime import datetime
import re
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/table")
def gettable():
    return render_template("table.html")
    #if request.method == 'POST':return getqueried()


@app.route("/queried")
def getqueried():
    return render_template("queried.html")
        #data=app.send_static_file("data.json")
    