# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
# Назаров ПВ

class House:
    houses_history = []

    def __new__(cls,*args):
        if cls.houses_history not in cls.houses_history:
            cls.houses_history.append(cls)
        return cls.houses_history
        
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self)
    
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        h = 'Название {self.name} количество этажей {number_of_floors}'
        return h.format(self=self, number_of_floors=self.number_of_floors)

    def __del__(self):
        print(self.name," снесён, но он останется в истории")


    
    def __eq__(self, other):
      if isinstance(other, House):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
      if isinstance(self, House) and isinstance(value, int):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
      return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
      return House(self.name, self.number_of_floors + value)

    def __lt__(self, other):
      if isinstance(self, House) and isinstance(other, House):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
      if isinstance(self, House) and isinstance(other, House):
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
      if isinstance(self, House) and isinstance(other, House):
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
      return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
      if isinstance(self, House) and isinstance(other, House):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
    



