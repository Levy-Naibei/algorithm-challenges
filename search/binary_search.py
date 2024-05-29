def bin_search(arr, target):
    left, right = 0, len(arr) - 1

    # Note: ensure the array is sorted

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # If the target value is not found
    return -1

print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],7))
            