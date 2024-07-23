# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
# Назаров ПВ
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list() # Создаем список для хранения простых чисел
not_primes = list() # Создаем список для хранения непростых чисел
is_prime = True
for i in range(0, len(numbers)):
    if numbers[i] == 1:
       print ('1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.')
       continue
    for j in range(0, len(numbers)):
        if numbers[j] == 1:
             continue
        if numbers[i] % numbers[j] == 0 and numbers[i] == numbers[j]:
            is_prime = True
        elif numbers[i] > numbers[j] and numbers[i] % numbers[j] == 0 and numbers[i] != numbers[j]:
            is_prime = False 
            break
            
    if is_prime == False:
        not_primes.append(numbers[i])
        is_prime = True
    else:
        primes.append(numbers[i])

print('Primes',primes)
print('Not_primes',not_primes)
      