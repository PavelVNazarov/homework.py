# Домашнее задание по теме "Генераторные сборки"
# Назаров ПВ
# module_9_3.py

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

new = list(zip(first,second))
first_result = (len(new[i][0]) - len(new[i][1]) for i in range(len(first)) if len(new[i][0]) != len(new[i][1]))

second_result = (len(first[i])==len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))
