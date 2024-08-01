# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Назаров ПВ

import inspect

def calculate_structure_sum(args):
 # print(args)
  count = 0 # переменная счетчика
  # params = locals().keys()
  # # Сразу копируйте ключи, пока locals() не наполнился другими переменными!
  # param_list = list(params)
  # # Продолжение функции
  # print(param_list)
  for i in range(len(args)):
    # определили тип аргументов
    print("\nData type of argument: ",type(args[i]),args[i])
    if type(args[i]) == int:
      count += args[i]
    elif type(args[i]) == str:
      count += len(args[i])
    elif type(args[i]) == list:
      count += calculate_structure_sum(args[i])
    #elif type(args[i]) == dict:

  return count


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
