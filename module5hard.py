# Дополнительное практическое задание по модулю: "Классы и объекты."
# Назаров ПВ
# module5hard.py

import time

class UrTube:
  #users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)

    # def __init__(self, users, videos, current_user):
    #     self.users = users = {}
    #     self.videos = videos = {}
    #     self.current_user = current_user=nick_name
        

    def add_user(self, User):
        self.users.append(User)

    def add(*args):
        Video.add_video(args)
       

    def get_current_user(self):
        return self.current_user

    def set_current_user(self, User):
        self.current_user = User

    def log_in(self, nikname,pasword):
        if self.nikname in User and self.pasword == pasword:
            self.current_user = User
        else:
            register()

    def register(self, nikname,pasword,age):
        print('Пожалуйста, пройдите регистрацию: ')
        nikname = input('Введите ваш никнейм: ')
        pasword = input('Введите ваш пароль: ')
        age = input('Введите ваш возраст: ')
        if self.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.nikname == self.nikname:
         print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User)
            self.current_user = User

    def log_out(self):
        self.current_user = None



    def get_video(self, search_Video):
        if lower(search_Video) in lower(videos):
            return Video
        else:
            return None

    def watch_video(self, wait_vidoe):
        if self.current_user is None:
            print("Вы не авторизованы")
        elif self.current_user.age < 18:
            print(f"Вам нет 18 лет, пожалуйста покиньте страницу")
        elif self.wait_video in self.videos:
            for i in range(1,10+1):
                print(i, end=' ')
                time.sleep(1)
            print('Конец видео')




class Video:
   # title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title =  title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        videos = {title: [duration,time_now,adult_mode]}
    
    def add_video(args):
        videos['title'] = '[duration,time_now,adult_mode]'
        


class User:
  # Класс пользователь, содержащий атрибуты: логин и пароль

  def __init__(self, nickname, pasword, age):
    self.username = nickname
    self.pasword = pasword
    self.age = age
    users = {nickname:[pasword, age]}


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))

# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')

# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)

# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
# print(ur.current_user)

# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
