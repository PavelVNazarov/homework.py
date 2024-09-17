# Домашнее задание по теме "Списковые, словарные сборки"
# Назаров ПВ
# module_9_2_old.py

def sq_func(number):
    return number**2

def nchet_all(x):
    if x % 2 != 0:
        return x

list_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

results = map(sq_func, filter(nchet_all, list_numbers))
print(list(results))
