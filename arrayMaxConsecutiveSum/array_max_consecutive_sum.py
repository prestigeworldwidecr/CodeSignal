"""

Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer inputArray

Array of positive integers.

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
1 ≤ inputArray[i] ≤ 1000.

[input] integer k

An integer (not greater than the length of inputArray).

Guaranteed constraints:
1 ≤ k ≤ inputArray.length.

[output] integer

The maximal possible sum.

"""

import sys

def consecutive_max_in_array(inputArray, k, sum, i) :
# {
    if (k == 0 or i > len(inputArray) - 1) :
    # {
        return sum
    # }
    
    else :
    # {
        sum = sum + inputArray[i]
        k = k - 1
        i = i + 1
        print(inputArray, inputArray[k], sum, k)
        return consecutive_max_in_array(inputArray, k, sum, i)
    # }

# }

def solution(inputArray, k) :
# {
    tmp = 0
    max = -sys.maxsize
    
    for i in range(len(inputArray) - 1) :
    # { 
        tmp = consecutive_max_in_array(inputArray, k, 0, i)

        if (max < tmp) :
        # {
            max = tmp
        # }

        else :
        # {
            None
        # }
        
    # }

    return max
# }

# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be solution(inputArray, k) = 8.
inputArray = [2, 3, 5, 1, 6] 
k = 2
inputArray = [1, 3, 2, 4]
k = 3

print(solution(inputArray, k))

"""

********
BONEYARD
********
# print(tmp)
# print(inputArray, inputArray[k], sum, k)
def find_then_delete_max(inputArray, k) :
# {
    

# }

result = 0
    
    for i in range(k) :
    # {
        result = result + max(inputArray)
        del inputArray[inputArray.index(max(inputArray))]
        print(i, result, inputArray)
    # }

    return result

import numpy as np
# for i in range(len(inputArray)) :
a = max(inputArray)
# a = int(a)
# del(inputArray)
arr = np.array(inputArray)
result = np.where(arr == a)

return str(result[0]).replace('[', '')

"""