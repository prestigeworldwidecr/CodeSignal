"""

Determine if the given number is a power of some non-negative integer.

Example

For n = 125, the output should be
solution(n) = true;
For n = 72, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 400.

[output] boolean

true if n can be represented in the form ab (a to the power of b) where a and b are some non-negative integers and b ≥ 2, false otherwise.

"""

import math

def solution(n) :
# {
    top = math.ceil(math.pow(n, .5)) + 1

    for i in range(1, top) :
    # {
        for j in range(1, top) :
        # {
            print(j, i, math.pow(j, i))
            
            if (math.pow(j, i) == n) :
            # {
                return True
            # }

            else :
            # {
                None
            # }

        # }

    # }

    return False
    
# }

# For n = 125, the output should be solution(n) = true;
# For n = 72, the output should be solution(n) = false.

n = 125
n = 72
n = 100

print(solution(n))

"""

********
BONEYARD
********


    # print(math.pow(n, .5))
    # print(math.pow(125, .5), math.pow(15, 2))
    # return isinstance(math.pow(n, .5), int)
# tmp = math.pow(j, i)
            # tmp = str(tmp).split('.')
            # print(tmp[1])

"""