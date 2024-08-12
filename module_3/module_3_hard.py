# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Назаров ПВ

def calculate_structure_sum(args):
  count = 0 # переменная счетчика
  for i in range(len(args)):
    # определили тип аргументов
    #print("\nData type of argument: ",type(args[i]),args[i])
    if type(args[i]) == int:
      count += args[i]
    elif type(args[i]) == str:
      count += len(args[i])
    elif type(args[i]) == list:
      count += calculate_structure_sum(args[i])
    elif type(args[i]) == tuple:
      count += calculate_structure_sum(args[i])
    elif type(args[i]) == set:
      temp_list = list(args[i])
      count += calculate_structure_sum(temp_list)
    elif type(args[i]) == dict:
      pairs = list(args[i].items()) 
      count += calculate_structure_sum(pairs)
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
