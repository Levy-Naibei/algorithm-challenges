"""
Let's define digit degree of some positive integer as the number of times
we need to replace this number with the sum of its digits until we get to
a one digit number. Given an integer, find its digit degree.
"""

def find_digit_degree(n):
    def digit_sum(num):
        return sum(int(digit) for digit in str(num))
    
    degree = 0
    while n >= 10:
        n = digit_sum(n)
        degree += 1
    return degree

print(find_digit_degree(99))
