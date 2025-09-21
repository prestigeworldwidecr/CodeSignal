'''

Your task is to write a function, interleave_matrices(), that takes two matrices (2D arrays) and a start and end range for rows and columns for each matrix as inputs. Instead of concatenating submatrices together, this task requires interleaving the columns from the submatrices within the final matrix.

If A and B are your two matrices, and the respective submatrices selected from them based on the given ranges are sub_A and sub_B, then the task is to form a new matrix C by interleaving columns from sub_A and sub_B. Starting with the first column of sub_A, alternately include a column from sub_A and a column from sub_B until all columns from both submatrices are included.

All matrices are filled with integers. The size of each matrix, A and B, ranges between 
1
×
1
1×1 and 
10
×
10
10×10, inclusive, and each element in the matrix is from the range of 
−
100
−100 to 
100
100, inclusive. The start and end ranges for rows and columns for each matrix are provided as a tuple (start_row, end_row, start_column, end_column), and these are 1-based indices.

For example, if A is:

Your task is to write a function, interleave_matrices(), that takes two matrices (2D arrays) and a start and end range for rows and columns for each matrix as inputs. Instead of concatenating submatrices together, this task requires interleaving the columns from the submatrices within the final matrix.

If A and B are your two matrices, and the respective submatrices selected from them based on the given ranges are sub_A and sub_B, then the task is to form a new matrix C by interleaving columns from sub_A and sub_B. Starting with the first column of sub_A, alternately include a column from sub_A and a column from sub_B until all columns from both submatrices are included.

All matrices are filled with integers. The size of each matrix, A and B, ranges between 
1
×
1
1×1 and 
10
×
10
10×10, inclusive, and each element in the matrix is from the range of 
−
100
−100 to 
100
100, inclusive. The start and end ranges for rows and columns for each matrix are provided as a tuple (start_row, end_row, start_column, end_column), and these are 1-based indices.

For example, if A is:

[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]]

and B is:

[[11, 12, 13],
[14, 15, 16],
[17, 18, 19]]

If we select 2x2 submatrices from each (comprising the 2nd to the 3rd rows and the 2nd to the 3rd columns from A, and the 1st to the 2nd rows and the 1st to the 2nd columns from B), their interleaved combination would look like this:

[[6, 11, 7, 12],
[10, 14, 11, 15]]

Note that in the output, columns from sub_A and sub_B are interwoven.

It is guaranteed that the given submatrices have pairwise equal dimensions.

submatrix_coords = [(2, 3, 2, 3), (1, 2, 1, 2)]

The first tuple (2, 3, 2, 3) is for matrix_A: rows 2–3, columns 2–3.
The second tuple (1, 2, 1, 2) is for matrix_B: rows 1–2, columns 1–2.
So, submatrix_coords stores the coordinates for which part of each matrix you want to extract.
Does that help clear things up?

You're getting an IndexError in your build_submatrix function.
Try to simplify:

Use list slicing to extract the rows and columns, just like in the lesson.
For example

submatrix = [row[start_col-1:end_col] for row in matrix[start_row-1:end_row]]

Read message aloud
You're currently just joining the rows from both submatrices, but the practice wants you to interleave columns from each submatrix.

Try this:

For each row, instead of row_A + row_B, build a new row by taking one column from row_A, then one from row_B, and repeat.
You can use a loop or a list comprehension with zip(row_A, row_B) to alternate elements.
What do you think would happen if you tried [a, b for a, b in zip(row_A, row_B)]? Can you adjust your code to build the interleaved row this way?

'''

def build_submatrix(matrix, coordinates) :
# {
    min_x = coordinates[0]
    min_y = coordinates[2]
    max_x = coordinates[1]
    max_y = coordinates[3]

    submatrix = []

    for row in matrix[min_x - 1: max_x : ] :
    # {
        sub_row = row[min_y - 1 : max_y : ]
        submatrix.append(sub_row)
    # }

    return submatrix

# }

def interleave_matrices(matrix_A, matrix_B, submatrix_coords) :
# {
    submatrix_A = build_submatrix(matrix_A, submatrix_coords[0])
    submatrix_B = build_submatrix(matrix_B, submatrix_coords[1])

    result = []

    for a, b in zip(submatrix_A, submatrix_B):
    # {
        result_row = []

        for x, y in zip(a, b) :
        # {
            result_row.append(x)
            result_row.append(y)
        # }

        result.append(result_row)
        
    # }

    return result

# }

def solution(matrix_A, matrix_B, submatrix_coords) :
# {
    # TODO: Implement the solution here.
    return interleave_matrices(matrix_A, matrix_B, submatrix_coords)
# }

matrix_A = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]


matrix_B = [[11, 12, 13],
            [14, 15, 16],
            [17, 18, 19]]

submatrix_coords = [(2, 3, 2, 3),
                    (1, 2, 1, 2)]

# result [[6, 11, 7, 12],
#        [10, 14, 11, 15]]

print(solution(matrix_A, matrix_B, submatrix_coords))

'''

***** BONEYARD *****

result_row.append(a)
result_row.append(b)
result.append(result_row)

from itertools import chain

return list(chain.from_iterable(zip(submatrix_A, submatrix_B)))

# result = []

result = 

for items in zip(submatrix_A, submatrix_B) :
# {
    result.extend(items)
# }

for pair in zip(submatrix_A, submatrix_B) :
# {
    # print (pair)

    for item in pair :
    # {
        # print(item[0], item[1])
        result.append(item)
    # }

# }

# [a, b for a, b in zip(row_A, row_B)]
# interleaved_list = [item for pair in zip(submatrix_A, submatrix_B) for item in pair]
# print(interleaved_list)


for item in pair :
# {
    for pair in zip(submatrix_A, submatrix_B) :
    # {
        result.append(item)
    # }

# }

 i = 0
tmp = []
tmp1 = []


for a, b in zip(submatrix_A, submatrix_B) :
# {
    for i in range(len(submatrix_A)) :
    # {
        tmp.append(a[i])
        tmp.append(b[i])
        print(i, a[i], b[i])
        i = i + 1
    # }

    tmp1 = tmp1 + tmp
    tmp1 = []
    result = result + tmp1

    i = 0

# }

print(tmp)

# j = 0        
# result.append(a + b)
# print(a, b)
# result.append(b)
# result.append(a[i])
# result.append(b[i])
# j = 0

# result.append(tmp)
# print(tmp1)

# result.append(tmp)


# result_matrix = [row_A + row_B for row_A, row_B in zip(submatrix_A, submatrix_B)]
for row_A, row_B in zip(submatrix_A, submatrix_B) :
# {
    result.append(row_A + row_B)
# }


    result = []
    a = 0
    b = 0

    for b in range(len(submatrix_A[0])) :
    # {
        row = []

        for a in range(len(submatrix_A) * 2) :
        # {
            row.append(0)
        # }

        result.append(row)

    # }

    a = 0
    b = 0
    i = 0
    j = 0

    # print('$', len(result))

    while (i < len(result)) :
    # {
        while (j < len(result[0]) - 1) :
        # {
            result[i][j] = submatrix_A[a][b]
            # print("!1", (i, j), a, b, result[i][j], submatrix_A[a][b], j)
            j = j + 1
            result[i][j] = submatrix_B[a][b]
            # print("!2", (i, j), a, b, result[i][j], submatrix_B[a][b], j)
            j = j + 1

            if (b < len(submatrix_A[a]) - 1) :
            # {
                b = b + 1
            # }

            else :
            # {
                b = 0
            # }

        # }

        # print('@')
        j = 0
        i = i + 1
        a = a + 1

    # }

# Iterate through the selected rows of the original matrix
# For each selected row, slice the relevant columns
# Append the resulting sub_row to the submatrix

result = []

for row in matrix[min_x : max_x : ] :
# {
    row = []

    for x in range(len(matrix)) :
    # {
        row.append(0)
    # }

    result.append(row)

# }

submatrix = []
# Iterate through the selected rows of the original matrix
for row in matrix[start_row-1:end_row]:
    # For each selected row, slice the relevant columns
    sub_row = row[start_col-1:end_col]
    # Append the resulting sub_row to the submatrix
    submatrix.append(sub_row)

for b in range(max_y - min_y + 1) :
# {
    row = []

    for a in range(max_x - min_x + 1) :
    # {
        row.append(0)
    # }

    submatrix.append(row)

# }

a = 0
b = 0

while(min_x <= max_x) :
# {
    j = min_y
    
    while (j <= max_y) :
    # {
        submatrix[a][b] = matrix[min_x][j]
        j = j + 1
        b = b + 1
    # }

    min_x = min_x + 1
    a = a + 1
    b = 0
# }

# print((i, j), a, b)
# b = b + 1
# print((i, j))
# print((i, j), a, b)
# print((i, j), a, b)
# b = 

# print(submatrix_A)
    # print(submatrix_B)
 

# import numpy

# print('!', len(submatrix))
# print(a, b)

# matrix = [[0 for x in range(3)] for y in range(3)] # x = width, y = height
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for a in range(max_y - min_y + 1) :
# {
    submatrix.append(0)

    for b in range(max_y - min_y + 1) :
    # {
        submatrix[b].append(0)
    # }

# }

# print(len(submatrix))


# submatrix = numpy.zeros((max_x - min_x + 1, max_y - min_y + 1))
# submatrix = [0] * (max_x - min_x + 1)
# submatrix.append([0])
# print(submatrix[k])
# print(k)
# submatrix = submatrix[0] * (k)

# submatrix.append(a)


# submatrix[a].append(b)
# print(matrix[min_x][j])

# submatrix = [max_x - min_x + 1] * [max_y - min_y + 1]

submatrix = [0] * (max_x - min_x + 1)
    # print(len(submatrix))

    for k in range(max_y - min_y + 1) :
    # {
        # submatrix[k].append(0)
        # print(k)
        submatrix = 0
    # }

    print(submatrix[0][1])


    # print(matrix, coordinates)
    # j = min_y

    # print(min_x, min_y, max_x, max_y)

for i in range(min_x - 1, max_x) :
    # {
        # i = min_x
        # j = min_y 
        print('x', i)

        for j in range(min_y - 1, max_y) :
        # {
            # j = min_y 
            print('y', j)
        # }
    # }

'''