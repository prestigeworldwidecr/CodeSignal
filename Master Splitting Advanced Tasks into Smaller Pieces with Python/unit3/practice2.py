'''

You are tasked with creating a Python function named matrix_boundary_concatenation(). This function should accept two 2D matrices, matrix_A and matrix_B, and the number of boundary layers, n, to extract from both matrices.

In this context, a boundary layer refers to the elements that form the outer contour of a matrix. For instance, the first layer of the following 4x4 matrix includes the elements 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, and 5:

[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

Your function should extract the first n boundary layers from both matrix_A and matrix_B. It should then concatenate these extracted layers into a new array, ensuring that the layers from matrix_A precede those from matrix_B in the resultant array.

The matrices A and B will be square matrices, with each side's length ranging from 1 to 10. The number of layers n will be less than or equal to the side length of the square matrices.

The function signature should be:

def matrix_boundary_concatenation(matrix_A, matrix_B, n):

The elements in the input matrices can be any integer between -100 and 100.

Example

Consider the following input to our function:

matrix_A = [[1, 2, 3, 4], 
            [5, 6, 7, 8], 
            [9, 10, 11, 12], 
            [13, 14, 15, 16]]

matrix_B = [[17, 18, 19, 20], 
            [21, 22, 23, 24], 
            [25, 26, 27, 28], 
            [29, 30, 31, 32]]
n = 2

Our function matrix_boundary_concatenation(matrix_A, matrix_B, n) should return:

[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10, 17, 18, 19, 20, 24, 28, 32, 31, 30, 29, 25, 21, 22, 23, 27, 26]

Explanation:

In matrix_A, the first boundary layer is composed of the elements 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, and 5, taken in a clockwise direction from the top-left corner. Our second layer then includes the elements 6, 7, 11, and 10.

For matrix_B, the corresponding boundary layers include the elements 17, 18, 19, 20, 24, 28, 32, 31, 30, 29, 25, 21 for the first layer and 22, 23, 27, 26 for the second one.

The function outputs an array where the extracted layers from matrix_A are followed by those from matrix_B.

'''

def one_loop(matrix, top_left, bottom_right) :
# {
    min_x = top_left[0]
    min_y = top_left[1]
    max_x = bottom_right[0]
    max_y = bottom_right[1]
    result = []
    x = min_x
    y = min_y

    # print(min_x, min_y, max_x, max_y)
    result.append(matrix[x][y])

    # right
    while(y < max_y - 1) :
    # {
        y = y + 1
        result.append(matrix[x][y])
    # }

    # down
    while(x < max_x - 1) :
    # {
        x = x + 1
        result.append(matrix[x][y])
    # }

    # left
    while(y > min_y) :
    # {
        y = y - 1
        result.append(matrix[x][y])
    # }
    
    # up
    while(x > min_x + 1) :
    # {
        x = x - 1
        result.append(matrix[x][y])
    # }

    # print(result)
    
    return result

# }

def matrix_boundary_concatenation(matrix_A, matrix_B, n) :
# {
    a_min_x = 0
    a_min_y = 0
    a_max_x = len(matrix_A)
    a_max_y = len(matrix_A[0])
    b_min_x = 0
    b_min_y = 0
    b_max_x = len(matrix_B)
    b_max_y = len(matrix_B[0])
    run_a = []
    run_b = []
    a = 0
    b = 0

    while (a < n) :
    # {
        run_a = run_a + one_loop(matrix_A, (a_min_x, a_min_y), (a_max_x, a_max_y))
        a_min_x = a_min_x + 1
        a_min_y = a_min_y + 1
        a_max_x = a_max_x - 1
        a_max_y = a_max_y - 1
        # print((a_min_x, a_min_y), (a_max_x, a_max_y))
        a = a + 1
    # }

    while (b < n) :
    # {
        run_b = run_b + one_loop(matrix_B, (b_min_x, b_min_y), (b_max_x, b_max_y))
        b_min_x = b_min_x + 1
        b_min_y = b_min_y + 1
        b_max_x = b_max_x - 1
        b_max_y = b_max_y - 1
        b = b + 1
    # }

    return run_a + run_b
# }

def solution(matrix_A, matrix_B, n) :
# {
    # TODO: implement the function that extracts 'n' boundary layers from matrix_A and matrix_B,
    # merges them into a single array and then returns this new array.
    return matrix_boundary_concatenation(matrix_A, matrix_B, n)
# }

matrix_A = [[1, 2, 3, 4], 
            [5, 6, 7, 8], 
            [9, 10, 11, 12], 
            [13, 14, 15, 16]]

matrix_B = [[17, 18, 19, 20], 
            [21, 22, 23, 24], 
            [25, 26, 27, 28], 
            [29, 30, 31, 32]]

n = 2

print(solution(matrix_A, matrix_B, n))

'''

***** BONEYARD *****



'''