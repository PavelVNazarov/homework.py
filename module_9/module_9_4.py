# Домашнее задание по теме "Создание функций на лету"
# Назаров ПВ
# module_9_4.py

from random import choice

#Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'



# Замыкание



# Метод __call__
class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self):
        word = choice(self.words)
        return word

first_ball = MysticBall('надо', 'меньше', 'пить')
print(first_ball())
print(first_ball())
print(first_ball())
