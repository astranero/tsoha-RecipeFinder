from db import (db as default_db)

class IngredientRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_ingredient(self, ingredient_name, category_id):
        values_to_db = {"ingredient_name":ingredient_name,
                        "category_id":category_id}
        sql = "INSERT INTO Ingredients (ingredient_name, category_id) \
                    VALUES (:ingredient_name, :category_id)"
        self._db.session.execute(sql, values_to_db)
        self._db.session.commit()

    def check_if_ingredient_exists(self, ingredient_name):
        sql = "SELECT ingredient_name \
                FROM Ingredients \
                WHERE ingredient_name=:ingredient_name"
        query_result = self._db.session.execute(sql, ingredient_name)
        if not query_result:
            return False
        return True

    def get_all_ingredients(self):
        sql = "SELECT id, ingredient_name, category_id FROM Ingredients"
        query_result = self._db.session.execute(sql).fetchall()
        return query_result

    def get_all_ingredients_with_categories(self):
        sql = "SELECT Ingredients.ingredient_name, IngredientCategory.category_name \
                    FROM Ingredients LEFT JOIN IngredientCategory ON \
                    Ingredients.category_id = IngredientCategory.id"
        return self._db.session.execute(sql).fetchall()

ingredient_repository = IngredientRepository()