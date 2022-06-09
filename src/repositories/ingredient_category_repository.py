
from db import db as default_db
from entities.ingredient_category import IngredientCategory

class IngredientCategoryRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_ingredient_category(self, category_name):
        try:
            sql = "INSERT INTO IngredientCategory (category_name) \
                        VALUES (:category_name)"
            self._db.session.execute(sql, {"category_name":category_name})
            self._db.session.commit()
            print("onnistui")
        except:
            print("ei onnistunut")
            return False

    def check_if_category_exists(self, category_name):
        sql = "SELECT category_name \
                FROM IngredientCategory \
                WHERE category_name =:category_name"
        query_result = self._db.session.execute(sql, {"category_name":category_name})
        if not query_result:
            return False
        return True

    def get_all_categories(self):
        sql = "SELECT * FROM IngredientCategory"
        query_result = self._db.session.execute(sql).fetchall()
        return self.create_categories_from_results(query_result)

    def create_category_from_result(self, result_row: IngredientCategory):
        if not result_row:
            return None
        return IngredientCategory(
            category_id=result_row[0],
            category_name=result_row[1]
        )

    def create_categories_from_results(self, result_rows):
        names = []
        for row in result_rows:
            names.append(self.create_category_from_result(row))
        return names

    def delete_category(self, id):
        try:
            sql = "DELETE FROM IngredientCategory WHERE id:=id"
            self._db.session.execute(sql, {"id":id})
            self._db.session.commit()
        except:
            return False

ingredient_category_repository = IngredientCategoryRepository()