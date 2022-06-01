from werkzeug.security import check_password_hash
from flask import session, abort, request
import secrets
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def register_user(self, username, password, role, phone_number, email):

        user = User(username=username,
                    password=password,
                    role=role,
                    phone_number=phone_number,
                    email=email)

        self.validate_registration(username, email, phone_number)
        self._user_repository.register_user(user)
        self.login_user(username, password)

    def validate_registration(self, username, email, phone_number):
        assert not self._user_repository.check_if_username_exists(username), "Username is taken"
        assert not self._user_repository.check_if_email_exists(email), "Email is taken"
        assert not self._user_repository.check_if_phone_number_exists(phone_number), "Phone number is taken"

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

    def get_current_username(self, id):
        return self._user_repository.get_current_user(id).username

    def get_current_email(self, id):
        return self._user_repository.get_current_user(id).email

    def get_current_phone_number(self, id):
        return self._user_repository.get_current_user(id).phone_number

    def get_current_phone_number(self, id):
        return self._user_repository.get_current_user(id).role

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