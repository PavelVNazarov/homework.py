# Домашняя работа по уроку "Специальные методы классов"
# Назаров ПВ

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        h = 'Название {self.name} количество этажей {number_of_floors}'
        return h.format(self=self, number_of_floors=self.number_of_floors)
    
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))