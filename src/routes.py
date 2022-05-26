from app import app
from flask import render_template, request, redirect, flash
from services.user_service import user_service

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        if not user_service.login_user(username, password):
            print('fail')
            return render_template("login.html")
        print('ok')
        return redirect("/homepage")
    return render_template("login.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if password1 != password2:
            return redirect("/signup")
        role = request.form["role"]
        phone_number = request.form["phone"]
        email = request.form["email"]
        print(username, password1, password2, role, phone_number, email)
        if not user_service.register_user(username, password1, role, phone_number, email):
            print('fail')
            return redirect("/signup")
        return redirect("/homepage")
    return render_template("signup.html")

@app.route("/homepage", methods=["GET","POST"])
def homepage():
    return render_template("homepage.html")

