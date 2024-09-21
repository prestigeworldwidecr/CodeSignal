"""

Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = true

For
grid = [[1, 3, 4, 2, 5, 6, 9, 8, 7],
        [4, 6, 8, 5, 7, 9, 3, 2, 1],
        [7, 9, 2, 8, 1, 3, 6, 5, 4],
        [9, 2, 3, 1, 4, 5, 8, 7, 6],
        [3, 5, 7, 4, 6, 8, 2, 1, 9],
        [6, 8, 1, 7, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 5, 6, 3, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = false.

The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
These examples are represented on the image below.



Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.array.integer grid

A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.

Guaranteed constraints:
grid.length = 9,
grid[i].length = 9,
1 ≤ grid[i][j] ≤ 9.

[output] boolean

true if the given grid represents a correct solution to Sudoku, false otherwise.

"""

def scan_sudoku(grid, startX, endX, startY, endY) :
# {
    a = []

    for i in range(startX, endX) :
    # {
        for j in range(startY, endY) :
        # { 
            a.append(grid[i][j])
        # }

    # }

    return a

# }

def is_sudoku_compliant(a) :
# {
    result = False
    j = 1

    a = sorted(a)

    for i in range(len(a)) :
    # {
        if (a[i] == j) :
        # {
            result = True
            j = j + 1
        # }

        else :
        # {
            return False
        # }

    # }

    return result

# }

def solution(grid) :
# {
    result1 = is_sudoku_compliant(scan_sudoku(grid, 0, 3, 0, 3))
    result2 = is_sudoku_compliant(scan_sudoku(grid, 0, 3, 3, 6))
    result3 = is_sudoku_compliant(scan_sudoku(grid, 0, 3, 6, 9))
    result4 = is_sudoku_compliant(scan_sudoku(grid, 3, 6, 0, 3))
    result5 = is_sudoku_compliant(scan_sudoku(grid, 3, 6, 3, 6))
    result6 = is_sudoku_compliant(scan_sudoku(grid, 3, 6, 6, 9))
    result7 = is_sudoku_compliant(scan_sudoku(grid, 6, 9, 0, 3))
    result8 = is_sudoku_compliant(scan_sudoku(grid, 6, 9, 3, 6))
    result9 = is_sudoku_compliant(scan_sudoku(grid, 6, 9, 6, 9))

    # print(result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 and result9)
    
    return (result1 and result2 and result3 and result4 and result5 and result6 and result7 and result8 and result9)

# }

grid = [[1, 3, 4, 2, 5, 6, 9, 8, 7],
        [4, 6, 8, 5, 7, 9, 3, 2, 1],
        [7, 9, 2, 8, 1, 3, 6, 5, 4],
        [9, 2, 3, 1, 4, 5, 8, 7, 6],
        [3, 5, 7, 4, 6, 8, 2, 1, 9],
        [6, 8, 1, 7, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 5, 6, 3, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]

        # the output should be solution(grid) = false

## console.log(isSudokuCompliant(scan_sudoku(grid, 0, 3, 0, 3)))
print(solution(grid))

"""

********
BONEYARD
********

"""