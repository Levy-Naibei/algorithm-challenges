from math import isqrt

"""
Given a range of integers in list. return number of perfect squares
"""

def squares(a, b):
    low, high = isqrt(a), isqrt(b)
    square_count = 0
    for i in range(low, high + 1):
        if a <= i * i <= b:
            square_count += 1
    return square_count

print(squares(24, 49))
