"""

Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 10,
-15 ≤ inputArray[i] ≤ 15.

[output] integer

The maximal absolute difference.

"""

import sys

def solution(inputArray) :
# {
    # i = 0
    pair = [inputArray[0], inputArray[1]]
    mini = min(pair)
    maxi = max(pair)
    tmp = -sys.maxsize
    mad = -sys.maxsize # Maximal Adjacent Difference
    
    for i in range(len(inputArray) - 1) :
    # {
        pair = [inputArray[i], inputArray[i + 1]]
        mini = min(pair)
        maxi = max(pair)
        tmp = maxi - mini

        if (tmp > mad) :
        # {
            mad = tmp
        # }

        else :
        # {
            None
        # }

    # }

    return mad

# }

# For inputArray = [2, 4, 1, 0], the output should be solution(inputArray) = 3.
inputArray = [2, 4, 1, 0]
print(solution(inputArray))

"""

********
BONEYARD
********

// console.log("pair: ", pair, " min: ", min, " max: ", max)
    // console.log("pair: ", pair, " min: ", min, " max: ", max, " tmp: ", tmp)
    // console.log(mad)

inputArray = [2, 4, 1, 0]  // 
solution(inputArray)

"""