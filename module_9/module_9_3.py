# Домашнее задание по теме "Генераторные сборки"
# Назаров ПВ
# module_9_3.py

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

#new = list(zip(first,second))
first_result = (len(list(zip(first,second))[i][0]) - len(list(zip(first,second))[i][1]) for i in range(len(list(zip(first,second)))) if len(list(zip(first,second))[i][0]) != len(list(zip(first,second))[i][1]))

second_result = (len(first[i])==len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))
