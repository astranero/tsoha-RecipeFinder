from db import (db as default_db)
from entities.ingredient import Ingredient

class IngredientRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_ingredient(self, ingredient_name):
        try:
            sql = "INSERT INTO Ingredients (ingredient_name) VALUES (:ingredient_name)"
            self._db.session.execute(sql, Ingredient(ingredient_name=ingredient_name))
            self._db.session.commit()
        except:
            return False

    def check_if_ingredient_exists(self, ingredient_name):
        sql = "SELECT ingredient_name FROM Ingredients WHERE ingredient_name =:ingredient_name"
        query_result = self._db.session.execute(sql, ingredient_name)
        if not query_result:
            return False
        return True

    def get_all_ingredients_in_category(self, category_name):
        try:
            sql = "SELECT ingredient_name FROM Ingredient, IngredientCategory \
                    WHERE Ingredient.category_id = IngredientCategory.id \
                        AND Ingredient.category_name=:category_name"
            query_result = self._db.session.execute(sql, category_name).fetchall()
            return self.create_ingredients_from_results(query_result)
        except:
            return False

    def create_ingredient_from_result(self, result_row):
        return Ingredient(ingredient_name=result_row[0])

    def create_ingredients_from_results(self, result_row):
        ingredients = []
        for row in result_row:
            ingredients.append(self.create_ingredient_from_result(row))
        return ingredients

ingredient_repository = IngredientRepository()