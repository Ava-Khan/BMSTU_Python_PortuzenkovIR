import math

def funk(x):
    if x <= -2:
        return (x + 3)
    elif (-2 < x <= 4):
        return (-0.5*x)
    elif (4 < x <= 6):
        return (-2)
    elif (6 < x <= 10):
        return (math.sqrt((4 - (x-8)**2))-2)
    else:
        return ("Вы ввели значение из неправильного диапазона")


x_start = float(input("Введите точку начала от -4 до 10 "))
x_end = float(input("Введите точку конца от -4 до 10 "))
step = float(input("Введите шаг "))


if step <= 0:
    print("Вы указали неправильный шаг")

print("+--------+------------------------+")
print("I   X            I            Y   I")
print("+--------+------------------------+")

while x_start <= x_end:
    print("I{0: 7.2f}         I        {1: 7.2f} I".format(x_start, funk(x_start)))
    x_start += step

