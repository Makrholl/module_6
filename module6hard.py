import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = False
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(s, int) and s > 0 for s in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__update_radius()

    def __update_radius(self):
        side_length = self.get_sides()[0]
        self.__radius = side_length / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def __len__(self):
        return int(2 * math.pi * self.__radius)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__update_radius()


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1] * self.sides_count
        else:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


# Пример использования:
circle1 = Circle((200, 200, 100), 10)  # Цвет (RGB), сторона = длина окружности
cube1 = Cube((222, 35, 130), 6)

# Проверка изменения цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # Выведет: [55, 66, 77]

cube1.set_color(300, 70, 15)  # Не изменится (некорректный цвет)
print(cube1.get_color())  # Выведет: [222, 35, 130]

# Проверка изменения сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится (количество сторон не совпадает)
print(cube1.get_sides())  # Выведет: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # Выведет: [15]

# Проверка периметра (для круга длина окружности)
print(len(circle1))  # Выведет: 15

# Проверка объёма (куба)
print(cube1.get_volume())  # Выведет: 216

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
