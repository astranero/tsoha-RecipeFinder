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

    def remove_ingredient_from_recipe(self, ingredient_id, recipe_id):
        try:
            sql = "DELETE FROM RecipeIngredients (ingredient_id) \
                    WHERE ingredient_id=:ingredient_id \
                        AND recipe_id=:recipe_id"
            self._db.session.execute(sql, (ingredient_id, recipe_id))
        except:
            return False

    def check_if_ingredient_added_to_recipe(self, recipe_id, ingredient_id):
        sql = "SELECT * \
                FROM RecipeIngredients \
                WHERE recipe_id=:recipe_id \
                    AND ingredient_id=:ingredient_id"
        query_result = self._db.session.execute(sql, (recipe_id, ingredient_id)).fetchone()
        if not query_result:
            return False
        return True

    def get_all_ingredients_with_recipe_id(self, recipe_id):
        try:
            sql = "SELECT Ingredients.ingredient_name \
                    FROM Ingredients, RecipeIngredients, Recipes \
                        WHERE Ingredients.id=RecipeIngredients.ingredient_id \
                            AND Recipe.id=RecipeIngredients.recipe_id \
                            AND RecipeIngredients.recipe_id=:recipe_id"
            return self._db.session.execute(sql, recipe_id).fetchall()
        except:
            return False

recipe_ingredients_repository = RecipeIngredientsRepository()