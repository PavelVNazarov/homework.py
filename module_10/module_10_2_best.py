# Домашнее задание по теме "Потоки на классах"
# Назаров ПВ
# module_10_2.py

from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
         self.Knight_name = name
         self.power = power
         super().__init__()

    def run (self):
        print(f'{self.Knight_name}, на нас напали!')
        solt = 100
        days = 0

        while solt > 0:
            solt -= self.power
            days += 1
            print(f'{self.Knight_name}, сражается {days} день(дня)..., осталось {solt} воинов.')
            sleep(1)
        print(f'{self.Knight_name}, одержал победу спустя {days} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы зак
