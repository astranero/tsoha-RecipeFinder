from werkzeug.security import generate_password_hash
from db import db as default_db
from entities.user import User

class UserRepository:
    def __init__(self, db=default_db):
        self._db = db

    def login(self, username):
        try:
            sql = "SELECT username, id, password, role FROM users WHERE username=:username"
            return self._db.session.execute(sql, {"username":username}).fetchone()
        except:
            return False

    def register_user(self, user_object: User):
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

    def check_if_username_exists(self, username):
        return bool(self._db.session.execute("SELECT username \
                                    FROM users \
                                    WHERE username=:username",
                                    {"username":username}).fetchall())

    def check_if_email_exists(self, email):
        return bool(self._db.session.execute("SELECT email \
                                    FROM users \
                                    WHERE email=:email",
                                    {"email":email}).fetchall())

    def check_if_phone_number_exists(self, phone_number):
        return bool(self._db.session.execute("SELECT phone_number \
                                    FROM users \
                                    WHERE phone_number=:phone_number",
                                    {"phone_number":phone_number}).fetchall())

    def get_current_username(self, id):
        return self._db.session.execute("SELECT username FROM Users WHERE id=:id", \
                                        {"id":id}).fetchone()[0]
    def get_current_email(self, id):
        return self._db.session.execute("SELECT email FROM Users WHERE id=:id", \
                                        {"id":id}).fetchall()[0]

    def get_current_phone_number(self, id):
        return self._db.session.execute("SELECT phone_number FROM Users WHERE id=:id", \
                                        {"id":id}).fetchone()[0]

    def modify_user_details(self, new_user_object):
        values_to_db = {"user_id":new_user_object.user_id,
                        "username":new_user_object.username,
                        "password":new_user_object.password,
                        "phone_number":new_user_object.phone_number,
                        "email": new_user_object.email}

        try:
            sql ="UPDATE Users SET \
                    username=:username, password=:password, \
                    phone_number=:phone_number, email=:email \
                    WHERE id=:user_id"

            self._db.session.execute(sql, values_to_db)
            self._db.connection.commit()
        except:
            return False
        return True

user_repository = UserRepository()
