"""


Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
solution(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2

2 1
2 2

2 2
2 2

2 2
1 2

2 2
2 3

2 3
2 1

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.array.integer matrix

Guaranteed constraints:
1 ≤ matrix.length ≤ 100,
1 ≤ matrix[i].length ≤ 100,
0 ≤ matrix[i][j] ≤ 9.

[output] integer

The number of different 2 × 2 squares in matrix.

"""

def create_all_2x2s(matrix) :
# {
    all_2x2s = []

    for i in range(len(matrix) - 1) :
    # {
        for j in range(len(matrix[0]) - 1) :
        # {
            tmp = [ [1, 2],
                        [3, 4]]

            tmp[0][0] = matrix[i][j]
            tmp[0][1] = matrix[i][j + 1]
            tmp[1][0] = matrix[i + 1][j]
            tmp[1][1] = matrix[i + 1][j + 1]

            all_2x2s.append(tmp)
        # }

    # }

    return all_2x2s
# }

def different_squares(a) :
# {
    tmp = []

    for i in range(len(a)) :
    # {
        s = str(a[i])
        s = s.replace('[', "")
        s = s.replace(']', "")

        if (s in tmp) :
        # {
            None
        # }

        else :
        # {
            tmp.append(s)
        # }

    # }

    return len(tmp)
# }

def solution(matrix) :
# {
    tmp = create_all_2x2s(matrix)
    
    return different_squares(tmp)
# }

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],    # height: 5
          [1, 2, 3],    # width: 3
          [2, 2, 1]]   # the output should be solution(matrix) = 6.

m1 = [  [1, 1],
        [1, 1]  ]
m2 = [  [2, 2],
        [2, 2]  ]

matrix1 = [ [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],    # height: 5
                [10, 11, 12],    # width: 3
                [13, 14, 15]]   # the output should be solution(matrix) = 8.

print(solution(matrix1))

"""

********
BONEYARD
********

"""