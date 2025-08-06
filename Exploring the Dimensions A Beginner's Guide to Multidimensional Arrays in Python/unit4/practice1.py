'''
Fantastic journey through the game board you've had! Now it's your turn to modify the code. Adjust our function so that it identifies potential positions for a new piece, based solely on its ability to move left or right. We're simplifying our search to horizontal moves only, aligning with our focus on multidimensional arrays. Modify the code accordingly and observe the difference.

'''

# Function to check if a neighboring position is empty ('E')
def is_empty_neighbor(board, x, y) :
# {
    # rows, cols = len(board), len(board[0])
    total_rows = len(board)
    total_columns = len(board[0])

    # Check that (x, y) is within board boundaries
    if (0 <= x < total_rows and 0 <= y < total_columns) :
    # {
        return board[x][y] == 'E'
    # }

    else :
    # {
        None
    # }

    return False

# }

def main() :
# {
    board = [
                ['P', 'E', 'E', 'P'],
                ['E', 'P', 'E', 'P'],
                ['P', 'E', 'P', 'P'],
                ['P', 'E', 'P', 'E']
            ]
    
    result = []
    # rows, cols = len(board), len(board[0])
    total_rows = len(board)
    total_columns = len(board[0])

    for i in range(total_rows) :
    # {
        for j in range(total_columns) :
        # {
            if (board[i][j] == 'E') and (is_empty_neighbor(board, i, j - 1) or is_empty_neighbor(board, i, j + 1)):

                result.append((i, j))
            # }

            else :
            # {
                None
            # }

        # }

    # }

    print(result)

    # }

# }

if (__name__ == "__main__") :
# {    
    main()
# }

else :
# {
    None    
# }

'''

***** BONEYARD *****

(is_empty_neighbor(board, i - 1, j) or is_empty_neighbor(board, i + 1, j) or   is_empty_neighbor(board, i, j - 1) or is_empty_neighbor(board, i, j + 1))

# Check for empty spot with an empty neighbor on four directions
            

'''