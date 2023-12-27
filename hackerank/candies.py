"""
"""
def candies(n, arr):
    candy = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i -1]:
            candy[i] = candy[i-1] + 1
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1] and candy[i] >= candy[i-1]:
            candy[i-1] = candy[i]+1
        
    return sum(candy)

# print(candies())
