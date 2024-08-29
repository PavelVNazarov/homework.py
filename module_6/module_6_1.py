# Домашнее задание по теме "Зачем нужно наследование"
# Назаров ПВ
# module_6_1.py

class Animal():
    def __init__(self, name):
        self.alive = alive = True 
        self.fed = fed = False 
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant():
    def __init__(self, name):
        self.edible = edible = False 
        self.name = name 


class Mammal(Animal):
    pass
    # def __init__(self, name):
    #     self.name = name


class Predator(Animal):
    pass
    # def __init__(self, name):
    #     self.name = name


class Flower(Plant):
    pass
    # def __init__(self, name):
    #     self.name = name


class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

