"""
You will be given an array of widths at points along the road (indices),
then a list of the indices of entry and exit points. Considering each entry and exit point pair, 
calculate the maximum size vehicle that can travel that segment of the service lane safely.
"""

def service_lane(width, cases):
    vehicles = []
    for i in range(0, len(cases)):
        """
        Each element in cases is a tuple, where the first element cases[i][0] 
        represents the starting index and the second element cases[i][1] represents the ending index.

        extracts a sub-list from the width list.
        It's using slicing to get elements from index cases[i][0] to cases[i][1] (inclusive/+1).
        finds the minimum value within the sub-list and appends to vehicles list.
        """
        vehicles.append(min(width[int(cases[i][0]):int(cases[i][1])+1]))

        # or vehicles = [min(width[start:end+1]) for start, end in cases]
        # instead of for loop and append
    return vehicles

print(service_lane([2,3,2,1], [[1,2], [2,4]]))
print(service_lane([2, 3, 1, 2, 3, 2, 3, 3], [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]))
