"""
Given a matrix, find the sum of elements whose value 
does not appear below column with 0 value
"""


def matrix_ele_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_sum = 0

    for col in range(cols):
        is_suitable = True
        for row in range(rows):
            if matrix[row][col] == 0:
                is_suitable = False
            if is_suitable:
                total_sum += matrix[row][col]

    return total_sum


print(matrix_ele_sum([[1, 1, 1, 0],
                      [0, 5, 0, 1],
                      [2, 1, 3, 10]]
                    ))
