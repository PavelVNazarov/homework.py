# Домашнее задание по теме "Множественное наследование"
# Назаров ПВ
# module_6_3_old.py

class Vehicle():
    vehicle_type = "none"


class Car():
    price = 1000000
    def horse_powers(self):
        horse_powers = self.horse_powers = 80
        return horse_powers


class Nissan(Vehicle, Car):
    price = 1500000
    vehicle_type = "Jeep"
    def horse_powers(self):
        horse_powers = self.horse_powers = 100
        return horse_powers


p1 = Nissan()

print(p1.vehicle_type, p1.price)
