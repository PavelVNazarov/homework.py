# Дополнительное практическое задание по модулю: "Наследование классов."
# Назаров ПВ
# module6hard.py
import math

class Figure():
    def __init__(self, sides_count = 0, __sides = [], __color = [r, g, b]):
        self.sides_count = sides_count
        self.__sides = sides
        filled = False
        self.__color = color
        
    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if side > 0:
                    return True
        return False

    def __is_valid_color(self, color):
        if len(color) == 3:
            for element in color:
                if 0 <= element <= 255:
                    return True
        return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides

    def _len(self):
        return len(self.__sides)


class Circle(Figure):
    def __init__(self, sides_count = 1):
        super().__init__(sides_count)
        self.sides_count = sides_count
        self.__radius = self.sides/(2*math.pi)
        
    def get_square(self):
        return math.pi * self.__radius ** 2
        
class Triangle(Figure):
    def __init__(self, sides_count = 3):
        super().__init__(sides_count)
        self.sides_count = sides_count

    def get_square(self):
        p={(a+b+c)/2}
        S={\sqrt {p(p-a)(p-b)(p-c)}}},
        return S

class Cube(Figure):
    def __init__(self, sides_count = 12):
        super().__init__(sides_count)
        self.sides_count = sides_count
       
    def get_volume(self):
        return self.__sides**3
