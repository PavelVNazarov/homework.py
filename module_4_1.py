# Домашняя работа по уроку "Модули и пакеты"
# Назаров ПВ
from math import inf
from fake_math import divide as divide_fake
from true_math import divide as divide_true


result1 = divide_fake(69, 3)
result2 = divide_fake(3, 0)
result3 = divide_true(49, 7)
result4 = divide_true(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)