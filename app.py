from flask import Flask
from sqlalchemy.sql import text
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    result = db.session.execute(text("SELECT group_name FROM Activitygroups"))
    groups = result.fetchall()
    return render_template("index.html", count=len(groups), groups=groups)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = "INSERT INTO Activitygroups (group_name, location, theme) VALUES (:content)"
    db.session.execute(text(sql), {"group_name":content})
    db.session.commit()
    return redirect("/")
    
@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
    
    





