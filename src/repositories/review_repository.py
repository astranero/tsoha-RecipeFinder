from db import db as default_db

class ReviewRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_review(self, rating, comment, user_id, recipe_id):
        try:
            values_to_db = {"rating": rating,
                            "comment": comment,
                            "user_id": user_id,
                            "recipe_id":recipe_id}
            sql = """INSERT INTO Review (rating, comment, recipe_id, user_id, sent_at)
                        VALUES (:rating, :comment, :recipe_id, :user_id, NOW())"""
            self._db.session.execute(sql, values_to_db)
            self._db.session.commit()
            return True
        except:
            return False

    def get_recipe_reviews(self, recipe_id):
        sql = """SELECT Review.rating, Review.comment, Review.sent_at, Users.username
                    FROM Review
                    LEFT JOIN Users ON Users.id = Review.user_id
                    WHERE Review.recipe_id=:recipe_id
                    """
        return self._db.session.execute(sql, {"recipe_id":recipe_id}).fetchall()

    def get_average_for_reviews(self, recipe_id):
        try:
            sql = """SELECT ROUND(COALESCE(AVG(rating), 0), 1)
                    FROM Review
                    WHERE recipe_id=:recipe_id"""
            return self._db.session.execute(sql, {"recipe_id":recipe_id}).fetchone()[0]
        except:
            return False

    def check_if_user_already_reviewed_recipe(self, recipe_id, user_id):
        sql = """SELECT user_id, recipe_id
                FROM Review
                WHERE recipe_id=:recipe_id
                        AND user_id=:user_id"""
        return bool(self._db.session.execute(sql,
                        {"recipe_id":recipe_id, "user_id": user_id}).fetchall())

review_repository = ReviewRepository()