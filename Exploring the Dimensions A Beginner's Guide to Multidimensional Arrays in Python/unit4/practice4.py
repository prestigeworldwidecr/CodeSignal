'''

Great job navigating the board so far, young Space Voyager! Now, let's challenge you a bit more. There's a magical spell (also known as "code") that allows you to inspect the chessboard for wise moves. Can you figure out the incantation (or code) that helps identify possible locations for a new piece, ensuring it has room to move in the next turn? Focus on checking the conditions for a spot to be deemed valid.

Good effort, but your function isn't quite checking the right conditions yet.

Make sure you:

Check if the current cell is empty before looking at neighbors.
Carefully check the correct neighbors (up, down, left, right) using the right indices.
Use a list comprehension to collect all valid positions.
Want to give it another shot or need a hint?

Cosmo
Yesterday
Read message aloud
Good effort, but your function has some boundary issues and you haven't used a list comprehension to print all valid move positions yet.

Want to try fixing those parts? Let me know if you need a hint!

Cosmo
Yesterday
Read message aloud
Good effort, but your function should return True or False, not a list. Also, you need to use a list comprehension to find all valid move positions on the board.

Want to try fixing those parts? Let me know if you need a hint!

Cosmo
2:21 AM
Read message aloud
Good effort, but your function isn't checking all four neighbors or if the cell is empty first. Also, try to return the list of valid positions instead of just printing True/False.

Want to give it another shot or need a hint?

'''

def evaluate_move(board, row, col) :
# {
    result = []
    
    # TODO: Check if a move to the given cell is possible; write a condition to check if the cell is empty.
    # Also, check if at least one neighboring cell is empty (not diagonally).
    if (board[row][col] == 'E') :
    # {
        if (row > 0) :
        # {
            if (board[row - 1][col] == 'E') :
            # {
                result.append((row - 1, col))
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

        if (row < total_rows - 1) :
        # {
            # print(row, col)

            if (board[row + 1][col] == 'E') :
            # {
                result.append((row + 1, col))
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

        if (col > 0) :
        # {
            if (board[row][col - 1] == 'E') :
            # {
                result.append((row, col - 1))
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

        if (col < total_columns - 1) :
        # {
            # print(i, j, row, col)
            
            if (board[row][col + 1] == 'E') :
            # {
                result.append((row, col + 1))
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