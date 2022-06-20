
from db import (db as default_db)

class RecipeRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_recipe_name_and_id(self, recipe_name):
        try:
            values_to_db = {"recipe_name":recipe_name}
            sql = "INSERT INTO Recipes (recipe_name) \
                        VALUES (:recipe_name)"
            self._db.session.execute(sql, values_to_db)
            self._db.session.commit()
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

    def add_details_to_recipe(self, description, cook_time, instructions, recipe_id):
        values_to_db = {"description":description,
                            "cook_time": cook_time,
                            "instructions":instructions,
                            "recipe_id": recipe_id
                            }
        sql = "INSERT INTO RecipeDetails (description, cook_time, instructions, recipe_id) \
                    VALUES (:description, :cook_time, :instructions, :recipe_id)"
        self._db.session.execute(sql, values_to_db)
        self._db.session.commit()

    def add_ingredient_to_recipe(self, ingredient_name, recipe_id):
        values_to_db = {"ingredient_name":ingredient_name,
                        "recipe_id":recipe_id}
        sql = "INSERT INTO Ingredients (ingredient_name, recipe_id) \
                    VALUES (:ingredient_name, :recipe_id)"
        self._db.session.execute(sql, values_to_db)
        self._db.session.commit()

    def get_recipe(self):
        sql = "SELECT Recipes.id, Recipes.recipe_name, RecipeDetails.cook_time, \
                        RecipeDetails.description, RecipeDetails.instructions, Ingredients.ingredient_name \
                                FROM Recipes \
                                LEFT JOIN RecipeDetails ON \
                                Recipes.id = RecipeDetails.recipe_id \
                                LEFT JOIN Ingredients ON \
                                Recipes.id = Ingredients.recipe_id"
        return self._db.session.execute(sql).fetchall()

    def get_recipe_with_id(self, recipe_id):
        sql = "SELECT Recipes.id, Recipes.recipe_name, RecipeDetails.cook_time, \
                    RecipeDetails.description, RecipeDetails.instructions, Ingredients.ingredient_name \
                                        FROM Recipes \
                                        LEFT JOIN RecipeDetails ON \
                                        Recipes.id = RecipeDetails.recipe_id \
                                        LEFT JOIN Ingredients ON \
                                        Recipes.id = Ingredients.recipe_id \
                                        WHERE Recipes.id=:recipe_id"
        return self._db.session.execute(sql, {"recipe_id":recipe_id}).fetchall()

    def delete_recipe(self, id):
        sql = "DELETE FROM Recipes WHERE id=:id"
        self._db.session.execute(sql, {"id":id})
        self._db.session.commit()

    def modify_recipe(self):
        pass


recipe_repository = RecipeRepository()