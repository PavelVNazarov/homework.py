# Практическое задание по теме: "Словари и множества"
# Назаров ПВ
# словари
my_dict = {'Andrey':1970, 'Vasya':1980, 'Petya':1985, 'Kolya':1975}
print(my_dict)
print('Год рождения Андрея ',my_dict['Andrey'])
print ('Год рождения Элрона ',my_dict.get ('Denis',"Нет такого имени"))
my_dict.update({'Angelica': 2000,
               'Sveta':1999})
print('Нас покинул Коля, его год рождения ',my_dict.pop('Kolya'))
print('К нам добавились девушки!')
print('Новый список')
print(my_dict)
print()
# множества
my_set = {'Шашлык', 0.5, 0.5, 0.5, 'Дождь'}
print(my_set)
print("Добавляем нужное...")
my_set.add('Друзья')
my_set.add(0.7)
print("Убираем лишнее...")
my_set.discard('Дождь')
print(my_set)