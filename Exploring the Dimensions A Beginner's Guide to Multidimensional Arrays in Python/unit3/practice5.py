'''

Time to apply what you've learned about transposing matrices! Imagine you are assisting in redesigning the seating arrangement of a restaurant to better accommodate guests. Your task is to write Python code from scratch, which takes an initial seating arrangement (a 2D list) and transposes it. Remember, transposing switches the rows and columns, creating a new perspective on seating.

'''

# TODO: Define a function 'transpose_seating' that takes a 2D list 'arrangement' as its parameter.
def transpose_seating(arrangement) :
# {
    total_rows = len(arrangement)
    total_columns = len(arrangement[0])

    # TODO: Create a new 2D list 'transposed' with dimensions swapped (columns become rows and vice versa) filled initially with zeros.
    result = [0] * total_columns

    for i in range(total_columns) :
    # {
        result[i] = [0] * total_rows
    # }

    # print(len(result), len(result[0]))

    # TODO: Use nested loops to transpose each element from the original seating arrangement to the new arrangement 'transposed'.
    for i in range(total_rows) :
    # {
        for j in range(total_columns) :
        # {
            result[j][i] = arrangement[i][j]
        # }

    # }

    return result

# }

# Restaurant seating before transposition (rows)
seating_before = [
                    [1, 2],
                    [3, 4],
                    [5, 6]
                    ]

# TODO: Print the 'transposed' arrangement to see the new seating arrangement.
print(transpose_seating(seating_before))

'''

***** BONEYARD *****

print(result)

    

'''