# Дополнительное практическое задание по модулю: "Классы и объекты."
# Назаров ПВ
# module5hard_User.py

class User:
    # Класс пользователь, содержащий атрибуты: логин и пароль

    current_user = None
    users = []
    User = []

    def __init__(self,
                 nickname,
                 # pasword = hash('pasword'),
                 pasword,
                 age):
        self.nickname = nickname
        self.pasword = pasword
        self.age = age
        # self.User = [nickname, pasword, age]
        # self.users.append(self.User)
        # User.current_user = nickname
        # print(User.current_user)

    # def __str__(self):
    #     h = '{nickname}, {pasword}, {age}.'
    #     return h.format(self = self,
    #                     nickname = self.nickname,
    #                     pasword = self.pasword,
    #                     age = self.age)

    def register(nickname, pasword, age):
        Us = User(nickname, pasword, age)
        if len(User.users) == 0:
            User.users.append(Us)
            User.current_user = nickname
        else:
            for i in range(len(User.users)):
                if nickname == User.users[i].nickname:
                    if pasword != User.users[i].pasword:
                        print(f'Пользователь {nickname} уже существует')
                else:
                    User.current_user = User.users[i].nickname
                    User.users.append(Us)
        return User.current_user

