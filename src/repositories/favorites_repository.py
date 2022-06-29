from db import db as default_db

class FavoritesRepository:
    def __init__(self, db=default_db):
        self._db = db

    def add_to_favorites(self, user_id, recipe_id):
        try:
            sql = """INSERT INTO Favorites (user_id, recipe_id)
                        VALUES (:user_id, :recipe_id)"""
            self._db.session.execute(sql,
                {"user_id": user_id, "recipe_id": recipe_id})
            self._db.session.commit()
        except:
            return False


    def remove_from_favorites(self, user_id, recipe_id):
        try:
            sql = """DELETE FROM Favorites
                    WHERE user_id=:user_id
                        AND recipe_id=:recipe_id"""
            self._db.session.execute(sql,
                {"user_id": user_id, "recipe_id": recipe_id})
            self._db.session.commit()
        except:
            return False

    def get_user_favorites(self, user_id):
        sql = """SELECT Recipes.id, Recipes.recipe_name,
                    Recipes.cook_time, Recipes.description
                        FROM Recipes
                        LEFT JOIN Favorites ON
                        Recipes.id = Favorites.recipe_id
                        WHERE Favorites.user_id=:user_id"""
        return self._db.session.execute(sql, {"user_id":user_id}).fetchall()

    def check_if_favorite(self, user_id, recipe_id):
        sql = """SELECT user_id, recipe_id
                FROM Favorites
                WHERE user_id=:user_id
                    AND recipe_id=:recipe_id"""
        return bool(self._db.session.execute(sql,
                    {"user_id": user_id, "recipe_id": recipe_id}).fetchall())

favorites_repository = FavoritesRepository()