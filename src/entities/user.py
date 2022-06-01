
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
            word = str(self.password)
            word2 = word.replace("(", "")
            word3 = word2.replace(")", "")
            word4 = word3.replace("'", "")
            word5 = word4.replace(",", "")
            user.append(f'{word5}')
        if self.role:
            user.append(f'{self.role}')
        if self.phone_number:
            number = str(self.phone_number)
            number2 = number.replace("(", "")
            number3 = number2.replace(")", "")
            number4 = number3.replace("'", "")
            number5 = number4.replace(",", "")
            user.append(f'{number5}')
        if self.email:
            mail = str(self.email)
            mail2 = mail.replace("(", "")
            mail3 = mail2.replace(")", "")
            mail4 = mail3.replace("'", "")
            mail5 = mail4.replace(",", "")
            user.append(f'{mail5}')
        return ", ".join(user)

    def __str__(self):
        return self.format()