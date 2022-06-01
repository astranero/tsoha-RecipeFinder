from db import db as default_db

class BasketRepository:
    def __init__(self, db=default_db):
        self._db = db

    def add_to_basket(self, user_id, ingredient_id):
        try:
            sql = "INSERT INTO Basket (user_id, ingredient_id) \
                    VALUES (:user_id, :ingredient_id)"
            self._db.session.execute(sql, (user_id, ingredient_id))
            self._db.session.commit()
        except:
            return False

    def remove_ingredient_from_basket(self, user_id, ingredient_id):
        try:
            sql = "DELETE FROM basket \
                    WHERE user_id=:user_id \
                        AND ingredient_id=:ingredient_id"
            self._db.session.execute(sql, (user_id, ingredient_id))
        except:
            return False

    def get_basket_with_user_id(self, user_id):
        try:
            sql = "SELECT ingredient_name \
                                FROM Basket, Ingredients, Users \
                                WHERE Basket.user_id=Users.id \
                                    AND Basket.ingredient_id=Ingredients.ingredient_id \
                                    AND Basket.user_id =: user_id"
            return self._db.session.execute(sql, user_id).fetchall()

        except:
            return False

    def check_if_ingredient_exists_in_basket(self):
        pass

basket_repository = BasketRepository()