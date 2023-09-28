"""
Find the leftmost digit that occurs in a given string.
"""

def left_most_digit(input_string):
    for char in input_string:
        if char.isdigit():
            return char
    return None

print(left_most_digit("var_1__Int"))
print(left_most_digit("q2q-q"))
