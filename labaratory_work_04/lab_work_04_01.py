# 1. Переименовать репозиторий проекта в соответствии с соглашением об именовании - репозиторий проекта
# и папка проекта должны иметь имя вида "BMSTU_Python_ФамилияИО" (ФамилияИО должно быть указано
# в латинской транскрипции).
# 2. Оформить и разместить в папке отчет о выполнении лабораторной работы в соответствии с шаблоном отчета
# о лабораторной работе (см. файл template_laboratory_report_00.ott) и методическими указаниями в нем.
# 3. Ограничить импортируемые функции только теми, что указаны в тексте программы.
# 4. Исправить текст программы в соответствии с требованиями Руководства по стилю кода Python
# (https://peps.python.org/pep-0008/).

import random


def main():
    n = int(input("Введите длину массива: "))

    array = [round(random.uniform(-5, 5), 3) for _ in range(n)]

    print("Массив до преобразования:")
    print(array)

    max_element = max(array)
    print(f"Максимальный элемент: {max_element}")

    last_positive_index = -1
    for i in range(len(array) - 1, -1, -1):
        if array[i] > 0:
            last_positive_index = i
            break

    sum_before = sum(array[:last_positive_index]) if last_positive_index != -1 else 0
    print(f"Сумма до последнего положительного: {sum_before}")

    a = float(input("Введите значение границы a: "))
    b = float(input("Введите значение границы b: "))

    i = 0
    removed_count = 0
    while i < len(array):
        if a <= abs(array[i]) <= b:
            array.pop(i)
            removed_count += 1
        else:
            i += 1
    array.extend([0] * removed_count)

    print("Массив после преобразования:")
    print(array)


if __name__ == "__main__":
    main()