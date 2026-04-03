# импорт всего модуля
import my_module

print("--- импорт всего модуля ---")
print("Золотое сечение:", my_module.GOLDEN_RATIO)
print("Площадь круга r=5:", my_module.circle_area(5))
print("Площадь прямоугольника 3x4:", my_module.rectangle_area(3, 4))

# импорт конкретных элементов
from my_module import circle_perimeter, rectangle_perimeter

print("\n--- импорт конкретных элементов ---")
print("Периметр круга r=5:", circle_perimeter(5))
print("Периметр прямоугольника 3x4:", rectangle_perimeter(3, 4))

# импорт с переименованием
import my_module as mm
from my_module import rectangle_area as rect_a

print("\n--- импорт с переименованием ---")
print("Площадь круга r=3 (mm):", mm.circle_area(3))
print("Площадь прямоугольника 2x5 (rect_a):", rect_a(2, 5))

# импорт всех элементов (только то, что в __all__)
from my_module import *

print("\n--- импорт всех элементов ---")
print("Золотое сечение:", GOLDEN_RATIO)
print("Площадь круга r=7:", circle_area(7))
