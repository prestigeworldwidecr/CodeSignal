"""

Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.

"""

import sys

def maxLengthString(inputArray) :
# {
    i = 0
    tmp = None
    max = sys.maxsize * -1

    for i in range(0, len(inputArray)) :
    # {
        tmp = len(inputArray[i])

        if (tmp > max) :
        # {
            max = tmp
        # }

        else :
        # {
            "do nothing"
        # }

    # }

    return max

# }

def solution(inputArray) :
# {
    i = 0
    mls = maxLengthString(inputArray)
    result = []

    for i in range(0, len(inputArray)) :
    # {
        if (len(inputArray[i]) == mls) :
        # {
            result.append(inputArray[i])
        # }

        else :
        # {
            "do nothing"
        # }

    # }

    return result
# }

inputArray = ["aba", "aa", "ad", "vcd", "aba"]  # , the output should be
print(solution(inputArray)) # = ["aba", "vcd", "aba"]

"""

########
BONEYARD
########

# print(mls, inputArray[i])
        
        # print(tmp)

"""