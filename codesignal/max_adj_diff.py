"""
Given an array of integers, find the maximal 
absolute difference between any two of its adjacent elements.
"""

def max_diff(input_list):
    max_diff = 0

    for i in range(len(input_list) -1):
        diff = abs(input_list[i] - input_list[i+1])
        max_diff = max(max_diff, diff)
    
    return max_diff
    
print(max_diff([2, 4, 1, 0]))
