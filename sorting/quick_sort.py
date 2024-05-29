"""
Implement the Quick Sort algorithm to sort an array of integers in ascending order.
Write a function quick_sort(arr) that takes an array of integers as input and returns the sorted array.
"""


def quick_sort(arr):
    # If the array is empty or has only one element, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Initialize a stack with the initial range of the entire array (from 0 to len(arr) - 1).
    stack = [(0, len(arr) - 1)]

    # Process ranges on the stack until the stack is empty.
    while stack:
        # Pop the last range from the stack (LIFO order).
        # This gives the current sub-array to be processed.
        low, high = stack.pop()

        # If the range is valid (low index is less than high index), proceed with partitioning.
        if low < high:
            # Partition the array and get the pivot index.
            pivot_index = partition(arr, low, high)

            # Push the left sub-array range (from low to pivot_index - 1) onto the stack.
            stack.append((low, pivot_index - 1))

            # Push the right sub-array range (from pivot_index + 1 to high) onto the stack.
            stack.append((pivot_index + 1, high))

    # Return the sorted array.
    return arr


def partition(arr, low, high):
    # Select the last element of the current range as the pivot.
    pivot = arr[high]

    # Initialize the index of the smaller element.
    i = low - 1

    # Iterate over the range from low to high-1.
    for j in range(low, high):
        # If the current element is smaller than the pivot, swap it with the element at index i+1.
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at index i+1 to place the pivot in its correct position.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the index of the pivot.
    return i + 1


print(quick_sort([3, 6, 8, 10, 1, 2, 1]))


"""
In the iterative version of quicksort, we use a stack to keep track of the 
sub-array ranges (defined by their starting and ending indices) that need to be sorted.
 Each element in the stack is a tuple (low, high) where:
low is the starting index of the sub-array.
high is the ending index of the sub-array.

low, high = stack.pop()
This removes the last tuple (range) that was added to the stack and returns it.
This unpacks the tuple into two variables, low and high.

Initial Push:
stack = [(0, 6)] (since len(arr) - 1 is 6).
First Iteration:

low, high = stack.pop() unpacks the tuple (0, 6), so low = 0 and high = 6.
We then call partition(arr, low, high) to partition this range of the array.
"""