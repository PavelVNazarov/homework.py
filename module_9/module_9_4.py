# Домашнее задание по теме "Создание функций на лету"
# Назаров ПВ
# module_9_4.py

from random import choice

#Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda first, second: first == second, first, second)))


# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, encoding='utf-8') as file:
            file.write(data_set)
            #return data_set
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


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
