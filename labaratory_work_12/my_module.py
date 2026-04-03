from math import sqrt

GOLDEN_RATIO = (1 + sqrt(5)) / 2

__all__ = ['GOLDEN_RATIO', 'circle_area', 'circle_perimeter', 'rectangle_area', 'rectangle_perimeter']


def circle_area(r):
    from math import pi
    return pi * r ** 2


def circle_perimeter(r):
    from math import pi
    return 2 * pi * r


def rectangle_area(a, b):
    return a * b


def rectangle_perimeter(a, b):
    return 2 * (a + b)


if __name__ == '__main__':
    print("Модуль запущен напрямую")
    print("Золотое сечение:", GOLDEN_RATIO)
    print("Площадь круга r=5:", circle_area(5))
    print("Периметр прямоугольника 3x4:", rectangle_perimeter(3, 4))
