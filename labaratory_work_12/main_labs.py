import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

# импорт из лабы 1
import lab_work_01
print("--- лаба 1 ---")
lab_work_01.main()

# импорт конкретного элемента из лабы 4
from lab_work_04 import main as lab04_main
print("\n--- лаба 4 ---")
lab04_main()

# импорт нескольких элементов из лабы 5
from lab_work_05 import generate_matrix, sum_el, min_sum_dig
print("\n--- лаба 5 ---")
n = int(input("Введите размер матрицы: "))
matrix = generate_matrix(n)
for row in matrix:
    print(' '.join(f'{elem:7.2f}' for elem in row))
sum_el(matrix)
min_sum_dig(matrix)
