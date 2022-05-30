from db import (db as default_db)

class RecipeIngredientsRepository:
    def __init__(self, db=default_db):
        self._db = db

    def add_ingredient_to_recipe(self, recipe_id, ingredient_id):
        try:
            sql = "INSERT INTO RecipeIngredients (recipe_id, ingredient_id) \
                    VALUES (:recipe_id, :ingredient_id)"
            self._db.session.execute(sql, (recipe_id, ingredient_id))
            self._db.session.commit()
        except:
            return False

    def check_if_ingredient_added_to_recipe(self, recipe_id, ingredient_id):
        sql = "SELECT * \
                FROM RecipeIngredients \
                WHERE recipe_id=:tip_id \
                    AND ingredient_id=:ingredient_id"
        query_result = self._db.session.execute(sql, (recipe_id, ingredient_id)).fetchone()
        if not query_result:
            return False
        return True

    def get_all_recipes_with_ingredient_id(self, ingredient_id):
        try:
            ingredient_sql = "SELECT ingredient_name \
                                FROM RecipeIngredients \
                                WHERE ingredient_id=:ingredient_id"
            query_result = self._db.session.execute(ingredient_sql, ingredient_id).fetchall()

            recipes = []
            for pair in query_result:
                recipe_id, ingredient_id = pair
                recipe_sql = "SELECT recipe_name \
                                FROM Recipes \
                                WHERE recipe_id=:recipe_id"
                recipes = self._db.session.execute(recipe_sql, recipe_id)
                recipes.append(recipes).fetchone()
            return recipes
        except:
            return False

    def get_all_ingredients_with_recipe_id(self, recipe_id):
        try:
            recipe_sql = "SELECT recipe_name \
                            FROM Recipes \
                            WHERE recipe_id=:recipe_id"
            query_result = self._db.session.execute(recipe_sql, recipe_id).fetchall()

            ingredients = []
            for pair in query_result:
                recipe_id, ingredient_id = pair
                ingredient_sql = "SELECT ingredient_name \
                                    FROM RecipeIngredients \
                                    WHERE ingredient_id=:ingredient_id"
                ingredients = self._db.session.execute(ingredient_sql, ingredient_id).fetchone()
                ingredients.append(ingredients).fetchone()
            return ingredients
        except:
            return False

recipe_ingredients_repository = RecipeIngredientsRepository()