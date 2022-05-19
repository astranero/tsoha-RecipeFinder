import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash
from entities.user import User

class UserRepository:
    def __init__(self):
        pass

    def login_user(self, username, password):
        sql = "SELECT password, id, role FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        if not user:
            return False
        if not check_password_hash(user[0], password):
            return False
        session["id"] = user[1]
        session["username"] = username
        session["role"] = user[2]
        session["csrf_token"] = os.urandom(16).hex()
        return True

    def check_login(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            return user
        else:
            return None


    def register_user(self, username, password, role):
        pass



user_repository = UserRepository()
