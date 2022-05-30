
from db import db as default_db

class IngredientCategoryRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_ingredient_category(self, category_name):
        try:
            sql = "INSERT INTO IngredientCategory (category_name) \
                    VALUES (:category_name)"
            self._db.session.execute(sql, category_name)
            self._db.session.commit()
        except:
            return False

    def get_all_categories(self):
        try:
            sql = "SELECT category_name \
                    FROM IngredientCategory"
            self._db.session.execute(sql).fetchall()
        except:
            return False

ingredient_category_repository = IngredientCategoryRepository()