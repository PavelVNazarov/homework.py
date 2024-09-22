# Домашнее задание по теме "Потоки на классах"
# Назаров ПВ
# module_10_2_old.py

from time import sleep
from threading import Thread
import requests

class Knight(Thread):
    def __init__(self, name, skill):
         super().__init__()
         self.name = name
         self.skill = skill

    def run (self):
        print(f'{self.name}, на нас напали!')
        solt = 100
        days = 0

        while solt > 0:
            solt -= self.skill
            days += 1
            print(f'{self.name}, сражается {days} день(дня)..., осталось {solt} воинов.')
            sleep(0.5)

        print(f'{self.name}, одержал победу спустя {days} дней!')

knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
