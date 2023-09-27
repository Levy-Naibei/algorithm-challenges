"""
Check if all digits of the given integer are even.
"""

def check_even_digits(num):
    for digit in str(num):
        # If the digit is not even, the function immediately returns False,
        # indicating that not all digits are even.
        if int(digit) % 2 != 0:
            return False
    return True

print(check_even_digits(248322))
