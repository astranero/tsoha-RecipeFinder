
from db import (db as default_db)

class RecipeRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_recipe(self, recipe_name, description, cook_time, instructions):
        try:
            values_to_db = {"recipe_name":recipe_name,
                            "description":description,
                            "cook_time": cook_time,
                            "instructions":instructions,
                            }
            sql = "INSERT INTO Recipes (recipe_name, description, cook_time, instructions) \
                        VALUES (:recipe_name, :description, :cook_time, :instructions)"
            self._db.session.execute(sql, values_to_db)
            self._db.session.commit()
            return True
        except:
            return False

    def check_if_recipe_name_exist(self, recipe_name):
        return bool(self._db.session.execute("SELECT recipe_name \
                                    FROM Recipes \
                                    WHERE recipe_name=:recipe_name",
                                    {"recipe_name":recipe_name}).fetchall())

    def get_recipe_id(self, recipe_name):
        try:
            return self._db.session.execute("SELECT id FROM Recipes \
                                            WHERE recipe_name=:recipe_name", \
                                            {"recipe_name":recipe_name}).fetchone()[0]
        except:
            return False

    def add_ingredient_to_recipe(self, ingredient_name, recipe_id):
        try:
            values_to_db = {"ingredient_name":ingredient_name,
                        "recipe_id":recipe_id}
            sql = "INSERT INTO Ingredients (ingredient_name, recipe_id) \
                        VALUES (:ingredient_name, :recipe_id)"
            self._db.session.execute(sql, values_to_db)
            self._db.session.commit()
            return True
        except:
            return False

    def check_if_ingredient_in_recipe(self, recipe_id):
        return bool(self._db.session.execute("SELECT ingredient_name \
                                    FROM Ingredients \
                                    WHERE recipe_id=:recipe_id",
                                    {"recipe_id":recipe_id}).fetchall())

    def get_recipe(self):
        try:
            sql = "SELECT Recipes.id, Recipes.recipe_name, Recipes.cook_time, \
                            Recipes.description, Recipes.instructions \
                            FROM Recipes"
            return self._db.session.execute(sql).fetchall()
        except:
            return False


    def get_recipe_with_id(self, recipe_id):
        try:
            sql = "SELECT Recipes.id, Recipes.recipe_name, Recipes.cook_time, \
                        Recipes.description, Recipes.instructions \
                        FROM Recipes \
                        WHERE Recipes.id=:recipe_id"
            return self._db.session.execute(sql, {"recipe_id":recipe_id}).fetchall()
        except:
            return False

    def get_recipe_ingredients(self, recipe_id):
        sql = "SELECT Ingredients.ingredient_name \
                        FROM Ingredients, Recipes \
                        WHERE Ingredients.recipe_id = Recipes.id \
                        AND Recipes.id=:recipe_id"
        return self._db.session.execute(sql, {"recipe_id":recipe_id}).fetchall()

    def delete_recipe(self, id):
        try:
            sql = "DELETE FROM Recipes WHERE id=:id"
            self._db.session.execute(sql, {"id":id})
            self._db.session.commit()
        except:
            return False

    def modify_recipe(self):
        pass


recipe_repository = RecipeRepository()