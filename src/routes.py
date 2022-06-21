from app import app
from flask import render_template, request, redirect, url_for, flash, session
from services.user_service import user_service
from services.recipe_service import recipe_service
from services.favorites_service import favorite_service

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not user_service.login_user(username, password):
            return render_template("login.html", error="Invalid credentials")
        return redirect("/homepage")
    return render_template("login.html", error=error)

@app.route("/signup", methods=["GET","POST"])
def signup():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        user_role = request.form["role"]
        phone_number = request.form["phone"]
        email = request.form["email"]
        if len(password1) < 8:
            return render_template("signup.html", error='Password is too short!')
        if password1 != password2:
            return render_template("signup.html", error='Passwords do not match!')
        if not user_service.register_user(username, password1, user_role, phone_number, email):
            return render_template("signup.html", error='Username is already taken')
        user_service.register_user(username, password1, user_role, phone_number, email)
        return redirect("/homepage")
    return render_template("signup.html", error=error)

@app.route("/homepage", methods=["GET","POST"])
def homepage():
    recipe_all = recipe_service.get_recipe()
    return render_template("homepage.html", recipe_all=recipe_all)


@app.route("/profile/<int:user_id>", methods=["GET","POST"])
def profile(user_id):
    username = user_service.get_current_username(user_id)
    email = user_service.get_current_email(user_id)
    phone_number = user_service.get_current_phone_number(user_id)
    role = user_service.get_current_role(user_id)
    if request.method == "GET":
        return render_template("profile.html", username=username, email=email, role=role, phone_number=phone_number, user_id=user_id)

@app.route("/profile/<int:user_id>/modify-username", methods=["GET", "POST"])
def modify_username(user_id):
    new_username = request.form["new_username"]
    user_service.modify_username(new_username, user_id)
    return redirect('/profile/'+str(user_id))

@app.route("/profile/<int:user_id>/modify-phone-number", methods=["GET", "POST"])
def modify_phone_number(user_id):
    new_phone_number = request.form["new_phone_number"]
    user_service.modify_phone_number(new_phone_number, user_id)
    return redirect('/profile/'+str(user_id))

@app.route("/profile/<int:user_id>/modify-email", methods=["GET", "POST"])
def modify_email(user_id):
    new_email = request.form["new_email"]
    user_service.modify_email(new_email, user_id)
    return redirect('/profile/'+str(user_id))

@app.route("/favorites", methods=["GET","POST"])
def favorites():
    user_id = user_service.get_user_id()
    favorites = favorite_service.get_user_favorites(user_id)
    return render_template("favorites.html", favorites=favorites)

@app.route("/favorites/remove-favorite", methods=["GET","POST"])
def remove_favorite():
    user_id = user_service.get_user_id()
    recipe_id = request.form["recipe_id"]
    favorite_service.remove_from_favorites(user_id, recipe_id)
    return redirect("/favorites")

@app.route("/logout", methods=["GET","POST"])
def logout():
    user_service.logout()
    return redirect("/")

@app.route("/manage-recipes", methods=["GET","POST"])
def manage_recipes():
    if request.method == "GET":
        recipe_all = recipe_service.get_recipe()
        return render_template("manage_recipes.html", recipe_all=recipe_all)
    if request.method == "POST":
        recipe_name = request.form["recipe_name"]
        recipe_service.create_recipe_name_and_id(recipe_name)
        recipe_id = recipe_service.get_recipe_id(recipe_name)
        cook_time = request.form["cook_time"]
        description = request.form["description"]
        instructions = request.form["instructions"]
        recipe_service.add_details_to_recipe(description, cook_time, instructions, recipe_id)
        ingredients = request.form.getlist("ingredient")
        for item in ingredients:
            print(item)
            recipe_service.add_ingredient_to_recipe(item, recipe_id)
        return redirect("/manage-recipes")
    return render_template("manage_recipes.html")

@app.route("/manage-recipes/delete-recipe", methods=["GET","POST"])
def delete_recipe():
    delete_recipe = request.form["recipe_id"]
    recipe_service.delete_recipe(delete_recipe)
    return redirect("/manage-recipes")

@app.route("/recipe/<int:recipe_id>", methods=["GET","POST"])
def recipe(recipe_id):
    recipe = recipe_service.get_recipe_with_id(str(recipe_id))
    user_id = user_service.get_user_id()
    if request.method == "GET":
        return render_template("recipe.html", recipe=recipe, recipe_id=recipe_id)
    if request.method == "POST":
        favorite = request.form["favorite"]
        if favorite:
            favorite_service.add_to_favorites(user_id, recipe_id)
        return render_template("recipe.html", recipe=recipe, recipe_id=recipe_id)



