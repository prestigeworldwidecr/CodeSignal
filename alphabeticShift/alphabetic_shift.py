"""

Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.


"""

import numpy

def alphabetic_shift(inputString) :
# {
    cur = -1
    tmp = numpy.zeros(len(inputString), str)
    result = ""

    for i in range(len(inputString)) :
    # {
        cur = ord(inputString[i])

        if (cur == 122) :
        # {
            tmp[i] = 'a'
        # }

        elif (97 <= cur and cur <= 121) :
        # {
            cur = cur + 1
            tmp[i] = chr(cur)
        # }

        else :
        # {
            None
        # }

    # }

    for i in tmp :
    # {
        result = result + i
    # }

    return result
# }

def solution(inputString) :
# {
    return alphabetic_shift(inputString)
# }

# For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

inputString = "crazy"
# print(solution(inputString))

"""

********
BONEYARD
********

# print(i)
# result = str(result).replace('[', '')
# print("!", cur)
# print('@', chr(cur), i, result[i])
# result = result + chr(cur)
# print(result, len(result))
# from numpy import ndarray

"""