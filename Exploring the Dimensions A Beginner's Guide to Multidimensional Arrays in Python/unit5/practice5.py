'''

You're on the final stretch of mastering grid traversal, Space Voyager! Imagine you're hiking in the mountains, tasked with finding the path that keeps you ascending. Your mission is to write a Python function named path_traverse that traverses a given matrix, always moving to an adjacent cell with a higher value. Begin your coding journey with the given starter code and follow the instructions in the TODO comments. This challenge will test your ability to work with two-dimensional arrays and navigate through them efficiently. Happy coding, and watch your step!

'''

def inbounds(matrix, x, y) :
# {
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) - 1
# }

# TODO: Define the path_traverse function that takes a matrix of "heights" and the current position as parameters. It should return the next step's position if a higher value is found, or None if there's no higher adjacent value.
def path_traverse(heights, x, y) :
# {
    adjacent = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    next_step = None
    cur_max = heights[x][y]

    for i in range(len(adjacent)) :
    # {
        next_x = x + adjacent[i][0]
        next_y = y + adjacent[i][1]

        if (inbounds(heights, next_x, next_y) and heights[next_x][next_y] > cur_max) :
        # {
            next_step = (next_x, next_y)
            cur_max = heights[next_x][next_y]
        # }

        else :
        # {
            None
        # }

    # }

    return next_step

# }

# Example matrix (mountain heights)
# TODO: Define a matrix named 'mountain' with ascending values, similar to hiking up a mountain
mountain = [[3, 1, 4], 
            [0, 6, 7],
            [3, 8, 4]
            ]

# TODO: Define the starting position on the mountain (you can use a tuple for row and column position)
starting_position = (2, 1)

# TODO: Use the path_traverse function to determine the next step from your starting position based on a higher adjacent value
next_step = path_traverse(mountain, starting_position[0], starting_position[1])

# TODO: Print out the next step's position or a message indicating that no higher step could be found
print(next_step)

'''

***** BONEYARD *****


    if (0 <= x < len(matrix) and 0 <= y < len(matrix) - 1) :
    # {
        
    # }

    else :
    # {
        return False
    # }

# print([next_step][0][1])

while(flag) :
    # {
        flag = False
        

    # }
        

    # cur_x = x
    # cur_y = y
    
    # flag = True    

    # cur_x = next_x
            # cur_y = next_y
            
flag = True

'''