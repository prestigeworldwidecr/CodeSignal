"""

Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:

Example

For bishop = "a1" and pawn = "c3", the output should be
solution(bishop, pawn) = true

For bishop = "h1" and pawn = "h3", the output should be
solution(bishop, pawn) = false

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string bishop

Coordinates of the white bishop in the chess notation.

Guaranteed constraints:
bishop.length = 2,
'a' ≤ bishop[0] ≤ 'h',
1 ≤ bishop[1] ≤ 8.

[input] string pawn

Coordinates of the black pawn in the same notation.

Guaranteed constraints:
pawn.length = 2,
'a' ≤ pawn[0] ≤ 'h',
1 ≤ pawn[1] ≤ 8.

[output] boolean

true if the bishop can capture the pawn, false otherwise.

"""

import sys

def slope_between_two_points(pos1, pos2) :
# {
    m = -sys.maxsize
    x_diff = (pos2[0] - pos1[0])
    y_diff = (pos2[1] - pos1[1])

    if (x_diff == 0) :
    # {
        None
    # }

    else :
    # {
        m = y_diff / x_diff   # m = (y2 - y1) / (x2 - x1)
    # }
    
    return m
# }

def bishop_eats(m) :
# {
    if(abs(m) == 1) :
    # {
        return True
    # }

    else :
    # {
        return False
    # }

# }

def convert_xy_position(pos) :
# {
    x = pos[0]
    y = int(pos[1])
    xy_pos = [-1, -1]

    match x :
    # {
        case 'a':
            x = 1
        case 'A':
            x = 1
        case 'b':
            x = 2
        case 'B':
            x = 2
        case 'c':
            x = 3
        case 'C':
            x = 3
        case 'd':
            x = 4
        case 'D': 
            x = 4
        case 'e':
            x = 5
        case 'E':
            x = 5
        case 'f':
            x = 6
        case 'F':
            x = 6
        case 'g':
            x = 7
        case 'G':
            x = 7
        case 'h':
            x = 8
        case 'H': 
            x = 8                
    # }

    xy_pos[0] = int(x)
    xy_pos[1] = y

    # print (xy_pos)

    return xy_pos
# }

def solution(bishop, pawn) :
# {
    return bishop_eats(slope_between_two_points(convert_xy_position(bishop), convert_xy_position(pawn)))
# }

bishop = "c4"  # 151
pawn = "f7"    # 157

bishop = "e8"  # 157
pawn = "a4"    # 149

bishop = "c4"  # 151
pawn = "f7"    # 157

bishop = "e8"  # 157
pawn = "a4"    # 149

bishop = "a2"  # 157
pawn = "c2"    # 149

bishop = "a2"  # 157
pawn = "c1"    # 149

bishop = "a1"  # 146
pawn = "c3"    # 150    the output should be solution(bishop, pawn) = true

bishop = "h1"  # 153
pawn = "h3"    # 155    the output should be solution(bishop, pawn) = false

print(solution(bishop, pawn))

"""

********
BONEYARD
********

"""