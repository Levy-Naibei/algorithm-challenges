"""
Given n and firstNumber, find the number which is written 
in the radially opposite position to firstNumber.
"""

def find_opposite_number(n, firstNumber):
    # firstNumber + n // 2: This calculates the position of the point 
    # that is diametrically opposite to firstNumber
    # The modulus operator % n is used to ensure that the result wraps around within the circle. 
    # For example, if firstNumber is 8 and n is 10, the opposite position would be (8 + 5) % 10 = 3.
    return (firstNumber + n // 2) % n

print(find_opposite_number(10, 8))
