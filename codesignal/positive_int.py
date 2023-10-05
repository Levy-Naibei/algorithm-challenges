"""
Given an integer product, find the smallest positive (i.e. greater than 0)
integer the product of whose digits is equal to product.
If there is no such integer, return -1 instead.
"""

def positive_int(product):
    # special case when product is 0, the smallest number is 10
    if product == 0:
        return 10
    
    # special case when product is 1, the smallest number is 1
    if product == 1:
        return 1
    
    result = 0
    factor = 9 # start with the largest digit

    while factor > 1:
        # checks if the current value of product is divisible evenly 
        # by the current value of factor.
        if product % factor == 0:
            # it appends this digit(factor) to the result by multiplying the 
            # current result by 10 (shifting the digits one place to the left)
            # and then adding the factor to it. This way, the number is
            # constructed digit by digit.
            result = result * 10 + factor
            # After appending the factor to the result, the product is divided
            # by the factor to reduce its value.
            product //= factor
        else:
            # current factor is not a factor of the product. In that case,
            # the value of factor is reduced by 1 and move on to check the
            # next smaller digit.
            factor -= 1

    # handles the case where there is no positive integer that can be obtained
    # by multiplying its digits to equal the given product
    if product > 1:
        return -1
    
    # reverse the digits in the result
    reversed_result = 0
    while result > 0:
        # calculate the last digit of the result using the modulo operator %.
        # This gives the remainder when result is divided by 10, effectively
        # extracting the last digit.
        digit = result % 10
        # appends the last digit (digit) to the reversed_result
        reversed_result = reversed_result * 10 + digit
        # removes the last digit from the result by performing integer division
        # by 10. This effectively removes the last digit from the result.
        result //= 10

    return reversed_result

print(positive_int(12))
