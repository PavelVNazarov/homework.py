# Дополнительное практическое задание по модулю: "Основные операторы"
# Назаров ПВ
import random

x = random.randint(3, 20)
key_list = str(x)+' - '
list_key = str(x)+' - '
for i in range(1,20):
    if i != x and i < x:
        for j in range(1,20):
            if j != i and j != x and j < x and x % (i + j) == 0:
                if len(key_list) <= 5:
                    key_list += str(i)+' и '+str(j)
                else:
                    key_list +=', '+str(i)+' и '+str(j)
                list_key += str(i)+str(j)
print('Ответ в том виде как в задании')
print(list_key)
print('Понятный ответ')
print(key_list+'.')