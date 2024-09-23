"""

We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;

if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.

An array is called smooth if its first and its last elements are equal to one another and to the middle. Given an array arr, determine if it is smooth or not.

Example

For arr = [7, 2, 2, 5, 10, 7], the output should be
solution(arr) = true.

The first and the last elements of arr are equal to 7, and its middle also equals 2 + 5 = 7. Thus, the array is smooth and the output is true.

For arr = [-5, -5, 10], the output should be
solution(arr) = false.

The first and middle elements are equal to -5, but the last element equals 10. Thus, arr is not smooth and the output is false.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer arr

The given array.

Guaranteed constraints:
2 ≤ arr.length ≤ 105,
-109 ≤ arr[i] ≤ 109.

[output] boolean

true if arr is smooth, false otherwise.

"""

import sys

def solution(arr) :
# {
    mid = -sys.maxsize
    
    if (len(arr) % 2 == 0) :
    # {
        mid = arr[len(arr) // 2 - 1] + arr[(len(arr) // 2)]
        # print(mid, arr[0], arr[len(arr) - 1])
        
        if ( (arr[0] + arr[len(arr) - 1]) / 2 == mid) :
        # {
            return True
        # }

        else :
        # {
            return False
        # }

    # }

    else :
    # {
        
        print(arr[len(arr) // 2], arr[0], arr[len(arr) - 1], int((arr[0] + arr[len(arr) - 1]) / 2))

        if ( int((arr[0] + arr[len(arr) - 1]) / 2) == arr[len(arr) // 2]) :
        # {
            return True
        # }

        else :
        # {
            return False
        # }

    # }

# }

# For arr = [7, 2, 2, 5, 10, 7], the output should be solution(arr) = true.
# For arr = [-5, -5, 10], the output should be solution(arr) = false.
arr = [7, 2, 2, 5, 10, 7]
# arr = [-5, -5, 10]
arr = [3, 4, 5]  # false
# arr = [-5, 3, -1, 9]    # false


print(solution(arr))


"""

********
BONEYARD
********

# print('@', len(arr) // 2)
# print('!', len(arr) // 2)
        # print(arr[len(arr) // 2 - 1], arr[(len(arr) // 2)])
        # print(mid)

"""