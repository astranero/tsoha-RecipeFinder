
class User:
    def __init__(self, username=str, user_id=None, password=str, role=int, phone_number=int, email=str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.phone_number = phone_number
        self.email = email

    def format(self):
        user = []
        if self.user_id:
            user.append(f'{self.user_id}')
        if self.username:
            user.append(f'{self.username}')
        if self.password:
            user.append(f'{self.password}')
        if self.role:
            user.append(f'{self.role}')
        if self.phone_number:
            user.append(f'{self.phone_number}')
        if self.email:
            user.append(f'{self.email}')
        return " ".join(user)

    def __str__(self):
        return self.format()