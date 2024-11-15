# Практическое задание по уроку "Базовые структуры данных"
# Назвров ПВ
# module_0

# Задача 1: Арифметика
# 1st program
result = 9 ** 0.5 * 5
print(result)  # Ожидаемый результат: 15.0


# Задача 2: Логика
# 2nd program
result = 9.99 > 9.98 and 1000 != 1000.1
print(result)  # Ожидаемый результат: True


# Задача 3: Школьная загадка
# 3rd program
result1 = 2 * 2 + 2  # Без приоритета
result2 = 2 * (2 + 2)  # С приоритетом для сложения
comparison_result = result1 == result2
print(result1)  # 6
print(result2)  # 8
print(comparison_result)  # Ожидаемый результат: False


# Задача 4: Первый после точки
# 4th program
number_str = '123.456'
number_float = float(number_str)  # Преобразуем в дробное число
shifted_number = number_float * 10  # Умножаем на 10
integer_part = int(shifted_number)  # Преобразуем в целое число
first_digit_after_decimal = integer_part % 10  # Находим первую цифру после запятой
print(first_digit_after_decimal)  # Ожидаемый результат: 4
