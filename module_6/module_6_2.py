# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
# Назаров ПВ
# module_6_2.py

class Vehicle():

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        
    
    def get_model(self):
        str_1 =  f"Модель: {self.__model}"
        return str_1

    def get_horsepower(self):
        str_2 =  f"Мощность двигателя: {self.__engine_power}"
        return str_2

    def get_color(self):
        str_3 =  f"Цвет: {self.__color}"
        return str_3

    def print_info(self):
        print(Vehicle.get_model(self))
        print(Vehicle.get_horsepower(self))
        print(Vehicle.get_color(self))
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color:str):
        change_color = False
        for i in range(len(self.__COLOR_VARIANTS)):
            if new_color.lower() == self.__COLOR_VARIANTS[i].lower():
                self.__color = new_color
                change_color = True
                break
        if change_color == False:
                print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

# Вывод на консоль:
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: blue
# Владелец: Fedos
# Нельзя сменить цвет на Pink
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: BLACK
# Владелец: Vasyok
