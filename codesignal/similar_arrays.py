"""
Two arrays are called similar if one can be obtained from another
by swapping at most one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.
"""

def similar_arrays(array_one, array_two):
    if array_two == array_one:
        return True
    
    # check number differences
    diffs = []
    for i in range(len(array_one)):
        if array_one[i] != array_two[i]:
            diffs.append(i)
    
    if len(diffs) == 2:
        i, j = diffs
        # swap
        if array_one[i] == array_two[j] and array_one[j] == array_two[i]:
            return True

    return False

print(similar_arrays([1, 2, 2], [2, 1, 1]))
print(similar_arrays([1, 2, 3], [2, 1, 3]))
