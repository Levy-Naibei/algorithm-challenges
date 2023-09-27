"""
Given an array of integers, replace all the 
occurrences of elemToReplace with substitutionElem.
"""

def list_replace(input_list, elemToReplace, substitutionElem):
    result = []
    for i in range(len(input_list)):
        if input_list[i] == elemToReplace:
            result.append(substitutionElem)
        else:
            result.append(input_list[i])
    return result

print(list_replace([1, 2, 1], 1, 3))