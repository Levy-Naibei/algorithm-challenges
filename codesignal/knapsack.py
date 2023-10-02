"""
You found two items in a treasure chest! The first item weighs weight1
and is worth value1, and the second item weighs weight2 and is worth value2.
What is the total maximum value of the items you can take with you, assuming
that your max weight capacity is maxW and you can't come back for the items 
later? Note that there are only two items and you can't bring more than one
item of each type, i.e. you can't take two first items or two second items.
"""

def knapsack_light(value1, weight1, value2, weight2, maxW):
    max_value = 0
    if weight1 <= maxW:
        max_value = max(max_value, value1)

    if weight2 <= maxW:
        max_value = max(max_value, value2)

    if weight1 + weight2 <= maxW:
        max_value = max(max_value, value1 + value2)
        
    return max_value

print(knapsack_light(10, 5, 6, 4, 9)) # You're strong enough to take both of the items with you.
print(knapsack_light(5, 3, 7, 4, 6)) # You can't take both items, but you can take any of them.
        