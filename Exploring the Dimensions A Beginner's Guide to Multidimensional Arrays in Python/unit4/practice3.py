'''

Excellent progress, Space Voyager! Now, let's deepen our mastery. On a smaller game board, identify whether an element in a specific position has free space around, ensuring it is adjacent to at least one empty cell. Remember, adjacent cells are only the cells directly up, down, left, or right — not diagonally. Check only the neighboring cells, it doesn't matter if the current position is empty or it contains a piece.

'''

# Board game configuration: 'E' for empty, 'P' for piece
game_board = [
                ['E', 'P'],
                ['P', 'E']
            ]

# Function to check if a position is strategic
def is_position_strategic(board, row, col) :
# {

    # return ((row > 0 and board[row - 1][col] == 'E') or            ___)
    # TODO: Complete the remaining conditions for down, left, and right
    total_rows = len(game_board)
    total_columns = len(game_board[0])
    is_position_strategic = False

    if (row > 0 and board[row - 1][col] == 'E') :
    # {
        return True
    # }

    elif (row < total_rows and board[row + 1][col] == 'E') :
    # {
        return True
    # }

    elif (col > 0 and board[row][col - 1] == 'E') :
    # {
        return True
    # }

    elif (col < total_columns and board[row][col + 1] == 'E') :
    # {
        return True
    # }

    else :
    # {
        None
    # }

    return is_position_strategic

# }

# TODO: Check if position (0, 1) is strategic and print the result
print(is_position_strategic(game_board, 0, 1))

'''

***** BONEYARD *****

'''