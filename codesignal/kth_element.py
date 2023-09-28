"""
Given array of integers, remove each kth element from it.
"""

def remove_kth(input_list, k):
    result = []
    for i, ele in enumerate(input_list):
        # keep elements whose index is not a multiple of 'k'
        # (i + 1) beacuse index i starts from 0
        if (i + 1) % k != 0:
            result.append(ele)
    return result

print(remove_kth([1, 1, 1, 1, 1], 1))
print(remove_kth([1, 2, 1, 2, 1, 2, 1, 2], 2))
print(remove_kth([1, 2, 1, 2, 1, 2, 1, 2], 10))
print(remove_kth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
