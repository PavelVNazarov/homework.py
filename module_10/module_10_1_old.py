# Домашнее задание по теме "Создание потоков".
# Назаров ПВ
# module_10_1_old.py

from time import sleep
from threading import Thread
from datetime import datetime
import requests

def func (*new_tupl):
        for char in new_tupl:
            print(char)
            sleep(1)

thr_first = Thread(target = func, args = (1,2,3,4,5,6,7,8,9,10))
thr_second = Thread(target = func, args = ('a','b','c','d','e','f','g','h','i','j'))

thr_first.start()
thr_second.start()

thr_first.join()
thr_second.join()
