"""

Reversing an array can be a tough task, especially for a novice programmer. Mary just started coding, so she would like to start with something basic at first. Instead of reversing the array entirely, she wants to swap just its first and last elements.

Given an array arr, swap its first and last elements and return the resulting array.

Example

For arr = [1, 2, 3, 4, 5], the output should be
solution(arr) = [5, 2, 3, 4, 1].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer arr

Guaranteed constraints:
0 ≤ arr.length ≤ 50,
-104 ≤ arr[i] ≤ 104.

[output] array.integer

Array arr with its first and its last elements swapped.

"""

def solution(arr) :
# {
    if (len(arr) == 0) :
    # {
        None    
    # }

    else :
    # {
        tmp1 = arr[0]
        tmp2 = arr[len(arr) - 1]
        arr[0] = tmp2
        arr[len(arr) - 1] = tmp1 
    # }

    return arr

# }

# For arr = [1, 2, 3, 4, 5], the output should be solution(arr) = [5, 2, 3, 4, 1].
arr = [1, 2, 3, 4, 5]
arr = []
print(solution(arr))

"""

********
BONEYARD
********

"""