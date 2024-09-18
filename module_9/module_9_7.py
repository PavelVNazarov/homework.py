# Домашнее задание по теме "Декораторы"
# Назаров ПВ
# module_9_7.py

def is_prime(func):
     def my_func(*numbers):
         result = func(*numbers)
         k = 0
         for i in range(2, result// 2 + 1):
             if (result % i == 0):
                 k += 1
         if k <= 0:
             print("Простое")
         else:
             print("Составное")
         return result
     return my_func

#@is_prime
def sum_three(*numbers):
    return (sum(numbers))

sum_three = is_prime(sum_three)

result = sum_three(2, 3, 6)
print(result)
