"""

You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-105 ≤ inputArray[i] ≤ 105.

[output] integer

The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.

"""

def makeStrictlyIncreasing(inputArray) :
# {
    # i = 0
    inc = 0    # necessary increment ("move")
    # max = inputArray[i]
    max = inputArray[0]
    result = 0

    # print(len(inputArray))

    for i in range(len(inputArray) - 1) :
    # {
        # max = inputArray[i] > max ? inputArray[i] : max
        # max if inputArray[i] < max else inputArray[i]
        # print(max, i)
        
        if (inputArray[i] > max) :
        # {
            max = inputArray[i]
        # }
        
        else :
        # {
            None
        # }
         
        if (inputArray[i] < inputArray[i + 1]) :
        # {
            None
        # }

        else :
        # {
            inc = max - inputArray[i + 1] + 1
            inputArray[i + 1] = max + 1            
            result = result + inc
        # }

    # }

    return result
# }

def solution(inputArray) :
# {
    return makeStrictlyIncreasing(inputArray)
# }

# For inputArray = [1, 1, 1], the output should be solution(inputArray) = 3.
inputArray = [1, 1, 1]
print("!", solution(inputArray))

"""

********
BONEYARD
********

    a "move" is an increment of one on any given number
    in the example, 3rd element '3' needs an increase of 2

"""