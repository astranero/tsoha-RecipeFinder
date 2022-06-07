
from db import (db as default_db)
from entities.recipe import Recipe

class RecipeRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_recipe(self, recipe_object: Recipe):
        try:
            values_to_db = {"recipe_name":recipe_object.recipe_name,
                            "description":recipe_object.recipe_description,
                            "cook_time":recipe_object.cook_time,
                            "instructions": recipe_object.instructions}
            sql = "INSERT INTO Recipes (recipe_name, cook_time, instructions) \
                        VALUES (:recipe_name, :cook_time, :instructions)"
            self._db.session.execute(sql, values_to_db)
            self._db.session.commit()
        except:
            return False

    def get_all_recipes_with_ingredient_id(self, ingredient_id):
        try:
            sql = "SELECT Recipe.recipe_name, Recipe.description \
                    FROM Recipes, RecipeIngredients, Ingredients \
                    WHERE Recipe.id=RecipeIngredients.recipe_id \
                        AND Ingredients.id=RecipeIngredients.ingredient_id \
                        AND RecipeIngredients.ingredient_id=:ingredient_id"
            self._db.session.execute(sql, ingredient_id).fetchall()

        except:
            return False

    def get_recipe(self, recipe_id):
        try:
            sql = "SELECT * \
                    FROM Recipes \
                    WHERE id=:recipe_id"
            query = self._db.session.execute(sql, recipe_id).fetchone()

            self.create_recipe_from_result(query)
        except:
            return False

    def modify_recipe(self, new_recipe_object: Recipe):
        values_to_db = {"recipe_id":new_recipe_object.recipe_id,
                        "recipe_name":new_recipe_object.recipe_name,
                        "description":new_recipe_object.description,
                        "cook_time":new_recipe_object.cook_time,
                        "instructions":new_recipe_object.instructions}

        try:
            sql ="UPDATE Recipe SET \
                    recipe_name=:recipe_name, description=:description, \
                    cook_time=:cook_time, instructions=:instructions \
                    WHERE recipe_id=:recipe_id"
            self._db.session.execute(sql, values_to_db)

            self._db.session.commit()
        except:
            return False
        return True

    def delete_recipe(self, recipe_id):
        try:
            sql = "DELETE FROM Recipe WHERE id=:recipe_id"
            self._db.session.execute(sql, recipe_id)
        except:
            return False

    def create_recipe_from_result(self, result_row) -> Recipe:
        if not result_row:
            return None

        return Recipe(
            recipe_id=result_row[0],
            recipe_name=result_row[1],
            description=result_row[2],
            cook_time=result_row[3],
            instructions=result_row[4]
        )

recipe_repository = RecipeRepository()