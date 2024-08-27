# Дополнительное практическое задание по модулю: "Классы и объекты."
# Назаров ПВ
# module_6_1_old.py

class Car():
    price = 1000000 
    def __init__(self,name):
        self.name = name
         
    def horse_powers(self):
        self.horse_powers = 80
        return self.horse_powers


class Nissan(Car):
    price = 2000000 
    def __init__(self,name):
        self.name = name

    def horse_powers(self):
        self.horse_powers = 120
        return self.horse_powers

class Kia(Car):
    price = 1500000 
    def __init__(self,name):
        self.name = name

    def horse_powers(self):
        self.horse_powers = 100
        return self.horse_powers



a1 = Car('Jeep')
a2 = Nissan('Patrul')
p1 = Kia('Rio')
print(a1.name, a1.price, a1.horse_powers())
print(a1.name)
print(a1.horse_powers)
print(a2.name, a2.price, a2.horse_powers())
print(a1.horse_powers)
print(p1.name)
print(p1.name, p1.price, p1.horse_powers())
print(a1.horse_powers)
print(a2.horse_powers)
print(p1.horse_powers)

