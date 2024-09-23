"""

We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;

if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.

Given array arr, your task is to find its middle, and, if it consists of two elements, replace those elements with the value of middle. Return the resulting array as the answer.

Example

For arr = [7, 2, 2, 5, 10, 7], the output should be
solution(arr) = [7, 2, 7, 10, 7].

The middle consists of two elements, 2 and 5. These two elements should be replaced with their sum, i.e. 7.

For arr = [-5, -5, 10], the output should be
solution(arr) = [-5, -5, 10].

The middle is defined as a single element -5, so the initial array with no changes should be returned.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer arr

The given array.

Guaranteed constraints:
2 ≤ arr.length ≤ 104,
-103 ≤ arr[i] ≤ 103.

[output] array.integer

arr with its middle replaced by a single element, or the initial array if the middle consisted of a single element to begin with.

"""

import sys

def solution(arr) :
# {
    mid = -sys.maxsize
    
    if (len(arr) % 2 == 0) :
    # {
        mid = arr[len(arr) // 2 - 1] + arr[(len(arr) // 2)]
        arr[len(arr) // 2 - 1] = mid
        del arr[(len(arr) // 2)]

        return arr
    # }

    else :
    # {
        return arr
    # }

# }

# For arr = [7, 2, 2, 5, 10, 7], the output should be solution(arr) = [7, 2, 7, 10, 7].
# For arr = [-5, -5, 10], the output should be solution(arr) = [-5, -5, 10].
arr = [7, 2, 2, 5, 10, 7]
# arr = [-5, -5, 10]

print(solution(arr))

"""

********
BONEYARD
********
        print(arr[len(arr) // 2], arr[0], arr[len(arr) - 1], int((arr[0] + arr[len(arr) - 1]) / 2))

        if ( int((arr[0] + arr[len(arr) - 1]) / 2) == arr[len(arr) // 2]) :
        # {
            return True
        # }

        else :
        # {
            return False
        # }

"""