from db import db as default_db

class FavoritesRepository:
    def __init__(self, db=default_db):
        self._db = db

    def add_to_favorites(self, user_id, recipe_id):
        try:
            sql = "INSERT INTO Favorites (user_id, recipe_id) \
                    VALUES (:user_id, :recipe_id)"
            self._db.session.execute(sql, (user_id, recipe_id))
            self._db.session.commit()
        except:
            return False

    def remove_from_favorites(self, user_id, recipe_id):
        try:
            sql = "DELETE FROM Favorites \
                    WHERE user_id=:user_id \
                        AND recipe_id=:recipe_id"
            self._db.session.execute(sql, (user_id, recipe_id))
        except:
            return False

    def get_all_favorites_with_user_id(self, user_id):
        try:
            user_favorite_sql = "SELECT * \
                                FROM Favorites \
                                WHERE user_id=:user_id"
            query_result = self._db.session.execute(user_favorite_sql, user_id).fetchall()

            favorites = []
            for pair in query_result:
                user_id, recipe_id = pair
                recipe_sql = "SELECT recipe_name \
                                FROM Recipes \
                                WHERE recipe_id=:recipe_id"
                recipe = self._db.session.execute(recipe_sql, recipe_id)
                favorites.append(recipe).fetchone()
            return favorites
        except:
            return False

favorites_repository = FavoritesRepository()