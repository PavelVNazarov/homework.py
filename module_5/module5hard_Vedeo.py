# Дополнительное практическое задание по модулю: "Классы и объекты."
# Назаров ПВ
# module5hard_video.py

import time

class Video:
    # title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    Video = []
    videos = []

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def add(self,other):
        Video.videos.append(self)
        Video.videos.append(other)

    def __str__(self):
        h = '{title}, {duration}, {time_now}, {adult_mode}.'
        return h.format(self=self,
                        title=self.title,
                        duration=self.duration,
                        time_now=self.time_now,
                        adult_mode=self.adult_mode)

    def get_videos(self):
        same_words = []
        for i in range(len(Video.videos)):
            if self.lower() in Video.videos[i].title.lower():
                same_words.append(Video.videos[i].title)
        return same_words

    def watch_video(self):
        for i in range(len(Video.videos)):
            if self == Video.videos[i].title:
                for j in range(Video.videos[i].duration):
                    print(j + 1, end=' ')
                    time.sleep(1)
                print('Конец видео')






v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
Video.add(v1, v2)

print(Video.get_videos('лучший'))
print(Video.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
#Video.watch_video('Для чего девушкам парень программист?')

Video.watch_video('Для чего девушкам парень программист?')

Video.watch_video('Для чего девушкам парень программист?')

# Попытка воспроизведения несуществующего видео
Video.watch_video('Лучший язык программирования 2024 года!')
