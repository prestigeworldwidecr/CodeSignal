'''

You've made it to the final challenge of this lesson, Space Explorer! It's time to showcase your skills with arrays. Your task involves writing a function that simulates a unique traversal across a library's bookshelves, moving through the collection in a zigzag pattern. Remember to start from the bottom right and zigzag up and down each column. To the code editor!

'''

def bookshelfTraversal(bookshelves):
# {    
    # TODO: Determine the number of rows and columns in 'bookshelves'
    total_rows = len(bookshelves)
    total_columns = len(bookshelves[0])
    current_row = total_rows - 1
    current_column = total_columns - 1
    direction = -1
    traversal_path = []
    
    # TODO: Traverse the bookshelves using a zigzag pattern; start from the bottom right
    for _ in range(total_rows * total_columns) :
    # {
        traversal_path.append(bookshelves[current_row][current_column])
        
        if((current_row == 0 and direction == -1) or (current_row == total_rows - 1 and direction == 1))  :
        # {
            direction = direction * -1
            current_column = current_column - 1
        # }

        else :
        # {
            current_row = current_row + direction
        # }

    # }


    return traversal_path
# }

# TODO: Create a 2x4 'bookshelves' variable with unique numbers representing books
bookshelves = [
                [1, 2, 3, 4],
                [5, 6, 7, 8]
            ]

# TODO: Print the traversal path of the books
print(bookshelfTraversal(bookshelves))

'''

***** BONEYARD *****

# current_row = total_rows - 1

'''