'''

Fantastic progress! Now, let's adjust our scope a bit and focus on a simpler traversal pattern that aligns with what we've learned. Your task is to append each book's position from our library bookshelves to the result list. This time, however, let's simplify the process to a vertical traverse starting from the bottom right. This approach closely aligns with our lesson on traversals, making it more accessible and directly applicable for you.

'''

def vertical_traverse(matrix) :
# {
    if (len(matrix) == 0 or len(matrix[0]) == 0) :
    # {
        return []
    # }

    # rows, cols = len(matrix), len(matrix[0])
    total_rows = len(matrix)
    total_columns = len(matrix[0])

    # We start at the bottom right for the vertical traversal.
    # row, col = rows - 1, cols - 1
    current_row = total_rows - 1
    current_col = total_columns - 1
    result = []

    # TODO: Append each book's position to the result list by following the vertical pattern.
    for _ in range(total_rows * total_columns) :
    # {
        result.append(matrix[current_row][current_col])

        if (current_row == 0) :
        # {
            current_row = total_rows - 1
            current_col = current_col - 1
        # }

        else :
        # {
            current_row = current_row - 1
        # }

    # }

    return result

# }

# Example matrix representing library bookshelves
bookshelves = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]
            ]

# Output should be the vertical traverse of the bookshelves
print(vertical_traverse(bookshelves))  # [12, 8, 4, 11, 7, 3, 10, 6, 2, 9, 5, 1]

'''

***** BONEYARD *****

'''