# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Назаров ПВ

def calculate_structure_sum(args):
  count = 0 
  for i in range(len(args)):
    match args[i]:
      case int():
        count += args[i]
      case str():
        count += len(args[i])
      case list():
        count += calculate_structure_sum(args[i])
      case tuple():
        count += calculate_structure_sum(args[i])
      case set():
        count += calculate_structure_sum(list(args[i]))
      case dict():
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