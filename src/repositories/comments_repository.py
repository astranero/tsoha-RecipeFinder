from db import db as default_db

class CommentsRepository:
    def __init__(self, db=default_db):
        self._db = db

    def add_comment(self, comment, user_id, recipe_id):
        try:
            values_to_db = {"comment":comment,
                            "user_id":user_id,
                            "recipe_id": recipe_id}
            sql = "INSERT INTO Comments (comment, user_id, recipe_id, sent_at) \
                        VALUES (:comment, :user_id, :recipe_id, NOW())"
            self._db.session.execute(sql, values_to_db)
            self._db.session.commit()
        except:
            return False

    def delete_comment(self, recipe_id):
        sql = "DELETE FROM Comments WHERE id=:id"
        self._db.session.execute(sql, {"id":recipe_id})
        self._db.session.commit()

    def get_comments(self, recipe_id):
        sql = "SELECT Comments.comment, Users.username, Comments.sent_at \
                FROM Comments, Users, Recipes \
                WHERE Comments.user_id=Users.id \
                    AND Comments.recipe_id = Recipes.recipe_id \
                    AND Recipes.recipe_id :=recipe_id \
                    ORDER BY Comments.id"
        return self._db.session.execute(sql, {"recipe_id":recipe_id}).fetchall()


comments_repository = CommentsRepository()