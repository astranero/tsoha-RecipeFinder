
from entities.ingredient_category import IngredientCategory
from db import db as default_db

class IngredientCategoryRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_ingredient_category(self, category_name):
        try:
            sql = "INSERT INTO IngredientCategory (category_name) VALUES (:category_name)"
            self._db.session.execute(sql, category_name)
            self._db.session.commit()
        except:
            return False

    def get_all_categories(self):
        try:
            sql = "SELECT category_name FROM IngredientCategory"
            query_result = self._db.session.execute(sql).fetchall()
            return self.create_categories_from_results(query_result)
        except:
            return False

    def create_categories_from_result(self, result_row):
        return IngredientCategory(category_name=result_row[0])

    def create_categories_from_results(self, result_row):
        categories = []
        for row in result_row:
            categories.append(self.create_categories_from_result(row))
        return categories

ingredient_category_repository = IngredientCategoryRepository()