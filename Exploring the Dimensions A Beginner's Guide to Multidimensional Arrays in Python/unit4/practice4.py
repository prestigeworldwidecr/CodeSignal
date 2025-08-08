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

Good try, but your function should return True or False, not a list, and you need to use a list comprehension to collect all valid positions.

Want to try adjusting your approach? Let me know if you need a hint!

Sure! Here are a couple of small hints:

First, check if the cell at (row, col) is empty ('E').
Then, look at its neighbors: up (row-1, col), down (row+1, col), left (row, col-1), and right (row, col+1). Make sure you don't go out of bounds!
If at least one neighbor is also empty, that's a valid move.
How would you check each neighbor safely

Exactly! Those checks help you avoid going out of bounds when looking at neighbors.

Now, for each direction:

Use these conditions before accessing a neighbor.
Then, check if that neighbor is 'E'.
Can you combine these checks to see if at least one neighbor is empty?

You’re on the right track with your neighbor checks! A few tips:

You only need to add (row, col) to your result if at least one neighbor is empty—not the neighbor’s coordinates.
Try to simplify: use or to check all four neighbors, and if any are empty, add (row, col).
Can you rewrite your logic so you only append (row, col) when the current cell is empty and at least one neighbor is empty

'''

def evaluate_move(board, row, col) :
# {
    # TODO: Check if a move to the given cell is possible; write a condition to check if the cell is empty.
    # Also, check if at least one neighboring cell is empty (not diagonally).
    if (board[row][col] == 'E') :
    # {
        # print((row, col))

        if (row > 0 and board[row - 1][col] == 'E') :
        # {
            return True
        # }

        elif (row < total_rows - 1 and board[row + 1][col] == 'E') :
        # {
            return True
        # }

        elif (col > 0 and board[row][col - 1] == 'E') :
        # {
            return True
        # }

        elif (col < total_columns - 1 and board[row][col + 1] == 'E') :
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

    return False

# }

# Assuming a constant 2D array representing a board
board = [
            ['P', 'E', 'E', 'P'],
            ['E', 'P', 'E', 'P'],
            ['P', 'E', 'P', 'P'],
            ['P', 'E', 'P', 'E']
        ]

# TODO: Write a list comprehension to find all valid move positions.
empty_spaces = []
valid_moves = []
total_rows = len(board)
total_columns = len(board[0])

for i in range(total_rows) :
# {
    for j in range(total_columns) :
    # {
        if (board[i][j] == 'E') :
        # {
            empty_spaces.append((i, j))
        # }

        else :
        # {
            None
        # }

    # }

# }

for i in range(len(empty_spaces)) :
# {
    row = empty_spaces[i][0]
    col = empty_spaces[i][1]

    if (evaluate_move(board, row, col)) :
    # {
        valid_moves.append((row, col))
    # }

    else :
    # {
        None
    # }
    
# }

print(valid_moves)

'''

***** BONEYARD *****

# print(evaluate_move(board, empty_spaces[i][0], empty_spaces[i][1]))
    

if (0 < row and row < total_rows - 1 and 0 < col and col < total_columns - 1) :
        # {
            print(row, col)
            
            if (board[row - 1][col] == 'E' or board[row + 1][col] == 'E' or board[row][col - 1] == 'E' or board[row][col + 1] == 'E') :
            # {
                # result.append((row, col))
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

# result = []
    
    

    # }

    else :
    # {
        None
    # }

# print(valid_moves[0][1])
# print(evaluate_move(board, 1, 2))
# print('(', valid_moves[i][0], ',', valid_moves[i][1], ')')
    
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

'''