"""
Given array arr=[1,4,2,10,23,3,1,0,20]
k = 4
Find maximum sum of subarray with O(N) time complexity
"""

def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1
    
    # sum of first window
    window_sum = sum(arr[:k])

    # initialize max sum as the first window's sum
    max_sum = window_sum

    # compute the sums of remaining windows by removing first element of previous
    # window and adding last element of the current window
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum

print(max_sum_subarray([1,4,2,10,23,3,1,0,20], 4))

"""
This technique is efficient because it avoids recalculating the sum of the
entire subaaray each time window moves; instead, it updates the sum by considering 
only the elements that are entering and leaving the window. 
This reduces the time complexity from O(n^2) to O(n)
"""
