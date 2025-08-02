'''

Great job navigating through our library's bookshelves! Now, let's apply what you've learned by focusing on a crucial aspect of the task. In this practice, you need to define how we switch directions and move left when we reach the top or bottom of our bookshelf. Remember, the books on these shelves are organized in a unique pattern. Can you implement this specific part?

'''

def column_traverse(matrix) :
# {    
    # rows, cols = len(matrix), len(matrix[0])
    rows = len(matrix)
    cols = len(matrix[0])

    # row, col = rows - 1, cols - 1
    current_row = rows - 1
    current_col = cols - 1

    direction = -1  # Start going upwards
    output = []

    for _ in range(rows * cols) :
    # {
        output.append(matrix[current_row][current_col])

        # TODO: Implement logic to change direction and move left when hitting the top or bottom of the shelf
        if (current_row == 0 and direction == -1) or (current_row == rows - 1 and direction == 1) :
        # {
            direction = direction * -1
            current_col = current_col - 1
        # }

        else :  # Otherwise, continue moving in the same direction
        # {
            current_row = current_row + direction
        # }

    # }

    return output

# }

# Example matrix resembling a bookshelf (3 shelves, 4 books each)
bookshelf = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]
            ]

print(column_traverse(bookshelf))

'''

***** BONEYARD *****

'''