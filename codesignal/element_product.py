"""
Given an array of integers, find the pair of adjacent elements 
that has the largest product and return that product.
"""


def adjacent_ele_prod(input_array):
    pair = []
    for i in range(1, len(input_array)):
        max_prod = input_array[i] * input_array[i - 1]
        pair.append(max_prod)

    return max(pair)


print(adjacent_ele_prod([3, 6, -2, -5, 7, 3]))
