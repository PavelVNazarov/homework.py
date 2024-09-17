# Домашнее задание по теме "Генераторные сборки"
# Назаров ПВ
# module_9_3_old.py

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

#first_result =

second_result = (len(first[i])==len(second[i]) for i in range(len(first)))

#print(list(first_result))
print(list(second_result))
