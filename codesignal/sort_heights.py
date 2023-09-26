"""
Some people are standing in a row in a park. There are trees between 
them which cannot be moved. Your task is to rearrange the people 
by their heights in a non-descending order without moving the trees.
"""

def sort_height(heights):
    sorted_height = []
    for height in heights:
        if height != -1:
            sorted_height.append(height)
    
    ordered_height = sorted(sorted_height)

    h=0
    for i in range(len(heights)):
        # ensure that only people are considered for rearrangement
        if heights[i] != -1:
            heights[i] = ordered_height[h]
            h += 1

    return heights

print(sort_height([-1, 150, 190, 170, -1, -1, 160, 180]))