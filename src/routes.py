from app import app
from flask import render_template, request, redirect, flash
from services.user_service import user_service

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not user_service.login_user(username, password):
            return render_template("login.html")
        return redirect("/homepage")
    return render_template("login.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        role = request.form["role"]
        phone_number = request.form["phone"]
        email = request.form["email"]
        user_service.register_user(username, password1, role, phone_number, email)
        return redirect("/homepage")
    return render_template("signup.html")

@app.route("/homepage", methods=["GET","POST"])
def homepage():
    return render_template("homepage.html")

@app.route("/profile/<int:id>", methods=["GET","POST"])
def profile(id):
    username = user_service.get_current_username(id)
    email = user_service.get_current_email(id)
    phone_number = user_service.get_current_phone_number(id)
    print(username, email, phone_number)
    if request.method == "GET":
        return render_template("profile.html", username=username, email=email, phone_number=phone_number, id=id)

@app.route("/favourites", methods=["GET","POST"])
def favourites():
    return render_template("favourites.html")


@app.route("/logout", methods=["GET","POST"])
def logout():
    user_service.logout()
    return redirect("/")