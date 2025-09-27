from math import *

def ln(x, eps):
    step = 1000000
    n = 0
    val = 0
    while step >= eps:
        step = ((x**(2*n+1))/(2*n+1))
        val += step
        n += 1
    print(f"I   {x: 5.2f}   I   {val: 5.2f}  I  {n}  I")
print("+--------+--------+-----+")
print("I  X    I   Y    I   N I")


x_st = float(input("Введите точку начада из интервала (-1; 1)"))
x_end = float(input("Введите точку конца из интервала (-1; 1)"))
step = float(input("Введите шаг"))
eps = float(input("Введите значение ε погрешности"))

while x_st <= x_end:
    ln(x_st, eps)
    x_st += step


