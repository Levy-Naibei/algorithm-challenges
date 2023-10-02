"""
Given the positions of a white bishop and a black pawn on the standard chess board,
determine whether the bishop can capture the pawn in one move. The bishop has no
restrictions in distance for each move, but is limited to diagonal movement.
Check out the example below to see how it can move:
"""

def chess_board(bishop, pawn):
    def get_indices(position):
        col, row = ord(position[0]) - ord("a"), int(position[1]) - 1
        return row, col

    bishop_col, bishop_row = get_indices(bishop)
    pawn_col, pawn_row = get_indices(pawn)

    return abs(bishop_col - pawn_col) == abs(bishop_row - pawn_row)

print(chess_board("a1", "c3"))
print(chess_board("h1", "h3"))
print(chess_board("e2", "f3"))
