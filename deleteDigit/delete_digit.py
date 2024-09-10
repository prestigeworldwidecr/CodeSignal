"""

Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
10 ≤ n ≤ 10^6.

[output] integer

"""

import sys

def solution(n) :
# {
    tmp = list(str(n))
    max = -sys.maxsize
    cur_number = 0
    cur_list = []

    for i in range(len(tmp)) :
    # {
        cur_list = tmp.copy()
        del cur_list[i]
        cur_number = int("".join(cur_list))

        if (cur_number > max) :
        # {
            max = cur_number
        # }

        else :
        # {
            None
        # }
        
    # }

    return max

# }

# For n = 152, the output should be solution(n) = 52;
# For n = 1001, the output should be solution(n) = 101.
n = 152
n = 1001

print(solution(n))

"""

********
BONEYARD
********

# print(i, cur_list, cur_number)

author: bandorthild
def solution(n):
    return max([int(str(n)[:i] + str(n)[i+1:]) for i in range(len(str(n)))])

author: ben_w6
int solution(int n)
{
    int max = 0;
    for (int t = 1; t < n; t *= 10)
        max = Math.max(n / 10 / t * t + n % t, max);
    return max;
}


author lucky-seven
def solution(n):
    n = str(n)
    return max(int(''.join(n[:i]+n[i+1:])) for i in range(len(n)))

def delete_digit(n) :
# {
    tmp = list(str(n))
    cur = int(tmp[0])
    next = int(tmp[1])
    result = ""
    flag = True

    if (len(tmp) == 2) :
    # {
        if (cur > next) :
        # {
            return cur
        # }

        else :
        # {
            return next
        # }

    # }

    else :
    # {
        None
    # }

    for i in range(len(tmp)) :
    # {
        print(i, i + 1, len(tmp), cur, len(tmp))
        
        cur = int(tmp[i])
        
        if (i == len(tmp) - 1) :
        # {
            # print(i)
            None
        # }

        else :
        # {
            next = int(tmp[i + 1])
        # }

        if (next > cur and flag) :
        # {
            flag = False
        # }

        else :
        # {
            result = result + str(cur)
        # }

    # }

    return int(result)

# }



"""