"""
You are given an unordered array of unique integers incrementing from 1.
You can swap any two elements a limited number of times. 
Determine the largest lexicographical value array that can be created by 
executing no more than the limited number of swaps.
- return an array that represents the highest value permutation that can be formed.

largestPermutation has the following parameter(s):
int k: the maximum number of swaps
int arr[n]: an array of integers
"""

def largest_permutation(k, arr):
    n = len(arr)

    # Create a dictionary to store the index of each element
    index_map = {value: i for i, value in enumerate(arr)}
    
    for i in range(n):
        # If we have used all swaps, break the loop
        if k == 0:
            break
        
        # If the current element is not already in its correct position
        if arr[i] != n - i:
            # Get the index of the largest remaining element
            max_index = index_map[n-i]
            
            # Swap the current element with the maximum remaining value/element
            arr[i], arr[max_index] = arr[max_index], arr[i]
            
            # Update the index_map for the swapped elements
            index_map[arr[i]] = i
            index_map[arr[max_index]] = max_index
            
            # Decrease the number of remaining swaps
            k -= 1 
    
    return arr

print(largest_permutation(1, [3, 1, 2]))
print(largest_permutation(1, [4, 2, 3, 5, 1]))
