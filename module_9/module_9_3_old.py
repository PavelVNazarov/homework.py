# Домашнее задание по теме "Генераторные сборки"
# Назаров ПВ
# module_9_3_old.py

def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add # возвращаем функцию как объект!! Тут скобки не нужны
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract
my_func_add = create_operation("add")
print(my_func_add(1,2))
#Пример лямбда функции с аналогом через def
multiply = lambda x, y: x * y
print(multiply(2, 3)) # Выводит 6
def multiply_def(x, y):
   return x * y
print(multiply_def(2, 3)) # Выводит 6
#Пример создания вызываемого объекта
class Repeater:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return [self.value] * n
repeat_five = Repeater(5)
print(repeat_five(3)) # Выводит [5, 5, 5]

