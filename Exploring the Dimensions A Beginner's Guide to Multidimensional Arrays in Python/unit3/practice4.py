'''

Great job on understanding matrix transformation! Now, it's time to apply that knowledge a bit more independently. Can you fill in the code to reflect the given matrix over its secondary diagonal?

Note that the secondary diagonal of the matrix is the line starting from the upper-right corner and ending in the bottom-left corner of the matrix. In the following matrix, we fill the elements in the secondary diagonal with 1s:

0 0 0 1
0 0 1 0
0 1 0 0
1 0 0 0

As an example, in a 4x4 matrix, reflecting the matrix over its secondary diagonal means that the elements matrix[0][0] and matrix[3][3] should be swapped, matrix[0][1] and matrix[2][3] should be swapped, etc. Elements in the secondary diagonal stay at the same place.

'''

import copy

def reflectOverSecondaryDiagonal(matrix) :
# {    
    new_matrix = copy.deepcopy(matrix)
    edge_length = len(matrix)
    edge_max_Y = edge_length

    new_matrix[0][0], new_matrix[edge_length -1][edge_length -1] = new_matrix[edge_length -1][edge_length -1], new_matrix[0][0]
    p = 1 # pivot column back to first column after processing first row

    for i in range(edge_length - 1) :
    # {
        for j in range(p, edge_max_Y - 1, 1) :
        # {
            print(edge_max_Y - 1, '(', i, ',', j, ')', '(', edge_length - i - 1, ',', edge_max_Y - 1, ')', edge_length - 1)  
            new_matrix[i][j], new_matrix[edge_length - i - 1][edge_max_Y - 1] = new_matrix[edge_length - i - 1][edge_max_Y - 1], new_matrix[i][j]
            
        # }

        edge_max_Y = edge_max_Y - 1
        p = 0

    # }

    return new_matrix
# }

# Example square matrix to reflect over the secondary diagonal
square_matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
                ]

square_matrix = [
                [1, 2, 3, 4],
                [4, 5, 6, 7],
                [8, 9, 10, 11],
                [12, 13, 14, 15]
                ]

square_matrix = [
                  [1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]
                ]

# Call the function and print the transformed matrix
# TODO: Call the function on square_matrix and store the result in transformed_matrix.

# print(reflectOverSecondaryDiagonal(square_matrix))
result = reflectOverSecondaryDiagonal(square_matrix)

for i in range(len(result)) :
# {
    print(result[i])
# }

# Output should be:
# [
#  [9, 6, 3],
#  [8, 5, 2],
#  [7, 4, 1]
# ]

'''

***** BONEYARD *****


            #1 flip diagonal
    
    #2 flip horizontally
            #   
            
            # if (i == 0) :
            # {
                # new_matrix[i][j], new_matrix[edge_max_Y - i - 1][j] = new_matrix[edge_max_Y - i - 1][j], new_matrix[i][j] 
            # }

            # else :
            # {
                # new_matrix[i][j], new_matrix[i][edge_max_Y - i + 1] = new_matrix[i][edge_max_Y - i + 1], new_matrix[i][j]
            # }
            






# print(i, j, edge_max_Y - i - 1, p) # (0, 1) -> (2, 1) | (1, 0) -> (1, 2)

                # print(matrix[i][j], matrix[edge_max_Y - i - 1][j])

# p = 0
            # print(i, j, matrix[i][j], matrix[i][edge_length - i])
            # 
            # matrix[i][j], matrix[i][edge_length - i] = matrix[i][edge_length - i], matrix[i][j] 
            # None

#3 flip horizontally
    # 3 passes, 1 flip diagonal, 2 flip horizontally, 3 flip horizontally

# print(i)
        # edge_max_Y = edge_max_Y - 1

        

edge_max_x = edge
    edge_max_y = edge

    for i in range(edge_max_x - 1) :
    # {
        # TODO: Complete the code to obtain the reflected square matrix in new_matrix.
        for j in range(edge_max_y - 1) :
        # {
            tmp = matrix[i][j]
            matrix[i][j] = matrix[i][edge - j - 1]
            matrix[i][edge - j - 1] = tmp
        # }

        edge_max_y = edge_max_y - 1

    # }

print("i\t", "j\t", "edge-j-1", "edge-i-1", "matrix[i][j]", "matrix[edge - j - 1][edge - i - 1]")

    
        # print('i', i, "edge_max_y", edge_max_y)

            # print(i, j, matrix[i][j], edge_max_x, edge_max_y)
            # print(i, '\t', j, '\t', edge - j - 1, '\t', edge - i - 1, '\t', matrix[i][j], '\t', matrix[edge - j - 1][edge - i - 1])
            # edge_max_y = edge_max_y - 1

# total_rows = len(matrix)
    # total_columns = len(matrix[0])
    

    # print(matrix)
    
    
    # new_matrix = [[0 for _ in range(size)] for _ in range(size)]



    # new_matrix = [0] * edge
    for j in range(edge) :
    # {
        new_matrix[j] = [0] * edge
    # }    

'''     