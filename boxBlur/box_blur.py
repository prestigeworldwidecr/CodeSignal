"""

Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be solution(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
the output should be

solution(image) = [[5, 4], 
                   [4, 4]]
There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output. To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.array.integer image

An image, stored as a rectangular matrix of non-negative integers.

Guaranteed constraints:
3 ≤ image.length ≤ 100,
3 ≤ image[0].length ≤ 100,
0 ≤ image[i][j] ≤ 255.

[output] array.array.integer

A blurred image represented as integers, obtained through the process in the description.

"""
import math

def run_blocks(image) :
# {
    row_length = len(image) - 2
    column_length = len(image[0]) - 2
    result = [ [ None for i in range(column_length) ] for j in range(row_length) ]
    tmp = -1

    for j in range(column_length) :
    # {
        i = 0

        for i in range(row_length) :
        # {
            print(j, i)
            tmp = [image[j][i : i + 3], image[j + 1][i : i + 3], image[j + 2][i : i + 3]]
            result[j][i] = avgof3x3(tmp)
        # }

    # }

    return result
# }

def avgof3x3(image) :
# {
    row_length = 3
    column_length = 3
    avg = -1
    sum = 0

    for j in range(column_length) :
    # {
        for i in range(row_length) :
        # {
            sum = sum + image[i][j]
        # }

    # }

    avg = sum / 9

    return math.floor(avg)
# }

def solution(image) :
# {
    return run_blocks(image)
# }

image = [[1, 1, 1], 
            [1, 7, 1], 
            [1, 1, 1]]    # the output should be solution(image) = [[1]]    

image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]] # the output should be solution(image) = [[5, 4], 
                        #                                         [4, 4]]

image = [[36,0,18,9], 
        [27,54,9,0], 
        [81,63,72,45]]

print(len(image), len(image[0]))
print(solution(image))

"""

********
BONEYARD
********

# print(j, i, avgof3x3(tmp), result)
# print(j, i, avgof3x3(tmp), result)
# result = [[0] * column_length] * row_length
# print(i, j, tmp, result[j])
# result[i] = avgof3x3(tmp)
# result[j] = [column_length]
# print(j, i, tmp, result[j][i], len(result))
# result[j][i] = avgof3x3(tmp)

# print(i, j, result[j])
# print(row_length, column_length)
# result = [row_length][column_length]

print("rowLength: ", " columnLength: " , row_length, column_length)
print("i\tj\tj\tj + 1\tj + 2\ti\ti + 3")
print("-\t-\t-\t-----\t-----\t-\t-----")
# print('!', row_length, column_length)
# print(j)
# print(image)

"""