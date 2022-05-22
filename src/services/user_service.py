from werkzeug.security import check_password_hash
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

        self._user_repository.signup_user(user)
        self.login_user(username, password)

    def login_user(self, username, password):
        user = self._user_repository.login_user(username)
        if user is not None and check_password_hash(user.password, password):
            return True
        return False

    def logout_user(self):
        self._user_repository.logout_user()




user_service = UserService()



