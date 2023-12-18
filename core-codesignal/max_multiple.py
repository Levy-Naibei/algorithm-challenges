"""
Given a divisor and a bound, find the largest integer N such that:
N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.
"""

def max_divisor(divisor, bound):
    # Calculate the largest multiple of divisor that is less than or equal to the bound
    return bound - (bound % divisor)

print(max_divisor(4, 15))