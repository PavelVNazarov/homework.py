# Дополнительное практическое задание по модулю: "Наследование классов."
# Назаров ПВ
# module6hard_from_Putilov_vladimir_2.py


import math
class Figure:
    '''Геометрические фигуры'''
    sides_count = 0                  # количество сторон, рёбер


    def __init__(self, color, *sides):
        self.__color = list(color)    # цвет стороны RGB
        self.filled = False           # закрашенный
        self.__sides = list(sides)

    def get_color(self):            # возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, r, g, b):  # проверка корректности
        if isinstance(r,int) and isinstance(g,int) and isinstance(b,int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if self.__is_valid_color == True:
            self.__color = [r, g, b]

    def get_color(self):    # возвращает список RGB цветов
        return self.__color

    def get_sides(self):
        return self.__sides

    def __len__(self):              # периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides == True:
            if len(new_sides) == 1:
                self.__sides = list(new_sides)*self.sides_count
            elif len(new_sides) == self.sides_count:
                self.__sides = list(new_sides)
            else:
                self.__sides = [1]*self.sides_count

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return len(sides) == self.sides_count

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = super().get_sides()
        self.__radius = self.__sides[0] / (2 * math.pi)

    def radius(self):
        return self.__sides[0] / (2 * math.pi)

    def get_square(self):               # площадь круга
        square = (self.__sides[0] ** 2) / (4 * math.pi)
        return square

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = self.get_sides()*self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = list(new_sides)*self.sides_count
        elif len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            self.__sides = Figure.get_sides(self)
            self.__sides = list(self.__sides)*self.sides_count

    def get_square(self, *sides):               # площадь треугольника
        if len(sides) == 0:
            self.a_ = self.__sides[0]
            self.b_ = self.__sides[1]
            self.c_ = self.__sides[2]
        else:
            self.a_ = sides[0]
            self.b_ = sides[1]
            self.c_ = sides[2]
        p = (self.a_ + self.b_ + self.c_) / 2
        square = math.sqrt(p * (p - self.a_) * (p - self.b_) * (p - self.c_))
        return square

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        
    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = list(new_sides)*self.sides_count
        elif len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            self.__sides = Figure.get_sides(self)
            self.__sides = list(self.__sides)*self.sides_count
            
    def get_sides(self):
        self.set_sides()
        return self.__sides

    def get_volume(self):               # площадь куба
        volume = self.__sides[0] ** 3
        return volume


# issubclass(Cube, Figure)
# print(Cube.mro)
#_______________________________________________________
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((44, 120, 245), 3)

    # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
print('Площадь треугольника')
print(triangle1.get_square())
print(triangle1.get_square(4, 5, 6))

   # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides (15)  # Изменится
print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
print(len(circle1))

    # Проверка объёма (куба):
print(cube1.get_volume())
