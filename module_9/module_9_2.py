# Домашнее задание по теме "Списковые, словарные сборки"
# Назаров ПВ
# module_9_2.py

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

def apply_all_func(int_list, *functions):
    results ={}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results

first_result = [len(word) for word in first_strings if len(word) >= 5]
second_result = [(word_1,word_2) for word_1 in first_strings  for word_2 in second_strings if len(word_1) == len(word_2)]
third_result = {word:len(word) for word in first_strings + second_strings if len(word) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)
