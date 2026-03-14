def apple_division(n, k):
    """n школьников делят между собой k яблок поровну,
     остаток в корзине оставляется"""
    return (k // n, k % n)


def table_tennis(a, b ,c):
    return ((c - a)//b)


def predposled_number(num):
    return (num // 10 % 10)


def sum_digit(num):
    return (num//1000 + num//100%10 + num//10%10 + num%10)


def el_clock(minutes):
    return (minutes//60, minutes%60)


def len_cep(d, r, n):
    return (2*n*(d+r))


def autoprobeg(n, m):
    return ((n+m-1)//n)


def parti(a, b, c):
    return ((a+1)//2 + (b+1)//2 + (c+1)//2)


def books_page(k, n):
    return ((n-1)//k + 1, (n-1)%k + 1)


def chess(n, m):
    return ((n*m+1)//2)


def next_num(n):
    return (n + 2 - n%2)

def sim(n):
    rev = (n%10)*1000 + (n//10%10)*100 + (n//100%10)*10+n//1000
    return (1 // ((n - rev)**2 + 1))


def maximum(a, b):
    return ((a // b * a + b // a * b) // (a // b + b // a))
    # Однако у этого решения есть 1 минус, он работает только с натуральными числами


    # Если дать разрешение на битовые операции, то можно реализовать и для целых чисел
    # diff = a - b
    # mask = diff >> 63
    # abs_diff = diff ^ mask - mask
    # return ((a+b-abs_diff)//2)

print(maximum(5, 19))

