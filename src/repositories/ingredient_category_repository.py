
from db import db as default_db
from entities.ingredient_category import IngredientCategory

class IngredientCategoryRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_ingredient_category(self, category_name):
       
        sql = "INSERT INTO IngredientCategory (category_name) \
                        VALUES (:category_name)"
        self._db.session.execute(sql, {"category_name":category_name})
        self._db.session.commit()
        print("onnistui")
       
    def check_if_category_exists(self, category_name):
        sql = "SELECT category_name \
                FROM IngredientCategory \
                WHERE category_name =:category_name"
        query_result = self._db.session.execute(sql, {"category_name":category_name})
        if not query_result:
            return False
        return True

    def get_all_categories(self):
        sql = "SELECT id, category_name FROM IngredientCategory"
        query_result = self._db.session.execute(sql).fetchall()
        return query_result

    def get_all_ingredients_in_category(self, category_id):
        sql = "SELECT Ingredients.category_id, IngredientCategory.category_name, Ingredients.ingredient_name \
                    FROM Ingredients LEFT JOIN IngredientCategory ON \
                    Ingredients.category_id = IngredientCategory.id \
                    WHERE Ingredients.category_id =:category_id"
        return self._db.session.execute(sql, {"category_id":category_id}).fetchall()

    def delete_category(self, id):
        sql = "DELETE FROM IngredientCategory WHERE id=:id"
        self._db.session.execute(sql, {"id":id})
        self._db.session.commit()
       
ingredient_category_repository = IngredientCategoryRepository()