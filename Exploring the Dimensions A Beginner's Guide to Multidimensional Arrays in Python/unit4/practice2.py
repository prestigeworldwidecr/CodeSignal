'''

Oh no, Space Explorer! We were analyzing our board to identify empty spots for our game pieces, but something went awry. The current code isn't pinpointing the correct positions where a piece could move on its first turn. Could you help debug and fix this glitch so the spaceship can land smoothly on our next adventure? More specifically, your task is to find the positions of empty cells that neighbor to at least one other empty cell. In the given matrix, 'E' represents an empty cell, and 'P' represents a cell with a piece. For a specific cell, its neighboring cells are the cells directly above, below, to the left, and to the right.

'''

# Sample 'chessboard' with 'E' for empty and 'P' for a piece
board = [
        ['P', 'E', 'E', 'P'],
        ['E', 'P', 'E', 'P'],
        ['P', 'E', 'P', 'P'],
        ['P', 'E', 'P', 'E']
    ]

# Find and print positions where a piece can move in its first turn
def print_movable_positions(board) :
# {
    total_rows = len(board)
    total_columns = len(board[0])

    # print('i', 'j')
    # print('-', '-')

    for i in range(total_rows) :
    # {
        for j in range(total_columns) :
        # {
            # print(i, j)

            # The logical bug is in the condition that checks for the empty neighbors
            if (board[i][j] == 'E' and
                ((i > 0 and board[i - 1][j] == 'E') or
                (i < total_rows - 1 and board[i + 1][j] == 'E') or
                (j > 0 and board[i][j - 1] == 'E') or
                (j < total_columns - 1 and board[i][j + 1] == 'E'))) :

                print((i, j))
            # }

            else :
            # {
                None
            # }

        # }

    # }

# }
 
print_movable_positions(board)

'''

***** BONEYARD *****


def check_left(c) :
# {
    if (c - 1 < 0) :
    # {
        return False
    # }

    else :
    # {
        return True
    # }

# }

def check_right(c, total_columns) :
# {
    if (c + 1 >= total_columns) :
    # {
        return False
    # }

    else :
    # {
        return True
    # }

# }

def check_up(r) :
# {
    if (r - 1 < 0) :
    # {
        return False
    # }

    else :
    # {
        return True
    # }

# }

def check_down(r, total_columns) :
# {
    if (r + 1 >= total_columns) :
    # {
        return False
    # }

    else :
    # {
        return True
    # }

# }


'''