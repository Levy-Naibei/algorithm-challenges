"""
Given five positive integers, find the minimum and maximum values 
that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of
two space-separated long integers.
"""

def mini_max_sum(arr):
    sorted_list=sorted(arr)
    total_sum = sum(arr)
    n = len(arr)
    print(total_sum - sorted_list[n-1], total_sum - sorted_list[0])

print(mini_max_sum([1, 3, 5, 7, 9]))
