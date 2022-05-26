
class User:
    def __init__(self, username, user_id=None, password=None, role=None, phone_number=None, email=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.phone_number = phone_number
        self.email = email

