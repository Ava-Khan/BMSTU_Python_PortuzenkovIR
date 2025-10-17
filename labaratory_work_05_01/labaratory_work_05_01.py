from random import uniform
from math import sqrt



def generate_matrix(size):
    matr = list()
    for i in range(0, size):
        matr.append(list())
        for j in range(0, size):
            matr[i].append(round(uniform(-10, 10),2))

    return matr
a = generate_matrix(5)
print(a)

def sum_el(matr):
    sum = 0
    for i in range(0, len(matr)):
        flag = True
        buf = 0
        for j in range(0, len(matr)):
            if matr[j][i] < 0:
                flag = False
            buf += matr[j][i]
        buf = buf * flag
        sum += buf
    return sum

def min_sum_dig(matr):
    for i in range(0, len(matr)):
        for j in range(0, len(matr)):
            print()

print(sum_el(a))

