from werkzeug.security import generate_password_hash
from db import db as default_db
from entities.user import User

class UserRepository:
    def __init__(self, db=default_db):
        self._db = db

    def login(self, username):
        try:
            sql = "SELECT id, password, role FROM users WHERE username=:username"
            return self._db.session.execute(sql, {"username":username}).fetchone()
        except:
            return False

    def signup_user(self, user_object: User):
        try:
            hash_value = generate_password_hash(user_object.password)
            values_to_db = {"username":user_object.username,
                            "password":hash_value,
                            "role":user_object.role,
                            "phone_number":user_object.phone_number,
                            "email":user_object.email}

            sql = "INSERT INTO users (username, password, role, phone_number, email) \
                    VALUES (:username, :password, :role, :phone_number, :email)"
            self._db.session.execute(sql, values_to_db)
            self._db.session.commit()
        except:
            return False

user_repository = UserRepository()
