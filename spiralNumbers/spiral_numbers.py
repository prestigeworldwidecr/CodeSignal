"""

Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

solution(n) = [[1, 2, 3],
               [8, 9, 4],
               [7, 6, 5]]
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Matrix size, a positive integer.

Guaranteed constraints:
3 ≤ n ≤ 100.

[output] array.array.integer

"""

import math

def print_matrix(matrix) :
# {
    tmp = ""

    for i in len(matrix[0]) :
    # {
        tmp = tmp + matrix[i][j] + "\t"
    # }

    print(tmp)

# }

def create_NxN_array(n) :
# {
    m = [None] * n

    for i in range(n) :
    # {
        # print(i)
        m[i] = [None] * n

        for j in range(n) :
        # { 
            m[i][j] = 'x'
        # }

    # }

    return m

# }

def spiral_numbers(n) :
# {
    m = create_NxN_array(n)
    cnt = 1
    right_borderX = 0
    right_borderY = len(m)
    down_borderX = 0
    down_borderY = len(m)
    left_borderX = len(m) - 1
    left_borderY = 0
    up_borderX = len(m) - 1
    up_borderY = 0

    while(cnt <= math.pow(len(m), 2) and cnt > 0) :
    # {        
        print("!", cnt, m)

        cnt = move_right(m, cnt, right_borderX, right_borderY)
        right_borderX = right_borderX + 1
        right_borderY = right_borderY - 1

        if (cnt <= math.pow(len(m), 2)) :
        # {
            cnt = move_down(m, cnt - 1, down_borderX, down_borderY)
            down_borderX = down_borderX + 1
            down_borderY = down_borderY - 1
            print("@", cnt, m)
        # }

        else :
        # {
            None
        # }

        if (cnt <= math.pow(len(m), 2)) :
        # {
            
            cnt = move_left(m, cnt - 1, left_borderX, left_borderY)
            left_borderX = left_borderX - 1
            left_borderY = left_borderY + 1
            print("#", cnt, m)

        # }

        else :
        # {
            None
        # }

        if (cnt <= math.pow(len(m), 2)) :
        # {
            
            cnt = move_up(m, cnt - 1, up_borderX, up_borderY)
            up_borderX = up_borderX - 1
            up_borderY = up_borderY + 1
            print("$", cnt, m)

        # }

        else :
        # {
            None
        # }

    # }

    return m

# }

def move_right(a, cnt, right_borderX, right_borderY) :
# {

    # for (let i = rightBorderX; i < rightBorderY; i++)
    for i in range(right_borderX, right_borderY) :
    # {
        # console.log("! i:", i, "cnt:", cnt, "rightBorderX:", rightBorderX, "rightBorderY:", rightBorderY);
        a[right_borderX][i] = cnt
        cnt = cnt + 1
    # }

    return cnt
# }

def move_down(a, cnt, downBorderX, downBorderY) :
# {

    # for (let i = downBorderX; i < downBorderY; i++)
    for i in range(downBorderX, downBorderY) :
    # {
        # console.log("@ i:", i, "cnt:", cnt, "downBorderX:", downBorderX, "downBorderY:", downBorderY);
        a[i][downBorderY - 1] = cnt
        cnt = cnt + 1
    # }

    return cnt
# }

def move_left(a, cnt, left_borderX, left_borderY) :
# {
    # for (let i = leftBorderX; i >= leftBorderY; i--) :
    # for i in range(left_borderX, left_borderY) :
    for i in range(left_borderY, left_borderX, -1) :
    # {
        # print(a, " # i:", i, "cnt:", cnt, "leftBorderX:", left_borderX, "leftBorderY:", left_borderY)
        a[left_borderX][i] = cnt
        cnt = cnt + 1
    # }

    return cnt
# }

def move_up(a, cnt, up_borderX, up_borderY) :
# {
    # for (let i = upBorderX; i > upBorderY; i--) 
    # for i in range(up_borderX, up_borderY) :
    for i in range(up_borderY, up_borderX, -1) :
    # {
        # print("$ i:", i, "cnt:", cnt, "up_borderX:", up_borderX, "up_borderY:", up_borderY)
        a[i][up_borderY] = cnt
        cnt = cnt + 1
    # }

    return cnt
# }

def solution(n) :
# {
    return spiral_numbers(n)
# }    

n = 3;   #the output should be solution(n) =  [[1, 2, 3],
#                                              [8, 9, 4],
#                                              [7, 6, 5]]

# spiral_numbers(5)
print(solution(n))

"""

********
BONEYARD
********

if (up_borderX <= 0) :
            # {
                None
            # }

            else :
            # {
                None
            # }
            
            if (up_borderY >= len(m)) :
            # {
                None
            # }    
                
            else :
            # {
                None # check if reaches len(m)
            # }

# let downBorderX = 0;
        # let downBorderY = m.length;
        

            if (left_borderX <= 0) :
            # {
                None 
            # }

            else :
            # {
                None
            # }
            
            if (left_borderY >= len(m)) :
            # {
                None
            # }

            else :
            # {
                None # check if reaches len(m)
            # }

            # print("!", "cnt:", cnt, "leftBorderX:", left_borderX, "leftBorderY:", left_borderY)
            # print("@", "cnt:", cnt, "leftBorderX:", left_borderX, "leftBorderY:", left_borderY)
            # print(cnt, right_borderX, right_borderY, down_borderX, down_borderY, left_borderX, left_borderY, up_borderX, up_borderY)

Creating an empty list:

>>> xs = [None] * 10
>>> xs
[None, None, None, None, None, None, None, None, None, None]
Assigning a value to an existing element of the above list:

>>> xs[1] = 5
>>> xs
[None, 5, None, None, None, None, None, None, None, None]

"""