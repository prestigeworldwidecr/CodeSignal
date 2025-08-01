'''

In the land of books and libraries, a challenge awaits you, Space Explorer! You have a grid that represents a library's bookshelf. Your mission is to traverse this bookshelf in a unique pattern, starting from the bottom right corner and moving in a zig-zag manner, visiting every book. However, there appears to be a mistake causing the traversal to behave unexpectedly. Can you identify and correct it to ensure the bookshelf is traversed correctly? Good luck in restoring order to the library!

Example

Given the following library grid:

library = [
            [1, 3, 5, 7],
            [2, 4, 6, 8],
            [9, 11, 13, 15]
        ]

inital: 15 8 7 5 3 1
goal:   15 8 7 5 6 13 11 4 3 1 2 9  

'''

library = [
            [1, 3, 5, 7],
            [2, 4, 6, 8],
            [9, 11, 13, 15]
        ]

# Starting from the bottom right corner of the bookshelf
current_row = len(library) - 1
current_col = len(library[0]) - 1
going_up = True

while (0 <= current_col and 0 <= current_row) :
# {
    print(library[current_row][current_col], ' ')

    if (going_up == True) :
    # {
        if (current_row == 0) :
        # {
            going_up = False
            current_col = current_col - 1
        # }

        else :
        # {
            current_row = current_row - 1
        # }

    else :
    # {
        if (current_row == (len(library) - 1)) :
        # {
            going_up = True
            current_col = current_col - 1
        # }

        else:
        # {
            current_row = current_row + 1
        # }

    # }

# }

'''

***** BONEYARD *****

 # or current_row == (len(library) - 1)) :

 # while(not(current_col == 0 and current_row == 0)) :
    # while (cnt < 15) :
    # cnt = cnt + 1

    # print(going_up, '\t', current_row, '\t', current_col, '\t', library[current_row][current_col])

        # print('!', going_up)

cnt = 0

print("going_up:", "current_row\t", "current_col\t", "current_val")
print("---------", "-----------\t", "-----------\t", "-----------")


'''