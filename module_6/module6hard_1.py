# Дополнительное практическое задание по модулю: "Наследование классов."
# Назаров ПВ
# module6hard.py
import math


class Figure():
    sides_count = 0

    def __init__(self, color=[], sides=[]):
        self.__sides = sides
        self.__color = color
        filled = False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r,g,b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __len__(self):
        return sum(self.__sides)

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

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            return True
        return False


class Circle(Figure):
    def __init__(self, arg, *sides_args):
        self.sides_count = 1
        self.sides = list()
        if len(sides_args) != self.sides_count:
            self.sides = [1]
        else:
            self.sides = sides_args[0]
        self.__radius = self.sides/ (2 * math.pi)
        super().__init__(self)
        super().set_color(arg[0], arg[1], arg[2])
        super().set_sides(self.sides)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, arg, *sides_args):
        self.sides_count = 3
        self.sides = list()
        if len(sides_args) == 1:
            for i in range(self.sides_count):
                self.sides.append(sides_args[0])
        elif len(sides_args) != self.sides_count:
            for i in range(self.sides_count):
                self.sides.append(1)
        else:
            for i in range(self.sides_count):
                self.sides[i] = sides_args[i]
        super().__init__(self)
        super().set_color(arg[0],arg[1],arg[2])
        super().set_sides(*self.sides)

    def get_square(self):
        p = (a + b + c) / 2
        S = sqrt(p(p - a)(p - b)(p - c)),
        return S


class Cube(Figure):
    def __init__(self,  arg, *sides_args):
        self.sides_count = 12
        self.sides = list()

        if len(sides_args) == 1:
            for i in range(self.sides_count):
                self.sides.append(sides_args[0])
        elif len(sides_args) != self.sides_count:
            for i in range(self.sides_count):
                self.sides.append(1)
        else:
            for i in range(self.sides_count):
                self.sides[i] = sides_args[i]
        super().__init__(self)
        super().set_color(arg[0],arg[1],arg[2])
        super().set_sides(*self.sides)
    def get_volume(self):
        return self.sides[0]*self.sides[1]*self.sides[2]



circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
