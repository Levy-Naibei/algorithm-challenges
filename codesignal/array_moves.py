"""
You are given an array of integers. On each move you are allowed
to increase exactly one of its element by one. Find the minimal 
number of moves required to obtain a strictly increasing 
sequence from the input.
"""

def min_moves(input_array):
    moves = 0

    for i in range(1, len(input_array)):
        if input_array[i] <= input_array[i - 1]:
            moves += input_array[i-1] - input_array[i] + 1
            input_array[i] = input_array[i-1] + 1
    return moves

print(min_moves([1, 1, 1]))
    