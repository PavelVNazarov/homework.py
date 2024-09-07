# Домашнее задание по теме "Режимы открытия файлов"
# Назаров ПВ
# module_7_1.py
from pprint import pprint

# решение старого задания
# name_file = 'poem.txt'
# file = open(name_file, 'w')
# file.write('''My soul is dark - Oh! quickly string
# The harp I yet can brook to hear;
# And let thy gentle fingers fling
# Its melting murmurs o'er mine ear.
# If in this heart a hope be dear,
# That sound shall charm it forth again:
# If in these eyes there lurk a tear,
# 'Twill flow, and cease to burn my brain.
# But bid the strain be wild and deep,
# Nor let thy notes of joy be first:
# I tell thee, minstrel, I must weep,
# Or else this heavy heart will burst;
# For it hath been by sorrow nursed,
# And ached in sleepless silence, long;
# And now 'tis doomed to know the worst,
# And break at once - or yield to song.
# ''')
# file.close()
# file = open(name_file, 'r')
# print(file.read())
# file.close()

class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'
        self.prod_list = []
    
    def get_products(self):
        file = open(self.__file_name, 'r')
        self.prod_list = file.read()
        file.close()
        return self.prod_list

    def add(self, *new_products):
        s1.get_products()
        file = open(self.__file_name, 'a')
        for temp_product in new_products:
            if Product.__str__(temp_product) in self.prod_list:
                print(f'Товар {temp_product.name} уже есть в магазине')
            else:
                file.write(Product.__str__(temp_product)+'\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
