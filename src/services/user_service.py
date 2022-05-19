from repositories.user_repository import (
    user_repository as default_user_repository)

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def register_user(self, username, password):
        pass

    def login_user(self, username, password):
        pass

    def logout_user(self):
        pass

    def is_authenticated(self):
        pass

user_service = UserService()



