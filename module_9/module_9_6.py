# Домашнее задание по теме "Генераторы"
# Назаров ПВ
# module_9_6.py

def all_variants(text):
    yield(text)

a = all_variants("abc")
for i in a:
    print(i)
