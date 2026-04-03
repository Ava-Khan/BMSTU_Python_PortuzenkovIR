__all__ = ['is_even', 'factorial', 'digit_sum', 'clamp']


def is_even(n):
    return n % 2 == 0


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))


def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))
