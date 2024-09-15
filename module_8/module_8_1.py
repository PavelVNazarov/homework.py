# Домашнее задание по теме "Try и Except".
# Назаров ПВ
# module_8_1.py

def add_everything_up(a, b):
    try:
        return round(a + b,3)
    except TypeError:
        return str(a)+str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
