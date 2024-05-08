"""

Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.

"""

import sys

def solution (inputArray):
# {
    maxProduct = sys.maxsize * -1
    
    for i in range(0, len(inputArray) - 1) :
    # {
        tmp = inputArray[i] * inputArray[i + 1]

        if (tmp > maxProduct) :
        # {
            maxProduct = tmp
        # }

        else :
        # {
            "do nothing"
        # }

    # }

    return maxProduct

# }

inputArray = [3, 6, -2, -5, 7, 3]
print(solution(inputArray))

"""

########
BONEYARD
########

print("maxProduct: ", maxProduct, " tmp: ", tmp)

        # print(list(l_inputArray), " > ", next(l_inputArray))
        # l_inputArray = iter(inputArray)

    # print(next(l_inputArray))
    # print(next(l_inputArray))

    # print(list(next(l_inputArray)))

l = [1, 2, 3]
l_iter = iter(l)  
print(next(l_iter))

# print(maxProduct)

You can use a pairwise cyclic iterator:

from itertools import izip, cycle, tee

def pairwise(seq):
    a, b = tee(seq)
    next(b)
    return izip(a, b)

for elem, next_elem in pairwise(cycle(li)):

# print(inputArray)

"""