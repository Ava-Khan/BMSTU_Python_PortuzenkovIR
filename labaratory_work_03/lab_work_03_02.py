# 1. Переименовать репозиторий проекта в соответствии с соглашением об именовании - репозиторий проекта
# и папка проекта должны иметь имя вида "BMSTU_Python_ФамилияИО" (ФамилияИО должно быть указано
# в латинской транскрипции).
# 2. Оформить и разместить в папке отчет о выполнении лабораторной работы в соответствии с шаблоном отчета
# о лабораторной работе (см. файл template_laboratory_report_00.ott) и методическими указаниями в нем.
# 3. Исправить текст программы в соответствии с требованиями Руководства по стилю кода Python
# (https://peps.python.org/pep-0008/).
# 4. Ограничить импортируемые функции только теми, что указаны в тексте программы.
# 5. В отчете пояснить использование f-строк.

import random
from math import sqrt


def check_hit(x, y, r):
    in_first_quarter = x >= 0 and y >= 0 and sqrt(x ** 2 + y ** 2) <= r
    in_third_quarter = x <= 0 and y <= 0 and sqrt(x ** 2 + y ** 2) <= r
    in_second_quarter = x <= 0 and y >= 0 and y <= x + r

    if in_first_quarter or in_third_quarter or in_second_quarter:
        return "Попадание"
    else:
        return "Промах"


def main():
    r = float(input("Введите r: "))

    print("    X       Y      Res")
    print("---------------------------")

    for _ in range(10):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        result = check_hit(x, y, r)
        print(f"I {x:6.2f}  {y:6.2f}  {result:10} I")

    print("---------------------------")


if __name__ == "__main__":
    main()