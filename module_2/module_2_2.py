# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
# Назаров ПВ
first=int(input("Введите первое число: "))
second=int(input("Введите второе число: "))
third=int(input("Введите третье число: "))
if first==second and first==third and second==third:
  print(3,'все числа равны')
elif first==second or first==third or second==third:
    print(2,'два числа равны')
else:
  print(0,'равных чисел нет')
