# Дополнительное практическое задание по модулю: "Классы и объекты."
# Назаров ПВ
# module5hard.py

class UrTube:
    # users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)

    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def add_user(self, User):
        self.users.append(User)

    def add_video(self, Video):
        self.videos.append(Video)

    def get_current_user(self):
        return self.current_user

    def set_current_user(self, User):
        self.current_user = User

    def log_in(self, nikname, pasword):
        if nikname == self.:
            self.current_user = User
        else:
            register()

    def register(self, nikname, pasword, age):
        if self.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.nikname == self.nikname:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User)
            self.current_user = User

    def log_out(self):
        self.current_user = None

    def add(Video):
        if self.Video not in videos:
            self.videos.append(Video)




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')