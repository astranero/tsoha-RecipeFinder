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
        print("jee onnistui")

    def check_if_ingredient_exists(self, ingredient_name):
        sql = "SELECT ingredient_name \
                FROM Ingredients \
                WHERE ingredient_name=:ingredient_name"
        query_result = self._db.session.execute(sql, ingredient_name)
        if not query_result:
            return False
        return True

    def get_all_ingredients_with_categories(self, category_id):
        try:
            sql = "SELECT IngredientCategory.category_name, Ingredient.ingredient_name \
                    FROM Ingredient, IngredientCategory \
                    WHERE Ingredient.category_id = IngredientCategory.id \
                        AND Ingredient.category_id=:category_id"
            self._db.session.execute(sql, category_id).fetchall()
            print("onnistui")
        except:
            print("ei onnistunut")
            return False


ingredient_repository = IngredientRepository()