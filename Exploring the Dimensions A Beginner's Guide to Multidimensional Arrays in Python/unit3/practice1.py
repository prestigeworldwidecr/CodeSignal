'''

Wonderful progress, Space Voyager! Here's a practical task involving the restaurant seating arrangements you've been learning about. Your task is to fix a minor error in the code that's supposed to transpose the seating arrangement of a restaurant. However, the output isn't as expected. Review the code carefully and adjust it to ensure it accurately transposes the matrix. Good luck!

'''

import math, numpy

# A function to transpose a matrix representing restaurant seating arrangement
def transpose_seating(seating) :
# {
    # rows, cols = len(seating), len(seating[0])
    total_rows = len(seating)
    total_columns = len(seating[0])
    result = [0] * total_columns
    
    for i in range(total_columns) :
    # {        
        result[i] = [0] * total_rows
    # }

    for i in range(total_rows) :
    # {
        for j in range(total_columns) :
        # {
            result [j][i] = seating [i][j]
        # }

    # }   

    return result

# }

# Sample restaurant seating arrangement represented as a 2D matrix
restaurant_seating = [
                        [10, 11, 12],
                        [20, 21, 22]
                    ]

# Trying to transpose the seating arrangement
transposed_seating = transpose_seating(restaurant_seating)
print(transposed_seating)  # Output isn't as expected. Can you identify the fix?

'''

***** BONEYARD *****

 # total_rows - i - 1

# print(i, j, seating [i][j], seating [j][j])
            # None

# result = [[0] * total_rows] * total_columns   # [[element] * numcols] * numrows
    # result = [[], []]
    # print(result)

    # print(result)

# result = [None] * total_columns
    # result[0] = [None] * total_rows

result = numpy.zeros((total_columns, total_rows))

# result = [None] * total_columns
    # result[0] = [None] * total_rows

result = numpy.zeros((total_columns, total_rows))
    i = 0
    j = 0
    k = total_rows - 1
    l = total_columns - 1

    # result = [total_columns] * [total_rows]
    # len(result) = total_columns
    # len(result[0]) = total_rows


    # return [[seating[i][j] for j in range(rows)] for i in range(cols)]
    


    
    print(result)
    print("result[i][j]" , "seating[k][l]" , 'i', 'j', 'k', 'l')

    for _ in range(math.floor(total_rows * total_columns / 2)) :
    # {
        result[i][j] = seating[k][l]

        print(result[i][j], seating[k][l], i, j, k, l)

        i = i + 1
        j = j + 1
        k = k - 1
        l = l - 1
    # } 
     

'''