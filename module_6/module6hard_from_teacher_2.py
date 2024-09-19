from math import pi

class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__color = color
        self.filled = False
        self.__sides = sides

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return (0<=r<=255 and 0<=g<=255 and 0<=b<=255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    @classmethod
    def __is_valid_sides(cls,*sides):
        flag = True
        for side in sides:
            if side<=0 or not isinstance(side,int):
                flag = False
                break
        return flag and len(sides)==cls.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *side):
        sides = side[0] if len(side) == self.sides_count else [1]
        super().__init__(color, sides)

    def get_square(self):
        self.__radius = len(self)/(2 * pi)
        return pi*(self.__radius)**2


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *side):
        if len(side) == 1:
            sides = [side[0]]*self.sides_count
        elif len(side) == self.sides_count:
            sides = side
        else:
            sides = [1]*self.sides_count
        super().__init__(color, sides)
        self.sides = sides

    def get_square(self):
        a, b, c = self.sides
        p = len(self)/2
        return (p*(p-a)*(p-b)*(p-c))**(1/2)


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *side):
        if len(side) == 1:
            sides = [side[0]]*self.sides_count
        elif len(side) == self.sides_count:
            sides = side
        else:
            sides = [1]*self.sides_count
        super().__init__(color, sides)
        self.sides = sides

    def get_volume(self):
        return self.sides[0]**3


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


print()
print("Еще одна проверка")
circle2 = Circle((200, 200, 100), 10, 15, 6)
print(circle2.get_sides())
print(circle1.get_square())
print(circle2.get_square())
Triangle1 = Triangle((200, 200, 100), 10, 6)
print(Triangle1.get_sides())
print(Triangle1.get_square())
cube2 = Cube((200, 200, 100), 9)
print(cube2.get_sides())
cube3 = Cube((200, 200, 100), 9, 12)
print(cube3.get_sides())
Triangle2 = Triangle((200, 200, 100), 3, 4, 5)
print(Triangle2.get_sides())
print(Triangle2.get_square())
print(len(Triangle2))
