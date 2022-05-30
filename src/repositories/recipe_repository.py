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
        try:
            sql = "SELECT recipe_name, cook_time, instructions \
                    FROM Recipes \
                    WHERE id=:recipe_id"
            self._db.session.execute(sql, recipe_id).fetchall()
            self._db.session.commit()
        except:
            return False

    def modify_recipe(self, new_recipe_object: Recipe):
        values_to_db = {"recipe_id":new_recipe_object.recipe_id,
                        "recipe_name":new_recipe_object.recipe_name,
                        "cook_time":new_recipe_object.cook_time,
                        "instructions":new_recipe_object.instructions}

        try:
            sql ="UPDATE Recipe SET \
                    recipe_name=:recipe_name, cook_time=:cook_time, instructions=:instructions \
                    WHERE recipe_id=:recipe_id"
            self._db.session.execute(sql, values_to_db)

            self._db.connection.commit()
        except:
            return False
        return True

    def delete_recipe(self, recipe_id):
        try:
            sql = "DELETE FROM Recipe WHERE id=:recipe_id"
            self._db.session.execute(sql, recipe_id)
        except:
            return False

    def search_by_title(self, query):
        min_ratio = 80
        results = []
        for recipe in self.get_all_recipes():
            if fuzz.WRatio(query, recipe) >= min_ratio:
                results.append(recipe)
        return results

recipe_repository = RecipeRepository()