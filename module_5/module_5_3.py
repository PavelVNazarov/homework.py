# Домашняя работа по уроку "Перегрузка операторов."
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
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10 
print(h1)
print(h1 == h2)

h1 += 10 
print(h1)

h2 = 10 + h2 
print(h2)

print(h1 > h2) 
print(h1 >= h2) 
print(h1 < h2) 
print(h1 <= h2) 
print(h1 != h2) 
