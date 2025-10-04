'''

Warren, an innovator in mathematical problems, challenges you to solve a complex task involving matrix manipulation. He provides you with a 2D matrix, M, with dimensions m x n, where m and n range from 1 to 500, inclusive. Each element in the matrix ranges from -100 to 100, inclusive.

Warren further provides you with the coordinates describing two sub-matrices within M, denoted as S1 and S2. He asks you to write a Python function, say submatrix_swap(), which takes as inputs the matrix M and the coordinates specifying the sub-matrices S1 and S2. This function is required to swap the positions of S1 and S2 within M and return the newly formed matrix M'.

The swapping of sub-matrices is subject to the following constraints:

The sub-matrices do not overlap.
S1 and S2 must have identical dimensions, i.e., the number of rows and columns in S1 must equal the number of rows and columns in S2.
The coordinates of each submatrix are given by 4 coordinates – [row_l, row_r, col_l, col_r] – which correspond to a valid submatrix with rows in [row_l, row_r) and columns in [col_l, col_r).
Note: All coordinates use 0-indexing (following standard Python list slicing).

Example

Let's consider an example to clarify the task. Suppose M is:

Python
Copy to clipboard
M = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25]]
With sub-matrix S1 defined by the coordinates [0, 2, 2, 4] (indicating that it spans rows 0 and 1 and columns 2 and 3), and S2 given by [2, 4, 0, 2].

Our function call, submatrix_swap(matrix, coord_S1=[0, 2, 2, 4], coord_S2=[2, 4, 0, 2]), should return the following swapped matrix:

Python
Copy to clipboard
[[1, 2, 11, 12, 5],
 [6, 7, 16, 17, 10],
 [3, 4, 13, 14, 15],
 [8, 9, 18, 19, 20],
 [21, 22, 23, 24, 25]]
Explanation:

In this scenario, the sub-matrix S1 spans rows 0 to 1 and columns 2 to 3, including the elements 3, 4, 8, 9. The sub-matrix S2 spans rows 2 to 3 and columns 0 to 1, including the elements 11, 12, 16, 17.

The function submatrix_swap() swaps the positions of S1 and S2 within M. As a result, the elements in columns 2 and 3 of rows 0 and 1 are replaced by S2, and the elements in columns 0 and 1 of rows 2 and 3 are replaced by S1.

'''

def submatrix_swap(matrix, coord_S1, coord_S2) :
# {
    # TODO: Implement the function that swaps coord_S1 and coord_S2 in the matrix
    s1_min_x = coord_S1[0]
    s1_min_y = coord_S1[2]
    s1_max_x = coord_S1[1]
    s1_max_y = coord_S1[3]
    s2_min_x = coord_S2[0]
    s2_min_y = coord_S2[2]
    s2_max_x = coord_S2[1]
    s2_max_y = coord_S2[3]

    a = s1_min_x
    b = s1_min_y
    c = s2_min_x
    d = s2_min_y

    while (a < s1_max_x and c < s2_max_x) :
    # {

         while (b < s1_max_y and d < s2_max_y) :
         # {
              matrix[a][b], matrix[c][d] = matrix[c][d], matrix[a][b]
              b = b + 1
              d = d + 1 
         # }  
 
         a = a + 1
         c = c + 1
         b = s1_min_y
         d = s2_min_y 
    # }
 
    return matrix
 
# }

M = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25]]

coord_S1 = [0, 2, 2, 4]
coord_S2 = [2, 4, 0, 2]

print(submatrix_swap(M, coord_S1, coord_S2))

'''

***** BONEYARD *****

'''