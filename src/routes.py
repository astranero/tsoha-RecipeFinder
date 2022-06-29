from app import app
from flask import render_template, request, redirect, url_for, flash, session
from services.user_service import user_service
from services.recipe_service import recipe_service
from services.favorites_service import favorite_service
from services.review_service import review_service

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
    if request.method == "GET":
        recipe_all = recipe_service.get_recipe_order_by_oldest()
        return render_template("homepage.html", recipe_all=recipe_all)
    if request.method == "POST":
        user_service.check_csrf()
        recipe_all = recipe_service.get_recipe_order_by_oldest()
        query = request.form.get("search")
        oldest = request.form.get("order_by_oldest")
        newest = request.form.get("order_by_newest")
        review = request.form.get("order_by_review")
        name = request.form.get("order_by_name")
        if oldest:
            recipe_all = recipe_service.get_recipe_order_by_oldest()
            return render_template("homepage.html", recipe_all=recipe_all)
        if newest:
            recipe_all = recipe_service.get_recipe_order_by_newest()
            return render_template("homepage.html", recipe_all=recipe_all)
        if review:
            recipe_all = recipe_service.get_recipe_order_by_review()
            return render_template("homepage.html", recipe_all=recipe_all)
        if name:
            recipe_all = recipe_service.get_recipe_order_by_name()
            return render_template("homepage.html", recipe_all=recipe_all)
        if query:
            search_title = recipe_service.search_by_name(query)
            return render_template("homepage.html", search_title=search_title)
        if query == '':
            return render_template("homepage.html", recipe_all=recipe_all)
        return render_template("homepage.html", recipe_all=recipe_all)

@app.route("/profile", methods=["GET","POST"])
def profile():
    user_id = user_service.get_user_id()
    username = user_service.get_current_username(user_id)
    email = user_service.get_current_email(user_id)
    phone_number = user_service.get_current_phone_number(user_id)
    role = user_service.get_current_role(user_id)
    if request.method == "GET":
        return render_template("profile.html", username=username, email=email, role=role, phone_number=phone_number, user_id=user_id)

@app.route("/profile/modify-username", methods=["POST"])
def modify_username():
    user_id = user_service.get_user_id()
    user_service.check_csrf()
    new_username = request.form["new_username"]
    user_service.modify_username(new_username, user_id)
    return redirect('/profile')

@app.route("/profile/modify-phone-number", methods=["POST"])
def modify_phone_number():
    user_id = user_service.get_user_id()
    user_service.check_csrf()
    new_phone_number = request.form["new_phone_number"]
    user_service.modify_phone_number(new_phone_number, user_id)
    return redirect('/profile')

@app.route("/profile/modify-email", methods=["POST"])
def modify_email():
    user_id = user_service.get_user_id()
    user_service.check_csrf()
    new_email = request.form["new_email"]
    user_service.modify_email(new_email, user_id)
    return redirect('/profile')

@app.route("/favorites", methods=["GET","POST"])
def favorites():
    user_id = user_service.get_user_id()
    favorites = favorite_service.get_user_favorites(user_id)
    if len(favorites) == 0:
        no_recipes = True
    else:
        no_recipes = False
    return render_template("favorites.html", favorites=favorites, no_recipes=no_recipes)

@app.route("/favorites/remove-favorite", methods=["POST"])
def remove_favorite():
    user_service.check_csrf()
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
    user_service.require_role(1)
    if request.method == "GET":
        recipe_all = recipe_service.get_recipe_details()
        return render_template("manage_recipes.html", recipe_all=recipe_all)
    if request.method == "POST":
        user_service.check_csrf()
        query = request.form.get("search")
        if query:
            recipe_all = recipe_service.search_by_name(query)
            return render_template("manage_recipes.html", recipe_all=recipe_all)
        if query == '':
            recipe_all = recipe_service.get_recipe_details()
            return render_template("manage_recipes.html", recipe_all=recipe_all)
        recipe_name = request.form["recipe_name"]
        cook_time = request.form["cook_time"]
        description = request.form["description"]
        instructions = request.form["instructions"]
        recipe_service.create_recipe(recipe_name, description, cook_time, instructions)
        recipe_id = recipe_service.get_recipe_id(recipe_name)
        ingredients = request.form.getlist("ingredient")
        for item in ingredients:
            recipe_service.add_ingredient_to_recipe(item, recipe_id)
        return redirect("/manage-recipes")
    return render_template("manage_recipes.html", recipe_all=recipe_all)

@app.route("/manage-recipes/delete-recipe/<int:recipe_id>", methods=["GET","POST"])
def delete_recipe(recipe_id):
    user_service.require_role(1)
    user_service.check_csrf()
    recipe_service.delete_recipe(recipe_id)
    return redirect("/manage-recipes")

@app.route("/manage-recipes/modify-recipe/<int:recipe_id>", methods=["GET","POST"])
def modify_recipe(recipe_id):
    user_service.require_role(1)
    recipe = recipe_service.get_recipe_with_id(recipe_id)
    ingredients = recipe_service.get_recipe_ingredients_with_id(recipe_id)
    if request.method == "POST":
        user_service.check_csrf()
        recipe_name = request.form["edited_recipe_name"]
        cook_time = request.form["edited_cook_time"]
        description = request.form["edited_description"]
        instructions = request.form["edited_instructions"]
        recipe_service.modify_recipe(recipe_id, recipe_name, cook_time, description, instructions)
        edited_ingredients = request.form.getlist("edited_ingredient")
        new_ingredients = request.form.getlist("new_ingredient")
        for item in edited_ingredients:
            recipe_service.modify_ingredients(recipe_id, item)
        for item in new_ingredients:
            recipe_service.add_ingredient_to_recipe(item, recipe_id)
        return redirect("/manage-recipes")
    return render_template("modify_recipe.html", recipe=recipe, ingredients=ingredients)

@app.route("/recipe/<int:recipe_id>", methods=["GET","POST"])
def recipe(recipe_id):
    recipe = recipe_service.get_recipe_with_id(str(recipe_id))
    ingredients = recipe_service.get_recipe_ingredients_with_id(recipe_id)
    average = review_service.get_average_for_reviews(recipe_id)
    reviews_all = review_service.get_recipe_reviews(recipe_id)
    user_id = user_service.get_user_id()
    review_done = review_service.check_if_user_already_reviewed_recipe(recipe_id, user_id)
    role = session.get('role')
    return render_template("recipe.html", recipe=recipe, ingredients=ingredients, recipe_id=recipe_id, average=average, reviews_all=reviews_all, role=role, review_done=review_done)

@app.route("/recipe/<int:recipe_id>/add-to-favorites", methods=["GET","POST"])
def add_to_favorites(recipe_id):
    user_service.check_csrf()
    user_id = user_service.get_user_id()
    favorite_service.add_to_favorites(user_id, recipe_id)
    return redirect("/recipe/"+str(recipe_id))

@app.route("/recipe/<int:recipe_id>/add-review", methods=["POST"])
def add_review(recipe_id):
    user_service.require_role(0)
    user_service.check_csrf()
    user_id = user_service.get_user_id()
    review = int(request.form["grade"])
    comment = request.form["comment"]
    review_service.create_review(review, comment, user_id, recipe_id)
    return redirect("/recipe/"+str(recipe_id))
