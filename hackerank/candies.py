"""
Alice is a kindergarten teacher. She wants to give some candies to the children in her class. 
All the children sit in a line and each of them has a rating score according to his or her performance in the class. 
Alice wants to give at least 1 candy to each child. If two children sit next to each other, 
then the one with the higher rating must get more candies.
Alice wants to minimize the total number of candies she must buy.
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

print(candies(3, [1, 2, 2]))
print(candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
print(candies(8, [2, 4, 3, 5, 2, 6, 4, 5]))
