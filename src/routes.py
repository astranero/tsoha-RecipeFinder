from app import app
from flask import render_template, request, redirect, url_for
from services.user_service import user_service
from services.recipe_service import recipe_service
from services.favorites_service import favorite_service

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
        user_role = request.form["role"]
        phone_number = request.form["phone"]
        email = request.form["email"]
        user_service.register_user(username, password1, user_role, phone_number, email)
        return redirect("/homepage")
    return render_template("signup.html")

@app.route("/homepage", methods=["GET","POST"])
def homepage():
    recipe_all = recipe_service.get_recipe()
    return render_template("homepage.html", recipe_all=recipe_all)


@app.route("/profile/<int:id>", methods=["GET","POST"])
def profile(id):
    username = user_service.get_current_username(id)
    email = user_service.get_current_email(id)
    phone_number = user_service.get_current_phone_number(id)
    role = user_service.get_current_role(id)
    if request.method == "GET":
        return render_template("profile.html", username=username, email=email, role=role, phone_number=phone_number, id=id)

@app.route("/profile/<int:id>/modify-username", methods=["GET", "POST"])
def modify_username(id):
    new_username = request.form["new_username"]
    user_service.modify_username(new_username, id)
    return redirect('/profile/'+str(id))

@app.route("/profile/<int:id>/modify-phone-number", methods=["GET", "POST"])
def modify_phone_number(id):
    new_phone_number = request.form["new_phone_number"]
    user_service.modify_phone_number(new_phone_number, id)
    return redirect('/profile/'+str(id))

@app.route("/profile/<int:id>/modify-email", methods=["GET", "POST"])
def modify_email(id):
    new_email = request.form["new_email"]
    user_service.modify_email(new_email, id)
    return redirect('/profile/'+str(id))

@app.route("/favorites", methods=["GET","POST"])
def favorites():
    favorites = favorite_service.get_user_favorites(user_service.get_user_id())
    return render_template("favorites.html", favorites=favorites)

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
        ingredient = request.form["ingredient"]
        recipe_service.add_ingredient_to_recipe(ingredient, recipe_id)
        return redirect("/manage-recipes")
    return render_template("manage_recipes.html")

@app.route("/manage-recipes/delete-recipe", methods=["GET","POST"])
def delete_recipe():
    delete_recipe = request.form["recipe_id"]
    recipe_service.delete_recipe(delete_recipe)
    return redirect("/manage-recipes")

@app.route("/recipe/<int:id>", methods=["GET","POST"])
def recipe(id):
    recipe = recipe_service.get_recipe_with_id(str(id))
    if request.method == "GET":
        return render_template("recipe.html", recipe=recipe, id=id)
    if request.method == "POST":
        favorite = request.form["favorite"]
        if favorite:
            favorite_service.add_to_favorites(id, user_service.get_user_id())
        return render_template("recipe.html", recipe=recipe, id=id)



