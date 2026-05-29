"""
Модуль с математическими операциями
"""

# import

PI = 3.14159
__all__ = ['add', 'multiply']

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
    print(__name__)
    print(add(2, 30))
else:
    print(__name__)
    print("Модуль импортирован")