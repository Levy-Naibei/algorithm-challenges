"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""

def diagonal_difference(arr):
    rows = len(arr)
    pri_sum = 0
    sec_sum = 0
    
    # Traversing through the rows of a matrix
    for row in range(rows):
        # Adding the principal Diagonal element of the current row
        pri_sum += arr[row][row]

        # Secondary diagonal condition(row -1 because index starts from 0)
        sec_sum += arr[row][rows - row -1]
    
    diag_diff = abs(pri_sum - sec_sum)
    return diag_diff

print(diagonal_difference( 
    [ [11, 2, 4], 
      [4, 5, 6 ],
      [10, 8, -12]
    ]
))

print(diagonal_difference(
    [
        [5, 1, 3],
        [9, 6, 8],
        [4, 2, 7]
    ]
))
