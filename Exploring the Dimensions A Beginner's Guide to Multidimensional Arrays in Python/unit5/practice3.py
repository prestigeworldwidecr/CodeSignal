'''

Great job navigating the peaks and valleys of our trail map. Ready for a new challenge? Your task is to find the next higher peak based on the hiker's current position. Consider directions carefully as you craft your solution. Remember, the peak must be higher than the hiker's current elevation. Let's see where the next adventure takes us!

'''

def findNextPeak(matrix, row, col) :
# {
    total_rows = len(matrix)
    total_columns = len(matrix[0])

    # TODO: Define directions for hiker's movement (East, West, South, North)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    current_height = matrix[row][col]
    max_row = row
    max_column = col

    for dr, dc in directions :
    # {
        r = row + dr
        c = col + dc

        # TODO: Check if the new position is within bounds and higher than the current
        if (0 <= r < total_rows and 0 <= c < total_columns and matrix[r][c] > current_height) :  # Fill in the condition
        # {
            current_height = matrix[r][c]
            max_row = r
            max_column = c
        # }

        else :
        # {
            None
        # }

    # }

    # return (row, col)  # No higher peak, stay in place
    return (max_row, max_column)

# }

# Hiking exploration example where the hiker looks for a higher peak around
trail_map = [
            [3, 5, 6],
            [4, 7, 8],
            [1, 2, 9]
        ]

start_position = (1, 1)  # Starting at elevation 7
next_peak = findNextPeak(trail_map, start_position[0], start_position[1])
print("Next peak at coordinates:", next_peak)

'''

***** BONEYARD *****


            # return (r, c)  # Return coordinates of the next higher peak
            
           
            # print((r, c), matrix[r][c], current_height)

'''