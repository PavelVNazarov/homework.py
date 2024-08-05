# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Назаров ПВ


def calculate_structure_sum(*args):
  count = 0 
  for i in args:
    match i:
      case int():
        count += i
      case str():
        count += len(i)
      case list()|tuple()|set():
        count += calculate_structure_sum(*i)
      case dict():
        count += calculate_structure_sum(*i.keys())
        count += calculate_structure_sum(*i.values())
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
