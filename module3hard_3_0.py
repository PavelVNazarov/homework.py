# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Назаров ПВ

def calculate_structure_sum(args):
  count = 0 
  for i in range(len(args)):
    if isinstance(args[i], int):
      count += args[i]
    elif isinstance(args[i], str):
      count += len(args[i])
    elif isinstance(args[i], list):
      count += calculate_structure_sum(args[i])
    elif isinstance(args[i], tuple):
      count += calculate_structure_sum(args[i])
    elif isinstance(args[i], set):
      count += calculate_structure_sum(list(args[i]))
    elif isinstance(args[i], dict):
      count += calculate_structure_sum(list(args[i].items()))
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