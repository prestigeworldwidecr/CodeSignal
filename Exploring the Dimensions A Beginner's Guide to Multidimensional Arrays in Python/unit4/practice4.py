'''

Great job navigating the board so far, young Space Voyager! Now, let's challenge you a bit more. There's a magical spell (also known as "code") that allows you to inspect the chessboard for wise moves. Can you figure out the incantation (or code) that helps identify possible locations for a new piece, ensuring it has room to move in the next turn? Focus on checking the conditions for a spot to be deemed valid.

'''

def evaluate_move(board, row, col) :
# {
    result = False
    
    # TODO: Check if a move to the given cell is possible; write a condition to check if the cell is empty.
    # Also, check if at least one neighboring cell is empty (not diagonally).
    if (row > 0) :
    # {
        if (board[row - 1][col] == 'E') :
        # {
            return True
        # }

        else :
        # {
            None
        # }
        
    # }

    elif (row < total_rows) :
    # {
        if (board[row + 1][col] == 'E') :
        # {
            return True
        # }

        else :
        # {
            None
        # }
    # }

    elif (col > 0) :
    # {
        if (board[row][col - 1] == 'E') :
        # {
            return True
        # }

        else :
        # {
            None
        # }

    # }

    elif (col < total_columns) :
    # {
        if (board[row][col + 1] == 'E') :
        # {
            return True
        # }

        else :
        # {
            None
        # }
        
    # }

    else :
    # {
        None
    # }

    return result

# }

# Assuming a constant 2D array representing a board
board = [
            ['P', 'E', 'E', 'P'],
            ['E', 'P', 'E', 'P'],
            ['P', 'E', 'P', 'P'],
            ['P', 'E', 'P', 'E']
        ]

# TODO: Write a list comprehension to find all valid move positions.
valid_moves = []
total_rows = len(board)
total_columns = len(board[0])

for i in range(total_rows) :
# {
    for j in range(total_columns) :
    # {
        if (board[i][j] == 'E') :
        # {
            valid_moves.append((i, j))
        # }

        else :
        # {
            None
        # }

    # }

# }

for i in range(len(valid_moves)) :
# {
    print(evaluate_move(board, valid_moves[i][0], valid_moves[i][1]))
# }

'''

***** BONEYARD *****



    # }

    else :
    # {
        None
    # }

# print(valid_moves[0][1])
# print(evaluate_move(board, 1, 2))
# print('(', valid_moves[i][0], ',', valid_moves[i][1], ')')
    

'''