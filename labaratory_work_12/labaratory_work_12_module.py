"""
Модуль с математическими операциями
"""

# import

PI = 3.14159


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b:
        raise ValueError("Деление на ноль")
    return a / b


if __name__ == "__main__":
    print(add(2, 30))
else:
    print("Модуль импортирован")