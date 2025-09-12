'''

Given a 2D matrix of n x m integers, where n represents the number of rows and m represents the number of columns. Both n and m range from 1 to 100, inclusive.

The matrix cells may contain either a positive, a negative integer, or zero, with values ranging from -100 to 100, inclusive.

In this task, you are required to traverse the matrix diagonally from the top-left cell to the bottom-right cell in a zigzag pattern. Start from the top-left cell, move one cell to the right (if it exists), then move one step diagonally down-left. After reaching a left (bottom) boundary, move one step down (right) and start moving diagonally up-right. Continue this pattern until you reach the last cell of the matrix. Your task is to return a list of tuples, each tuple containing the index pair of cells with negative integers encountered during your traversal.

For example, consider a 3 x 4 matrix:

Copy to clipboard
[[1, -2, 3, -4],
[5, -6, 7, 8],
[-9, 10, -11, 12]]
The traversal in a zigzag pattern will result in: [1, -2, 5, -9, -6, 3, -4, 7, 10, -11, 8, 12]

The negative integers in this sequence and their corresponding positions in the matrix are: [-2, -9, -6, -4, -11], with indices: [(0, 1), (2, 0), (1, 1), (0, 3), (2, 2)].

Your function, solution(matrix), should then return these indices as a list of tuples: [(0, 1), (2, 0), (1, 1), (0, 3), (2, 2)].

Thanks for your honesty! Let’s break it down with a concrete example:

Suppose you’re at position (row, col).

If you’re moving up-right (row -= 1, col += 1), but you hit the top row (row == 0), you can’t go further up. So, instead, you move right one step (col += 1) and then switch to moving down-left.
If you’re moving down-left (row += 1, col -= 1), but you hit the left column (col == 0), you can’t go further left. So, you move down one step (row += 1) and then switch to moving up-right.
You only move directly right or down when you hit the edge and can’t continue diagonally.
Would you like to see a step-by-step for a small matrix?

'''

def traverse_zigzag(matrix) :
# {
    row = 0
    col = 0
    up_right = True
    down_left = False
    visited = []
    result = []

    visited.append((row, col))

    if (matrix[row][col] < 0) :
    # {
        result.append((row, col))
    # }

    else :
    # {
        None
    # }

    while (row < len(matrix) and col < len(matrix[0]) and len(visited) != len(matrix) * len(matrix[0])) :
    # {
        # up-right
        while(up_right and len(visited) != len(matrix) * len(matrix[0])) :
        # {
            if (row > 0 and col < len(matrix[0]) - 1) :
            # {
                row = row - 1
                col = col + 1
                visited.append((row, col))

                if (matrix[row][col] < 0) :
                # {
                    result.append((row, col))
                # }

                else :
                # {
                    None
                # }
                        
            # }

            else :
            # {
                None
            # }

            # If you hit the bottom row, move right (if possible).
            if (row == len(matrix) - 1 and col < len(matrix[0]) - 1) :
            # {
                up_right = False
                col = col + 1
                visited.append((row, col))

                if (matrix[row][col] < 0) :
                # {
                    result.append((row, col))
                # }

                else :
                # {
                    None
                # }
            
            # }

            else :
            # {
                None
            # }

            # If you hit the right column, move down (if possible).
            if (col == len(matrix[0]) - 1 and up_right and row < len(matrix) - 1) :
            # {
                up_right = False
                row = row + 1
                visited.append((row, col))
                
                if (matrix[row][col] < 0) :
                # {
                    result.append((row, col))
                # }

                else :
                # {
                    None
                # }
            
            # }

            else :
            # {
                None
            # }

            # If you hit the top row, move right.
            if (row == 0 and up_right and col < len(matrix[0]) - 1) :
            # {
                up_right = False
                col = col + 1
                visited.append((row, col))
                
                if (matrix[row][col] < 0) :
                # {
                    result.append((row, col))
                # }

                else :
                # {
                    None
                # }
            
            # }

            else :
            # {
                None
            # }

            # If you hit the left column, move down.
            if (col == 0 and up_right and row < len(matrix) - 1) :
            # {
                up_right = False
                row = row + 1
                visited.append((row, col))
                
                if (matrix[row][col] < 0) :
                # {
                    result.append((row, col))
                # }

                else :
                # {
                    None
                # }
            
            # }

            else :
            # {
                None
            # }

        # }

        if(len(visited) < len(matrix) * len(matrix[0])) :
        # {
            down_left = True
        # }

        else :
        # {
            None
        # }

        # down-left
        while(down_left and len(visited) <= len(matrix) * len(matrix[0])) :
        # {
            if (row < len(matrix) - 1 and col > 0) :
            # {
                row = row + 1
                col = col - 1
                visited.append((row, col))
                
                if (matrix[row][col] < 0) :
                # {
                    result.append((row, col))
                # }

                else :
                # {
                    None
                # }
            
            # }

            else :
            # {
                None
            # }

            # If you hit the bottom row, move right (if possible).
            if (row == len(matrix) - 1 and col < len(matrix[0]) - 1) :
            # {
                down_left = False
                col = col + 1
                visited.append((row, col))
                
                if (matrix[row][col] < 0) :
                # {
                    result.append((row, col))
                # }

                else :
                # {
                    None
                # }
            
            # }

            else :
            # {
                None
            # }

            # If you hit the right column, move down (if possible).
            if (col == len(matrix[0]) - 1 and down_left and row < len(matrix) - 1) :
            # {
                down_left = False
                row = row + 1
                visited.append((row, col))
                
                if (matrix[row][col] < 0) :
                # {
                    result.append((row, col))
                # }

                else :
                # {
                    None
                # }
            
            # }

            else :
            # {
                None
            # }

            # If you hit the top row, move right.
            if (row == 0 and down_left and col < len(matrix[0]) - 1) :
            # {
                down_left = False
                col = col + 1
                visited.append((row, col))
                
                if (matrix[row][col] < 0) :
                # {
                    result.append((row, col))
                # }

                else :
                # {
                    None
                # }
            
            # }

            else :
            # {
                None
            # }

            # If you hit the left column, move down.
            if (col == 0 and down_left and row < len(matrix) - 1) :
            # {
                down_left = False
                row = row + 1
                visited.append((row, col))
                
                if (matrix[row][col] < 0) :
                # {
                    result.append((row, col))
                # }

                else :
                # {
                    None
                # }
            
            # }

            else :
            # {
                None
            # }

        # }

        if(len(visited) < len(matrix) * len(matrix[0])) :
        # {
            up_right = True
        # }

        else :
        # {
            None
        # }

    # }

    return result

# }

def solution(matrix) :
# {
    # TODO: implement
    return traverse_zigzag(matrix)
# }

matrix = [
            [-1, -2,  3, -4],
            [5, -6,  7,  8],
            [-9, 10, -11, 12]
         ]

# zigzag [1, -2, 5, -9, -6, 3, -4, 7, 10, -11, 8, 12]
# [-2, -9, -6, -4, -11], with indices: [(0, 1), (2, 0), (1, 1), (0, 3), (2, 2)]
# [(0, 1), (2, 0), (1, 1), (0, 3), (2, 2)].

print(solution(matrix))


'''

***** BONEYARD *****


        # up_right = True
        # print(visited, len(visited))

print("!1", matrix[row][col])
print("!2", matrix[row][col])
print("!3", matrix[row][col])
print("!4", matrix[row][col])
print("!5", matrix[row][col])
print("!6", matrix[row][col])
print("!7", matrix[row][col])
print('!8', matrix[row][col])
print("!9", matrix[row][col])
print("!10", matrix[row][col])

# print((row, col))
# down_left = True


# print()

# if (row == len(matrix) - 1 and col == len(matrix[0]) - 1) :

# right
col = col + 1
print(matrix[row][col])

# down
print("hey")
if (row + 1 < len(matrix)) :
# {
    row = row + 1
    print(matrix[row][col])
# }

else :
# {
    None
# }

def traverse_zigzag(matrix) :
# {
    i = 0
    j = 0
    visited = []
    result = []

    if (matrix[i][j] < 0) :
    # {
        result.append((i, j))
        # return result
    # }

    else :
    # {
        None
    # }

    while(i < len(matrix) and j < len(matrix[0])) : 
    # {
        if (i == len(matrix) - 1 and j == len(matrix[0]) - 1) :
        # {
            visited.append((i, j))

            if (matrix[i][j] < 0) :
            # {
                result.append((i, j))
            # }

            else :
            # {
                None
            # }

            i = len(matrix)
            j = len(matrix[0])

        # }

        else :
        # {
            None
        # }
        
        # move right
        if (j + 1 <= len(matrix[0]) - 1 and (i, j + 1) not in visited) :
        # {
            j = j + 1
            visited.append((i, j))

            if (matrix[i][j] < 0) :
            # {
                result.append((i, j))
            # }

            else :
            # {
                None
            # }

        # }

        else :
        # {
            None
        # }

        while(i + 1 <= len(matrix) - 1 and j - 1 >= 0 and (i + 1, j - 1) not in visited) :
        # {            
            # down-left
            if (i + 1 <= len(matrix) - 1 and j - 1 >= 0 and (i + 1, j - 1) not in visited) :
            # {
                i = i + 1
                j = j - 1
                
                visited.append((i, j))

                if (matrix[i][j] < 0) :
                # {
                    result.append((i, j))
                # }

                else :
                # {
                    None
                # }

            # }

            else :
            # {
                None
            # }

        # }

        # down
        if (i + 1 <= len(matrix) - 1 and (i + 1, j) not in visited) :
        # {
            i = i + 1
            visited.append((i, j))

            if (matrix[i][j] < 0) :
            # {
                result.append((i, j))
            # }

            else :
            # {
                None
            # }
                
        # }

        else :
        # {
            None
        # }

        while (i - 1 >= 0 and j + 1 <= len(matrix[0]) - 1 and (i - 1, j + 1) not in visited) :
        # {            
            # up-right
            if (i - 1 >= 0 and j + 1 <= len(matrix[0]) - 1 and (i - 1, j + 1) not in visited) :
            # {
                i = i - 1
                j = j + 1
                visited.append((i, j))

                if (matrix[i][j] < 0) :
                # {
                    result.append((i, j))
                # }

                else :
                # {
                    None
                # }
                
            # }

            else :
            # {
                None
            # }

        # }

    # }

    return result

# }

if (len(matrix) == 1) :
# {
    # visited.append((i, j))

    

# }

else :
# {
    None
# }

if (i == 0 and j == 0) :
        # {
            visited.append((i, j))

            if (matrix[i][j] < 0) :
            # {
                result.append((i, j))
            # }

            else :
            # {
                None
            # }

        # }

        else :
        # {
            None
        # }


# print('@@')


        
        
            
                
            # print(len(matrix), len(matrix[0]))
        # print('1')

            # print('1', (i, j), matrix[i][j])
        # print('2', (i + 1, j - 1), i + 1 <= len(matrix) - 1, j - 1 >= 0, (i + 1, j - 1) not in visited)
        # print('2')
            # print('2!', (i + 1, j - 1), i + 1 <= len(matrix), j - 1 >= 0, (i + 1, j - 1) not in visited)
                # print('2', (i, j), matrix[i][j])
        # print('3')
            # print('3', (i, j), matrix[i][j])
        # print('4', (i, j), i - 1 >= 0, j + 1 <= len(matrix[0]) - 1, (i - 1, j + 1) not in visited, visited)
            # print('4', (i, j), i - 1 >= 0, j + 1 <= len(matrix[0]) - 1, (i - 1, j + 1) not in visited)
                # print('4', (i, j), matrix[i][j])

        # print((i, j), i < len(matrix), j < len(matrix[0]))
                

'''