"""

Given an integer size, return array of length size filled with 1s.

Example

For size = 4, the output should be
solution(size) = [1, 1, 1, 1].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer size

A positive integer.

Guaranteed constraints:
1 ≤ size ≤ 1000.

[output] array.integer

"""

def solution(size) :
# {
    result = []

    for i in range(size) :
    # {
        # print(i)
        result.append(1)
    # }

    return result

# }

# For size = 4, the output should be solution(size) = [1, 1, 1, 1].
size = 4

print(solution(size))

"""

********
BONEYARD
********

"""