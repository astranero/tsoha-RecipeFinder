from app import app
from flask import render_template, request, redirect, flash
from services.user_service import user_service

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user_service.login_user(username, password):
            return redirect("/homepage", username, password)
        return redirect("/")

@app.route("/signup", methods=["GET","POST"])
def signup():
    return render_template("signup.html")

@app.route("/homepage", methods=["GET","POST"])
def homepage():
    if request.method == "GET":
        return render_template("homepage.html")

