from thefuzz import fuzz
from database import (db as default_db)
from entities.recipe import Recipe

class RecipeRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_recipe(self, recipe_object: Recipe):
        try:
            values_to_db = {"recipe_name":recipe_object.recipe_name,
                            "cook_time":recipe_object.cook_time,
                            "instructions": recipe_object.instructions}
            sql = "INSERT INTO Recipes (recipe_name, cook_time, instructions) \
                        VALUES (:recipe_name, :cook_time, :instructions)"
            self._db.session.execute(sql, values_to_db)
            self._db.session.commit()
        except:
            return False

    def get_all_recipes(self):
        try:
            sql = "SELECT recipe_name FROM Recipes"
            self._db.session.execute(sql)
            self._db.session.commit()
        except:
            return False

    def get_recipe(self, recipe_id):
        pass

    def modify_recipe(self):
        pass

    def delete_recipe(self):
        pass

    def create_recipe_from_result(self, result_row):
        pass

    def create_recipes_from_results(self, result_rows):
        pass

    def search_by_title(self, query):
        pass
recipe_repository = RecipeRepository()