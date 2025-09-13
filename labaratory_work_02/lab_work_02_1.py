import math

x = float(input("Введите x от -4 до 10"))

if x <= -2:
    print("X = ",x, "Y = ",x + 3)
elif (-2 < x <= 4):
    print("X = ",x, "Y = ",-0.5*x)
elif (4 < x <= 6):
    print("X = ",x, "Y = ",-2)
elif (6 < x <= 10):
    print("X = ",x, "Y = ",math.sqrt((4 - (x-8)**2))-2)
else:
    print("Вы ввели значение из неправильного диапазона")