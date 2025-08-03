'''

Great job on understanding the basics of matrix transposition! Now, I'd like you to apply that knowledge in a new context. Imagine we're organizing a special event at a local restaurant and need to rearrange the seating to accommodate guest preferences. Your task is to write a piece of code that will transpose the given seating arrangement matrix. Remember, transposing involves converting rows into columns and vice versa.

'''

def transposeRestaurantSeating(seatingArrangement) :
# {
    # one-liner transposition to be implemented
    total_rows = len(seatingArrangement)
    total_columns = len(seatingArrangement[0])
    result = [0] * total_columns

    for i in range(total_columns) :
    # {
        result[i] = [0] * total_rows
    # }

    for i in range(total_rows) :
    # {
        for j in range(total_columns) :
        # {
            result[j][i] = seatingArrangement[i][j]
        # }

    # }

    return result

# }

# Example Seating Arrangement
original_seating = [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]

# TODO: Call the function to transpose the seating and print each row of the transposed seating.

print(transposeRestaurantSeating(original_seating))

'''

***** BONEYARD *****

'''