"""

Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2, and r = 4, the output should be
solution(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

A positive integer.

Guaranteed constraints:
5 ≤ n ≤ 109.

[input] integer l

A positive integer.

Guaranteed constraints:
1 ≤ l ≤ r.

[input] integer r

A positive integer.

Guaranteed constraints:
l ≤ r ≤ 109,
r - l ≤ 106.

[output] integer

"""

def solution(n, l, r) :
# {
    a = l
    b = r
    result = list()

    if (l == r and l + r == n) :
    # {
        return 1
    # }
    
    else :
    # {
        for i in range(a, b) :
        # {
            for j in range(b - 1, n) :
            # {
                print(i, j, i + j)
                if (i + j == n) :
                # {
                    result.append([i, j])
                # }

                else :
                # {
                    None
                # }

            # }

        # }

    # }

    return len(result)

# }

n = 6
l = 2
r = 4
# n = 93
# l = 24
# r = 58
n = 6
l = 3
r = 3
n = 24
l = 8
r = 16  # solution == 5

print(solution(n, l, r))

"""

********
BONEYARD
********

def all_pair_combinations(n, l, r) :
# {
    a = l
    b = r
    result = list()
    
    for i in range(a, b) :
    # {
        for j in range(b, n) :
        # {
            # print(i, j, i + j)
            if (i + j == n) :
            # {
                result.append([i, j])
            # }

            else :
            # {
                None
            # }

        # }

    # }

    print(result)

# }

a = l
    b = r
    cnt = 0
    
    for i in range(l, r) :
    # {
        print (a, b)

        if (a + b == n) :
        # {
            cnt = cnt + 1
        # }

        else :
        # {
            None
        # }

        a = a + 1
        b = b - 1

    # }

    return cnt

"""