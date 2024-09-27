# Домашнее задание по теме "Интроспекция"
# Назаров ПВ
# module_11_3.py

def introspection_info(obj):
    number_info = {}
    number_info['type'] = (type(obj))
    return number_info

number_info = introspection_info(42)
print(number_info)
