"""

Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.

For cell1 = "A1" and cell2 = "H3", the output should be
solution(cell1, cell2) = false.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string cell1

Guaranteed constraints:
cell1.length = 2,
'A' ≤ cell1[0] ≤ 'H',
1 ≤ cell1[1] ≤ 8.

[input] string cell2

Guaranteed constraints:
cell2.length = 2,
'A' ≤ cell2[0] ≤ 'H',
1 ≤ cell2[1] ≤ 8.

[output] boolean

true if both cells have the same color, false otherwise.

"""

def chessboard_cell_color(cell1, cell2) :
# {
    val1 = ord(cell1[0]) + ord(cell1[1])
    val2 = ord(cell2[0]) + ord(cell2[1])
    result = None

    if (val1 % 2 == 0 and val2 % 2 == 0) :
    # {
        result = True
    # }

    elif (val1 % 2 == 1 and val2 % 2 == 1) :
    # {
        result = True
    # }

    else :
    # {
        return False
    # }

    return result

# }

def solution(cell1, cell2) :
# {
    return chessboard_cell_color(cell1, cell2)
# }

# For cell1 = "A1" and cell2 = "C3", the output should be solution(cell1, cell2) = true.
# For cell1 = "A1" and cell2 = "H3", the output should be solution(cell1, cell2) = false.

cell1 = "A1" 
cell2 = "C3"
cell1 = "A1" 
cell2 = "H3"

print(solution(cell1, cell2))

"""

********
BONEYARD
********

# print(val1, val2)
# print(result)

    
"""