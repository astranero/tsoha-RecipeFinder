import secrets
from flask import abort, request, session
from werkzeug.security import generate_password_hash
from db import db
from entities.user import User

class UserRepository:
    def __init__(self):
        pass

    def login_user(self, username):
        try:
            sql = "SELECT user_id, password, role FROM users WHERE username=:username"
            user = db.session.execute(sql, {"username":username}).fetchone()
            session["id"] = user.id
            session["username"] = user.username
            session["role"] = user.role
            session["csrf_token"] = secrets.token_hex(16)
        except:
            return None

    def check_csrf(self):
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)

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
            db.session.execute(sql, values_to_db)
            db.session.commit()
        except:
            return None

    def logout(self):
        del session["id"]
        del session["username"]
        del session["role"]


user_repository = UserRepository()
