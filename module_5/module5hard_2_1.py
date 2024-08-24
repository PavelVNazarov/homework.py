# Дополнительное практическое задание по модулю: "Классы и объекты."
# Назаров ПВ
# module5hard.py

import time

class Video:
    # title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    #Video = []

    def __init__(self, title, duration, time_now=0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        h = '{title}, {duration}, {time_now}, {adult_mode}.'
        return h.format(self=self,
                        title=self.title,
                        duration=self.duration,
                        time_now=self.time_now,
                        adult_mode=self.adult_mode)


class User:
    # Класс пользователь, содержащий атрибуты: логин и пароль
   # User = []

    def __init__(self,
                 nickname,
                 password,
                 age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        #pasword = hash('pasword')


class UrTube:
    # users(список объектов User), videos(список объектов Video), current_user (текущий пользователь User)
    # users = []
    # videos = []
    # current_user = None
    # current_user_adult_mode = False

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.current_user_adult_mode = False
    

    def register(self, nickname, password, age):
        #Us = User(nickname, password, age)       
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname,password,age)
        self.users.append(new_user)
        self.current_user = new_user.nickname
        self.curent_user_adult_mode = age < 18

    def add(self,*Videos):
        for video in Videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, word):
        same_words = []
        for i in range(len(self.videos)):
            if word.lower() in self.videos[i].title.lower():
                same_words.append(self.videos[i].title)
        return same_words

    def log_in(self, nickname, pasword):
        for i in range(len(UrTube.users)):
            if nickname == UrTube.users[i].nickname:
                if hash(pasword) == hash(UrTube.users[i].pasword):
                    UrTube.current_user = nickname
                    return UrTube.current_user
                else:
                    print('Неверный пароль')
                    break
            else:
                print('Пользователь не найден')

    def log_out(self):
        current_user = None
        UrTube.current_user_adult_mode = False

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        else:
            for video in self.videos:
                if video.title == title:
                    if video.adult_mode and self.current_user_adult_mode:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        self.log_out()
                        return
                    else:
                        for second in range(video.time_now,video.duration):
                            print(second+1, end = ' ')
                            time.sleep(1)
                        video.time_now = 0
                        print('Конец видео')
                        return
                #print('Видео не найдено')


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