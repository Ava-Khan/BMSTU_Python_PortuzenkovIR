__all__ = ['reverse_str', 'count_vowels', 'is_palindrome', 'repeat']


def reverse_str(s):
    return s[::-1]


def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiouаеёиоуыэюя')


def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]


def repeat(s, n):
    return s * n
