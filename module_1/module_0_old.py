# Практическое задание по уроку "Базовые структуры данных"
# Назвров ПВ
# module_0_old.py

# Задача 1: Арифметика
# 1st program
result = 9 ** 0.5 * 5
print(result)  # Ожидаемый результат: 15.0
print(9 ** 0.5 * 5)

# Задача 2: Логика
# 2nd program
result = 9.99 > 9.98 and 1000 != 1000.1
print(result)  # Ожидаемый результат: True
print(9.99 > 9.98 and 1000 != 1000.1)


# Задача 3: 
# 3th program
number_1 = 1234
number_2 = 5678
print ((number_1 // 10 % 100) + (number_2 // 10 % 100))
number_1 = str(number_1)
number_1 = str(number_1[1:3])
number_1 = int(number_1)
number_2 = str(number_2)
number_2 = str(number_2[1:3])
number_2 = int(number_2)
print(number_1+number_2)
