"""
Ratiorg got statues of different sizes as a present from CodeMaster 
for his birthday, each statue having an non-negative integer size. 
Since he likes to make things perfect, he wants to arrange them from
smallest to largest so that each statue will be bigger than 
the previous one exactly by 1. He may need some additional statues 
to be able to accomplish that. Help him figure out the minimum number 
of additional statues needed.
"""

def make_array_consecutive(statues):
    min_value = min(statues)
    max_value = max(statues)
    range_size = max_value - min_value + 1
    additional_size = range_size - len(set(statues))

    return additional_size

# Test data
print(make_array_consecutive([6, 2, 3, 8]))
