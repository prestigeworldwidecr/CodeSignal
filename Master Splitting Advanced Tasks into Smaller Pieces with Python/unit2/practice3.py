'''

You are given a 2D matrix of integer values where each cell represents a unique integer. The size of the matrix, n x n, ranges from 1 x 1 to 10 x 10, and each integer cell value, v, ranges from 1 to 100, inclusive.

Your task is to traverse the matrix in a unique way: Start from the top-left cell and move right until you hit the upper right corner. Then, move downward one cell and start moving to the left until you hit the left boundary. Upon hitting the left boundary, move down one cell and start moving right until you hit the right boundary. When you hit the right boundary, move down one cell and start moving left again. Continue this pattern until you have traversed every cell in the matrix.

Having completed this zigzag traversal, you will gather a list of traversed cell values. Your task now is to process this list and identify the values of the prime numbers and their indices. Therefore, implement the function zigzag_traverse_and_primes(matrix) that returns a dictionary where each key-value pair represents an index and the prime number found at that index from the traversed list.

For instance, suppose you have a 3x3 matrix:

Copy to clipboard
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Upon completing the zigzag traversal, you obtain the list: [1, 2, 3, 6, 5, 4, 7, 8, 9]. From this list, we observe that 2, 3, 5, and 7 are prime numbers, and they are located at the 2nd, 3rd, 5th, and 7th positions in the list. Our function should return: {1: 2, 2: 3, 4: 5, 6: 7}.

Remember, a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are 2, 3, 5, 7, 11, and so on.

'''

import math

def is_prime(n) :
# {
    if (n <= 1) :
    # {
        return False  # Numbers less than or equal to 1 are not prime.
    # }

    else :
    # {
        None
    # }

    if (n == 2) :
    # {
        return True   # 2 is the only even prime number.
    # }

    else :
    # {
        None
    # }

    if (n % 2 == 0) :
    # {
        return False
    # }

    else :
    # {
        None
    # }

    for i in range(3, int(math.sqrt(n)) + 1, 2) :
    # {
        if (n % i == 0) :
        # {
            return False  # If divisible, it's not prime.
        # }

        else :
        # {
            None
        # }

    # }

    return True
    
# }

def zigzag_traverse_and_primes1(l) :
# {
    result = {}

    for i in range(len(l)) :
    # {
        if (is_prime(l[i])) :
        # {
            result[i] = l[i]
        # }

        else :
        # {
            None
        # }

    # }
    
    return result
# }

def zigzag_traverse_and_primes(a) :
# {
    row = 0
    col = 0
    visited = []
    i = 0
    result = {}

    visited.append(a[row][col])
    i = i + 1

    while (i <= len(a) * len(a[0]) - 1) :
    # {
        # move right
        while (col < len(a[0]) - 1 and i <= len(a) * len(a[0]) - 1) :
        # {
            col = col + 1
            visited.append(a[row][col])
            i = i + 1
        # }

        # move down
        if (row < len(a) - 1 and i <= len(a) * len(a[0]) - 1) :
        # {
            row = row + 1
            visited.append(a[row][col])
            i = i + 1
        # }

        else :
        # {
            None
        # }

        # move left
        while (col > 0 and i <= len(a) * len(a[0]) - 1) :
        # {
            col = col - 1
            visited.append(a[row][col])
            i = i + 1
        # }

        if (row < len(a) - 1 and i <= len(a) * len(a[0]) - 1) :
        # {
            # move down
            row = row + 1
            visited.append(a[row][col])
            i = i + 1

        # }

        else :
        # {
            None
        # }

    # }

    for i in range(len(visited)) :
    # {
        if (is_prime(visited[i])) :
        # {
            result[i] = visited[i]
        # }

        else :
        # {
            None
        # }

    # }
    
    return result
# }

def step1_ztp(grid) :
# {
    row = 0
    col = 0
    visited = []
    i = 0

    visited.append(grid[row][col])
    i = i + 1

    while (i <= len(grid) * len(grid[0]) - 1) :
    # {
        # move right
        while (col < len(grid[0]) - 1 and i <= len(grid) * len(grid[0]) - 1) :
        # {
            col = col + 1
            visited.append(grid[row][col])
            i = i + 1
        # }

        # move down
        if (row < len(grid) - 1 and i <= len(grid) * len(grid[0]) - 1) :
        # {
            row = row + 1
            visited.append(grid[row][col])
            i = i + 1
        # }

        else :
        # {
            None
        # }

        # move left
        while (col > 0 and i <= len(grid) * len(grid[0]) - 1) :
        # {
            col = col - 1
            visited.append(grid[row][col])
            i = i + 1
        # }

        if (row < len(grid) - 1 and i <= len(grid) * len(grid[0]) - 1) :
        # {
            # move down
            row = row + 1
            visited.append(grid[row][col])
            i = i + 1

        # }

        else :
        # {
            None
        # }

    # }

    return visited

# }

a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9] 
    ]

# print(zigzag_traverse_and_primes(step1_ztp(a)))
print(zigzag_traverse_and_primes(a))

'''

***** BONEYARD *****

# print('2', (row, col), grid[row][col], i)
# print('3', (row, col), grid[row][col], i)
# print('!', grid[row][col], grid[row][col] == 'e')
# print('4', (row, col), grid[row][col], i)
# print('5', (row, col), grid[row][col], i)

# clip_primes(zigzag_traverse_and_primes(a))

# up_right = True
# down_left = False

# result = {}
# print(len(grid) * len(grid[0]))
# print('1', (row, col), grid[row][col])



if is_prime((grid[row][col])) :
# {
    result = {
                i : grid[row][col]
            }
    
    i = i + 1
# }

else :
# {
    None
# }

# print(a, matrix[row][col], is_prime(matrix[row][col]))

while (row < len(matrix) and col < len(matrix[0]) and len(visited) != len(matrix) * len(matrix[0])) :
# {
    # up-right
    while(up_right and len(visited) != len(matrix) * len(matrix[0])) :
    # {
        if (row > 0 and col < len(matrix[0]) - 1) :
        # {
            row = row - 1
            col = col + 1
            visited.append(matrix[row][col])

            if is_prime((matrix[row][col])) :
            # {
                result[i] = matrix[row][col]
                print('1', i, matrix[row][col])
                i = i + 1
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
            visited.append(matrix[row][col])

            if is_prime((matrix[row][col])) :
            # {
                result[i] = matrix[row][col]
                print('2', i, matrix[row][col])
                i = i + 1
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
            visited.append(matrix[row][col])
            
            if is_prime((matrix[row][col])) :
            # {
                result[i] = matrix[row][col]
                print('3', i, matrix[row][col])
                i = i + 1
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
            visited.append(matrix[row][col])
            
            if is_prime((matrix[row][col])) :
            # {
                result[i] = matrix[row][col]
                print('4', i, matrix[row][col])
                i = i + 1
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
            visited.append(matrix[row][col])
            
            if is_prime((matrix[row][col])) :
            # {
                result[i] = matrix[row][col]
                print('5', i, matrix[row][col])
                i = i + 1
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
            visited.append(matrix[row][col])
            
            if is_prime((matrix[row][col])) :
            # {
                result[i] = matrix[row][col]
                print('6', i, matrix[row][col])
                i = i + 1
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
            visited.append(matrix[row][col])
            
            if is_prime((matrix[row][col])) :
            # {
                result[i] = matrix[row][col]
                print('7', i, matrix[row][col])
                i = i + 1
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
            visited.append(matrix[row][col])
            
            if is_prime((matrix[row][col])) :
            # {
                result[i] = matrix[row][col]
                print('8', i, matrix[row][col])
                i = i + 1
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
            visited.append(matrix[row][col])
            
            if is_prime((matrix[row][col])) :
            # {
                result[i] = matrix[row][col]
                print('9', i, matrix[row][col])
                i = i + 1

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
            visited.append(matrix[row][col])
            
            if is_prime((matrix[row][col])) :
            # {
                result[i] = matrix[row][col]
                print('10', i, matrix[row][col])
                i = i + 1
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

print(visited)

You can create a new dictionary by unpacking an existing dictionary and adding new key-value pairs. This is useful when you want to avoid modifying the original dictionary.
Python

original_dict = {"a": 1, "b": 2}
new_dict = {**original_dict, "c": 3, "d": 4}
print(new_dict)
print(original_dict) # Original dictionary remains unchanged

'''