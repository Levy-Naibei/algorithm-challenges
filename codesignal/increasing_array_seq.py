"""
Given a sequence of integers as an array, determine whether 
it is possible to obtain a strictly increasing sequence by removing
no more than one element from the array.
"""


def array_sequence(input_array):
    removed = False
    n = len(input_array)

    for i in range(n - 1):
        if input_array[i] >= input_array[i + 1]:
            if removed:
                return False
            if i == 0 or input_array[i - 1] < input_array[i + 1]:
                removed = True
            elif i == n - 2 or input_array[i] < input_array[i + 2]:
                removed = True
            else:
                return False
    return True

print(array_sequence([[1, 3, 2]]))
