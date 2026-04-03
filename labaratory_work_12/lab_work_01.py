from math import cos, sin

__all__ = ['main']


def main():
    angle = float(input("Введите значение угла в радианах: "))

    print("Результаты функций:")
    print(1 - 0.25 * sin(2 * angle) ** 2 + cos(2 * angle))
    print(cos(angle) ** 2 + cos(angle) ** 4)


if __name__ == '__main__':
    main()
