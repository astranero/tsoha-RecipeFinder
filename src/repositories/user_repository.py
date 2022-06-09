from werkzeug.security import generate_password_hash
from db import db as default_db
from entities.user import User

class UserRepository:
    def __init__(self, db=default_db):
        self._db = db

    def login(self, username):
        try:
            sql = "SELECT id, username, password, role FROM users WHERE username=:username"
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

    def modify_user(self, new_user_object: User):
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
            self._db.session.commit()
        except:
            return False
        return True

    def get_current_user(self, id):
        try:
            sql = self._db.session.execute("SELECT * FROM Users WHERE id=:id", \
                                            {"id":id}).fetchone()
            return self.create_user_from_result(sql)
        except:
            return False

    def create_user_from_result(self, result_row) -> User:
        if not result_row:
            return None

        return User(
            user_id=result_row[0],
            username=result_row[1],
            password=result_row[2],
            role=result_row[3],
            phone_number=result_row[4],
            email=result_row[5]
        )

user_repository = UserRepository()