"""
Given array of integers, find the maximal possible 
sum of some of its k consecutive elements.
"""

def max_consecutive(input_list, k):
    n = len(input_list)

    if k > n:
        return 0
    
    max_sum=sum(input_list[:k]) # initial max sum of first k elements
    current_sum = max_sum

    # sliding window appproach
    for i in range(k, n):
        current_sum = current_sum - input_list[i - k] + input_list[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

print(max_consecutive([2, 4, 10, 1], 2))
print(max_consecutive([2, 3, 5, 1, 6], 2))
print(max_consecutive([1, 3, 2, 4], 3))
