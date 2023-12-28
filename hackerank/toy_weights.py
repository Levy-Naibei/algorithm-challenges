"""
Priyanka works for an international toy company that ships by container. 
Her task is to the determine the lowest cost way to combine her orders for shipping. 
She has a list of item weights. The shipping company has a requirement that all items 
loaded in a container must weigh less than or equal to 4 units plus the weight of 
the minimum weight item. All items meeting that requirement will be shipped in one container.
What is the smallest number of containers that can be contracted to ship the items based 
on the given list of weights?

sample input:
[1, 2, 3, 21, 7, 12, 14, 21]

The first container holds items weighing 1,  2 and 3. (weights in range 1...5 )
The second container holds the items weighing 21  units. (21....25)
The third container holds the item weighing 7  units. (7...11)
The fourth container holds the items weighing  12 and  14 units. (12...14)
 4 containers are required.
"""

def toys(w):
    # sort the weights
    w.sort()
    containers = 0
    i = 0

    while i < len(w):
        # Increment the container count
        containers += 1
        # Get the minimum weight in the current container
        min_weight = w[i]

        # Iterate through the remaining weight in the current container
        while i < len(w) and w[i] <= min_weight + 4:
            i += 1

    return containers

print(toys([1, 2, 3, 21, 7, 12, 14, 21]))
