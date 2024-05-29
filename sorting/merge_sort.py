"""
You are given an array of integers.
Write a function to sort the array using the Merge Sort algorithm. 
Your function should return a new sorted array.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # mid point
    mid = len(arr) // 2

    # divide the unsorted list by slicing
    left = arr[:mid]
    right = arr[mid:]

    # recursively sort the sub-lists
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # merge sorted sub-lists
    return merge(sorted_left, sorted_right)


def merge(left, right):
    sorted_list = []

    # pointers to track current index/position in the sub-lists
    i, j = 0, 0

    # merge the sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # if there are remaining elements in left sub array, add them
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    # if there are remaining elements in right sub array, add them
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))

"""
Steps of Merge Sort:
Divide:
The array is split into two halves using slicing.
The middle index is calculated as mid = len(arr) // 2

Conquer:
The merge_sort function is called recursively on each half.
This process continues until the base case is reached (arrays of length 1 or 0).

Combine:
The merge function is used to merge two sorted arrays into one sorted array.
- It uses two pointers, i and j, to track the current position in the left 
and right arrays, respectively.
- Elements are compared, and the smaller element is appended to the result array.
- If one of the arrays is exhausted before the other, the remaining elements of 
the other array are appended to the result.
Complexity:
Time Complexity: 
 O(nlogn)
The array is divided into two halves logn times.
Each level of recursion involves merging n elements.
Space Complexity: O(n)
Additional space is required to store the divided halves and the merged array.
Merge Sort is particularly useful for large datasets and is stable, 
meaning it preserves the relative order of equal elements. However, 
its space complexity can be a disadvantage compared to in-place sorting algorithms like Quick Sort.
"""
