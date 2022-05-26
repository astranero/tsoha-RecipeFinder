from werkzeug.security import check_password_hash
from flask import session, abort, request
import secrets
from entities.user import User
from repositories.user_repository import (
    UserRepository as default_user_repository)

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def register_user(self, username, password, role, phone_number, email):

        user = User(username=username,
                    password=password,
                    role=role,
                    phone_number=phone_number,
                    email=email)

        self._user_repository.signup_user(user)
        self.login_user(username, password)

    def login_user(self, username, password):
        user = self._user_repository.login(username)
        if not user:
            return False
        if check_password_hash(user.password, password):
            session["id"] = user.id
            session["username"] = user.username
            session["role"] = user.role
            session["csrf_token"] = secrets.token_hex(16)
            return True
        return False

    def logout(self):
        del session["id"]
        del session["username"]
        del session["role"]
        del session['csrf_token']

    def check_csrf(self):
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)

    def user_role(self):
        return session.get("role", 0)

    def require_role(self, role):
        if role > session.get("role", 0):
            abort(403)

user_service = UserService()



