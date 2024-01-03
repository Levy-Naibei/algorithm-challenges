"""
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. 
There are a number of different toys lying in front of him, tagged with their prices.
Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. 
Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.
Note Each toy can be purchased only once.

maximumToys has the following parameter(s):
int prices[n]: the toy prices
int k: Mark's budget
Returns
int: the maximum number of toys

"""

def maximum_toys(prices, k):
    prices.sort()
    item_count = 0
    total_cost = 0
    for i in range(len(prices)):
        # inccrement the number of toys if within limit
        if total_cost + prices[i] <= k:
            total_cost += prices[i]
            item_count += 1
        else:
            break
    return item_count

print(maximum_toys([1, 12, 5, 111, 200, 1000, 10], 50))
print(maximum_toys([1, 2, 3, 4], 7))
