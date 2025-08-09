'''

In your latest hiking exploration project, you have written a program to identify the highest peak reachable from a starting point on a mountain. However, it appears there is an issue with the code, as it is not always returning the correct altitude of the highest peak reachable. Can you spot and fix the issue to ensure the mountain exploration is successful?

'''

# Given a grid representing a mountain terrain where each value represents altitude
# and a starting point, we'll find the highest peak reachable through adjacent steps.

def find_peak(grid, start_row, start_col) :
# {
    total_rows = len(grid) 
    total_columns = len(grid[0])
    altitude = grid[start_row][start_col]

    # Check North, East, South, West for higher altitude
    for direction_row, direction_column in [(-1, 0), (0, 1), (1, 0), (0, -1)] :
    # {
        r = start_row + direction_row
        c = start_col + direction_column

        if (0 <= r < total_rows and 0 <= c < total_columns and grid[r][c] > altitude) :
        # {
            altitude = grid[r][c]  # This line introduces a logical error
        # }

        else :
        # {
            None
        # }

    # }

    return altitude

# }

# Example mountain terrain grid
mountain = [
            [1, 2, 3],
            [2, 5, 7],
            [4, 6, 9]
        ]

# Starting at the base (0, 1) representing the beginning of the hike
print(find_peak(mountain, 0, 1))  # Should print the altitude of the highest peak reachable

'''

***** BONEYARD *****

'''