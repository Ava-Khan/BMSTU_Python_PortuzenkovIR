from random import uniform


def generate_matrix(size):
    matr = list()
    for i in range(0, size):
        matr.append(list())
        for j in range(0, size):
            matr[i].append(round(uniform(-10, 10), 2))
    return matr


def sum_el(matr):
    sum = 0
    for i in range(0, len(matr)):
        flag = True
        buf = 0
        for j in range(0, len(matr)):
            if matr[j][i] < 0:
                flag = False
            buf += matr[j][i]
        if flag:
            sum += buf
            print(f"Столбец {i}: сумма = {buf:.2f}")
    return sum


def min_sum_dig(matr):
    n = len(matr)
    min_sum = float('inf')
    for k in range(0, 2 * n - 1):
        current_sum = 0
        for i in range(0, n):
            j = k - i
            if j >= 0 and j < n:
                current_sum += abs(matr[i][j])
        if current_sum < min_sum and current_sum > 0:
            min_sum = current_sum
        print(f"Диагональ i+j={k}: сумма модулей = {current_sum:.2f}")
    return min_sum


def main():
    n = int(input("Введите размер матрицы "))
    a = generate_matrix(n)

    print("Матрица:")
    for row in a:
        print(' '.join(f'{elem:7.2f}' for elem in row))

    print("\n1. Сумма элементов в столбцах без отрицательных элементов:")
    sum_result = sum_el(a)
    print(f"Общая сумма: {sum_result:.2f}")

    print("\n2. Минимум среди сумм модулей элементов диагоналей:")
    min_result = min_sum_dig(a)
    print(f"Минимальная сумма: {min_result:.2f}")


if __name__ == "__main__":
    main()