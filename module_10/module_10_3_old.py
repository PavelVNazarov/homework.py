# Домашнее задание по теме "Блокировки и обработка ошибок"
# Назаров ПВ
# module_10_3_old.py

from time import sleep
from threading import Thread, Lock
from random import randint

lock = Lock()
