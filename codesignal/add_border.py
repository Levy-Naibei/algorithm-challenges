"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
"""

def add_border_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    bordered_matrix = []

    bordered_matrix.append("*" * (cols + 2))
    
    for row in matrix:
        bordered_matrix.append("*" + row + "*")
    
    bordered_matrix.append("*" * (cols + 2))
    return bordered_matrix

print(add_border_matrix(
        ["abc",
        "ded"])
    )