# Дополнительное практическое задание по модулю: "Наследование классов."
# Назаров ПВ
# module6hard.py
import math

class Figure():
    sides_count = 0
    
    def __init__(self, color = [], sides = []):
        self.__sides = sides
        self.__color = color
        filled = False

    def set_color(self, r ,g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.__color = [r, g, b]
            
    def get_color(self):
        return self.__color


    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and new_sides[0] > 0:
            self.__sides = list(new_sides)
        elif len(new_sides) == self.sides_count:
            if self.__is_valid_sides(new_sides):
                self.__sides = new_sides

    def __len__(self):
        return sum(self.__sides)

    def get_sides(self):
        return self.__sides
        return self.__color


    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and new_sides[0] > 0:
            self.__sides = list(new_sides)
        elif len(new_sides) == self.sides_count:
            if self.__is_valid_sides(new_sides):
                self.__sides = new_sides

    def __len__(self):
        return sum(self.__sides)

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, new_sides):
        if len(new_sides) == self.sides_count:
            for side in new_sides:
                if side > 0:
                    return True
        return False

    def __is_valid_color(self, color):
        if len(color) == 3:
            for element in color:
                if 0 <= element <= 255:
                    return True
        return False        


class Circle(Figure):
    def __init__(self, color=[], *sides_args):
        self.sides_count = 1
        if len(sides_args) != self.sides_count:
            sides = [1]
        else:
            sides = sides_args[0]
        self.__radius = sides/(2*math.pi)
        super().__init__(self)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, color=[], *sides_args):
        self.sides_count = 3
        if len(sides_args) == 1:
            for i in range(self.sides_count):
                sides[i] = sides_args
        elif len(sides_args) != self.sides_count:
            sides = [1,1,1]
        else:
            for i in range(self.sides_count):
                sides[i] = sides_args[i]
        super().__init__(self)

    def get_square(self):
        p=(a+b+c)/2
        S=sqrt (p(p-a)(p-b)(p-c)),
        return S

class Cube(Figure):
    def __init__(self, color=[], *sides_args):
        self.sides_count = 12
        if len(sides_args) == 1:
            for i in range(self.sides_count):
                sides[i] = sides_args
        elif len(sides_args) != self.sides_count:
            for i in range(self.sides_count):
                sides[i] = 1
        else:
            for i in range(self.sides_count):
                sides[i] = sides_args[i]
        super().__init__(self)

    def get_volume(self):
        return self.__sides**3

print('Пока все нормально')

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
