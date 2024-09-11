"""

Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
solution(product) = 26;
For product = 19, the output should be
solution(product) = -1.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer product

Guaranteed constraints:
0 ≤ product ≤ 600.

[output] integer

"""

import math
import sys

# determine all multiples
# find min

def solution(product) :
# {
    min = sys.maxsize

    for i in range(2, math.ceil(product / 2)) :
    # {
        if ((product / i) % 1 == 0) :
        # {
            tmp = int(str(i) + str(int(product / i)))
            
            if (tmp < min) :
            # {
                min = tmp
            # }

            else :
            # {
                None
            # }

        # }

        else :
        # {
            None
        # }

    # }

    if (min == sys.maxsize) :
    # {
        min = -1
    # }

    else :
    # {
        None
    # }

    return min

# }

# For product = 12, the output should be solution(product) = 26;
# For product = 19, the output should be solution(product) = -1.
product = 12
# product = 19

print(solution(product))

"""

********
BONEYARD
********

# print(math.ceil(product / 2))
            # print('!', product / i)
            # print('!', i, int(product / i))

"""