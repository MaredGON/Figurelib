from abc import ABC, abstractmethod
import math


class Figure(ABC):
    """
    Абстрактный базовый класс для всех фигур.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Вычисляет площадь фигуры.

        :return: Площадь фигуры.
        """
        pass


class Triangle(Figure):
    """
    Класс для представления треугольника.

    Атрибуты:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.
    """

    def __init__(self, a: float, b: float, c: float):
        """
        Инициализирует треугольник с заданными сторонами.

        :param a: Длина первой стороны.
        :param b: Длина второй стороны.
        :param c: Длина третьей стороны.
        """
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """
        Вычисляет площадь треугольника по формуле Герона.

        :return: Площадь треугольника.
        """
        half_perimeter = (self.a + self.b + self.c) / 2
        return math.sqrt(
            half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c))

    def is_right_triangle(self) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным.

        :return: True, если треугольник прямоугольный, иначе False.
        """
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)


class Circle(Figure):
    """
    Класс для представления круга.

    Атрибуты:
        r (float): Радиус круга.
    """

    def __init__(self, r: float):
        """
        Инициализирует круг с заданным радиусом.

        :param r: Радиус круга.
        """
        self.r = r

    def area(self) -> float:
        """
        Вычисляет площадь круга.

        :return: Площадь круга.
        """
        return math.pi * self.r ** 2


def area_calculation(figure: Figure) -> float:
    """
    Вычисляет площадь фигуры.

    :param figure: Объект фигуры, реализующий метод `area`.
    :return: Площадь фигуры.
    """
    return figure.area()
