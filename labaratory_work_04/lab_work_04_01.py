import random

n = int(input("Введите длину масссива "))

masive = list()

for j in range (n):
    masive.append((round(random.uniform(-5, 5), 3)))

max = -6

for j in masive:
    if max <= abs(j): max = abs(j)

print("Массив до преобразования")
print(masive)

print(max)

a = float(input("Введите значения границы a "))

b = float(input("Введите значения границы b "))
buf_mas = masive
for i in buf_mas:
    n = 0

    if a <= abs(i) <= b:
        masive.remove(i)
        masive.append(0)
print("Массив после преобразования")


print(masive)