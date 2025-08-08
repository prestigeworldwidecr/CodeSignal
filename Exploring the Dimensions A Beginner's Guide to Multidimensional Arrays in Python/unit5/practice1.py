'''

In our hiking trail navigation exercise, you modified the code to find the next uphill value. This time, enhance your function by considering diagonal moves to capture the richness of possible paths. Modify the directions list to include diagonal directions in addition to the current cardinal directions. Ready to expand your path-finding capabilities?

'''

# Function which takes a grid and a start position. 
# It then finds and returns the next cell's value going uphill.
def find_next_uphill(grid, position) :
# {
    row, col = position
    # Up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
    next_val = grid[row][col]

    for direction_row, direction_col in directions :
    # {
        new_r, new_c = row + direction_row, col + direction_col

        if (0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] > next_val) :
        # {
            next_val = grid[new_r][new_c]
        # }

        else :
        # {
            None
        # }

    # }

    # return next_val if next_val != grid[row][col] else None
    if (next_val == grid[row][col]) :
    # {
        None
    # }

    else :
    # {
        return next_val
    # }

# }

# Example usage:
trail_grid = [[1, 2, 3], 
              [6, 5, 8],
              [7, 4, 9]]  # Representing a hiking trail

start_position = (1, 1)  # value: 5 Starting in the middle of the grid

# Prints the value uphill from the start position or None if there's no uphill
print(find_next_uphill(trail_grid, start_position))

'''

***** BONEYARD *****

'''