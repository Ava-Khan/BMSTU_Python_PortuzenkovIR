import random
from math import *

def funk(x,y,r):
    if x >= 0 and y >= 0 and sqrt(x ** 2 + y ** 2) <= r:
        return "Попадание"
    elif x <= 0 and y <= 0 and sqrt(x ** 2 + y ** 2) <= r:
        return "Попадание"
    elif x <= 0 and y >= 0 and y <= x + r:
        return "Попадание"

    else:
        return "Промах   "
r = float(input("Введите r "))

print("    X     Y    Res")
print("---------------------------")
for i in range(10):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)

    print(f"I {str(x)[:4]}  {str(y)[:4]} {str(funk(x,y,r))}    I")
print("---------------------------")