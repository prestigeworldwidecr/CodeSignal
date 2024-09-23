"""

Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
solution(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
solution(n) = 0.

There are no ways to represent n = 8.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 104.

[output] integer

"""

def solution(n) :
# {
    i = 1
    j = 2
    # top = n // 2 + 1
    cnt = 0
    
    while (i < n) :
    # {
        print(i, j)
        i = i + 1
        j = j + 1

        if (i + j == n) :
        # {
            cnt = cnt + 1
        # }

        # elif (j )

        else :
        # {
            None
        # }
    # }

    return cnt * 2
# }

# For n = 9, the output should be solution(n) = 2.
# For n = 8, the output should be solution(n) = 0.
n = 9
# n = 8

print(solution(n))

"""

********
BONEYARD
********

for i in range(1, n // 2 + 1) :
    # {
        for j in range(2, n // 2 + 1) :
        # {
            print(i, j)
            i = i + 1
            j = j + 2
        # }

        
    # }

"""