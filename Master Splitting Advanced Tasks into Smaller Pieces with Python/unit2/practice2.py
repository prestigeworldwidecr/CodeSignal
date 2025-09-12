'''

Consider a grid of characters in the form of a 2D array, where each cell represents a distinct character selected from a-z. Your task is to process this grid following a specific order.

Start from the top-left cell of the grid and move in a clockwise spiral direction. Initially, go right until you hit the right boundary, then down until you reach the bottom boundary, then left until you encounter the left boundary, and finally, up until you hit the top boundary (note that the top boundary is now the first row since we already visited the first cell in the matrix). Once this cycle is complete, move inwards, i.e., one cell to the right, and repeat the spiral process within the remaining unvisited cells.

During this spiral traversal, you will generate a sequence of visited cell characters. Afterwards, identify the vowels (a, e, i, o, u) in the sequence and return their positions.

Please implement the function spiral_traverse_and_vowels(grid) to achieve this. This function takes a 2D array of characters (grid) as input and returns a list containing the positions of the vowels in the spirally traversed sequence.

For instance, consider the following 3x4 grid:

Copy to clipboard
[['a', 'b', 'c', 'd'],
['e', 'f', 'g', 'h'],
['i', 'j', 'k', 'l']]
Upon completing the spiral traversal, we will obtain the sequence: ['a', 'b', 'c', 'd', 'h', 'l', 'k', 'j', 'i', 'e', 'f', 'g']. From this sequence, we observe that 'a', 'i', and 'e' are vowels and are located at the 1st, 9th, and 10th positions in the sequence, so our function returns: [0, 8, 9].

The size of the 2D array (grid) will not exceed 100x100, and each character will be a lowercase letter from 'a' to 'z'.

'''

def is_vowel(a) :
# {
    vowels = ['a', 'e', 'i', 'o', 'u']

    return a in vowels
# }

def spiral_traverse_and_vowels(grid) :
# {
    row = 0
    col = 0
    min_x = 0
    min_y = 0
    max_x = len(grid)
    max_y = len(grid[0])
    i = 0
    result = []

    if (is_vowel(grid[0][0])) :
    # {
        result.append(i)
    # }

    else :
    # {
        None
    # }

    i = i + 1

    while (0 < i < len(grid) * len(grid[0])) :
    # {
        # right
        while (col < max_y - 1 and i < len(grid) * len(grid[0])) :
        # {
            col = col + 1
            
            if (is_vowel(grid[row][col])) :
            # {
                result.append(i)
            # }

            else :
            # {
                None
            # }

            i = i + 1
        # }

        max_y = max_y - 1
        min_x = min_x + 1

        # down
        while (row < max_x - 1 and i < len(grid) * len(grid[0])) :
        # {
            row = row + 1

            if (is_vowel(grid[row][col])) :
            # {
                result.append(i)
            # }

            else :
            # {
                None
            # }
            
            i = i + 1
        # }

        max_x = max_x - 1

        # left
        while (col > min_y and i < len(grid) * len(grid[0])) :
        # {
            col = col - 1
            
            if (is_vowel(grid[row][col])) :
            # {
                result.append(i)
            # }

            else :
            # {
                None
            # }
            
            i = i + 1
        # }

        min_y = min_y + 1

        # up
        while (row > min_x and i < len(grid) * len(grid[0])) :
        # {
            row = row - 1
            
            if (is_vowel(grid[row][col])) :
            # {
                result.append(i)
            # }

            else :
            # {
                None
            # }
            
            i = i + 1
        # }

        min_x = min_x + 1

    # }

    return result

# }

def solution(grid) :
# {
    return spiral_traverse_and_vowels(grid)
# }

grid = [['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h'],
        ['i', 'j', 'k', 'l']]

# result ['a', 'b', 'c', 'd', 'h', 'l', 'k', 'j', 'i', 'e', 'f', 'g']

print(solution(grid))

'''

***** BONEYARD *****

print(grid[row][col])

# print(i)

# max_y = max_y - 1
# print('1', (col, row), grid[row][col], max_y, i)
# max_x = max_x - 1
# print('2', (col, row), grid[row][col], max_y, i)
# min_y = min_y - 1
# print('3', (col, row), grid[row][col], max_y, i)
# min_x = min_x - 1
# print('4', (col, row), grid[row][col], max_y, i)

# print(grid[0][0])

    
# print('1')

while (row < len(grid) and col < len(grid[0]) and i <= len(grid) * len(grid[0])) :
# {
    print('1', (row, col), grid[row][col], result)

    # move right
    while (col < len(grid[0]) - 1) : # and i <= len(grid) * len(grid[0])) :
    # {
        col = col + 1
        print('2', (row, col), grid[row][col], i, result)

        if (is_vowel(grid[row][col])) :
        # {
            result.append(i)
        # }

        else :
        # {
            None
        # }

        i = i + 1

    # }

    # move down
    if (row < len(grid) - 1) : # and i <= len(grid) * len(grid[0])) :
    # {
        row = row + 1
        print('3', (row, col), grid[row][col], i, result)

        if (is_vowel(grid[row][col])) :
        # {
            result.append(i)
        # }

        else :
        # {
            None
        # }

        i = i + 1

    # }

    else :
    # {
        None
    # }

    # move left
    while (col > 0) : # and i <= len(grid) * len(grid[0])) :
    # {
        col = col - 1
        # print('!', grid[row][col], grid[row][col] == 'e')
        print('4', (row, col), grid[row][col], i, result)
                
        if (is_vowel(grid[row][col])) :
        # {
            result.append(i)
        # }

        else :
        # {
            None
        # }

        i = i + 1

    # }

    if (row < len(grid) - 1 and i <= len(grid) * len(grid[0])) :
    # {
        # move down
        row = row + 1
        print('5', (row, col), grid[row][col], i, result)

        if (is_vowel(grid[row][col])) :
        # {
            result.append(i)
        # }

        else :
        # {
            None
        # }

        i = i + 1

    # }

    else :
    # {
        None
    # }

# }

'''