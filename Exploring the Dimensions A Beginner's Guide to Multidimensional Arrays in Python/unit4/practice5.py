'''

Your coding quest is nearly complete! Here's one final challenge: Write a Python function to count how many 3x3 submatrices in a given matrix have 'E's in all four corners. Remember, each 3x3 submatrix is like a smaller square within the larger matrix. Are you ready to apply what you've learned and show off your skills?

'''

def count_submatrices_with_e(board) :
# {
    # TODO: Initialize a count variable to keep track of how many submatrices meet the criteria
    total_submatrix = 0

    # TODO: Use a nested loop to go through each element in the matrix that can be the top-left corner of a 3x3 submatrix
    for i in range(len(board) - 2):
    # {
        for j in range(len(board) - 2) :
        # {
            # print((i, j), board[i][j], total_submatrix)
            
            # TODO: Check if the current 3x3 submatrix has 'E's in all four corners
            # If it does, increment the count
            if (board[i][j] == 'E' and board[i][j + 2] == 'E' and board[i + 2][j] == 'E' and 
                board[i + 2][j + 2] == 'E') :
            # {
                total_submatrix = total_submatrix + 1
            # }

            else :
            # {
                None
            # }

        # }

    # }

    # TODO: Return the count of submatrices that meet the criteria
    return total_submatrix
# }

# TODO: Define a matrix 'board' with some 'E's and 'P's, representing empty and piece positions respectively
board = [
            ['P', 'E', 'E', 'E'],
            ['E', 'P', 'E', 'P'],
            ['P', 'E', 'P', 'E'],
            ['E', 'E', 'E', 'E']
        ]

# TODO: Call the function to count the submatrices and print the result
print(count_submatrices_with_e(board))

'''

***** BONEYARD *****

submatrix = [0] * 3
    
    for i in range(len(submatrix)) :
    # {
        submatrix[i] = [0] * 3
    # }

'''