import random

n = int(input("Введите длину массива: "))

masive = [round(random.uniform(-5, 5), 3) for _ in range(n)]

print("Массив до преобразования:")
print(masive)

max_element = max(masive)
print(f"Максимальный элемент: {max_element}")

last_pos_idx = -1
for i in range(len(masive)-1, -1, -1):
    if masive[i] > 0:
        last_pos_idx = i
        break

sum_before = sum(masive[:last_pos_idx]) if last_pos_idx != -1 else 0
print(f"Сумма до последнего положительного: {sum_before}")


a = float(input("Введите значение границы a: "))
b = float(input("Введите значение границы b: "))

i = 0
removed_count = 0
while i < len(masive):
    if a <= abs(masive[i]) <= b:
        masive.pop(i)
        removed_count += 1
    else:
        i += 1
masive.extend([0] * removed_count)

print("Массив после преобразования:")
print(masive)