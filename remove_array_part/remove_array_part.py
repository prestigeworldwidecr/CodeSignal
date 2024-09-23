"""

Remove a part of a given array between given 0-based indexes l and r (inclusive).

Example

For inputArray = [2, 3, 2, 3, 4, 5], l = 2, and r = 4, the output should be
solution(inputArray, l, r) = [2, 3, 5].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer inputArray

Guaranteed constraints:
2 ≤ inputArray.length ≤ 104,
-105 ≤ inputArray[i] ≤ 105.

[input] integer l

Left index of the part to be removed (0-based).

Guaranteed constraints:
0 ≤ l ≤ r.

[input] integer r

Right index of the part to be removed (0-based).

Guaranteed constraints:
l ≤ r < inputArray.length.

[output] array.integer

"""

def solution(inputArray, l, r) :
# {
    # print(inputArray[0:l], inputArray[r + 1:len(inputArray)])
    # return inputArray[0:l]
    return inputArray[0:l] + inputArray[r + 1:len(inputArray)]
# }

# For inputArray = [2, 3, 2, 3, 4, 5], l = 2, and r = 4, the output should be solution(inputArray, l, r) = [2, 3, 5].

inputArray = [2, 3, 2, 3, 4, 5]
l = 2
r = 4

print(solution(inputArray, l, r))

"""

********
BONEYARD
********

"""