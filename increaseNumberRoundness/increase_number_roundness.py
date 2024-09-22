"""

Define an integer's roundness as the number of trailing zeroes in it.

Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.

Example

For n = 902200100, the output should be
solution(n) = true.

One of the possible ways to increase roundness of n is to swap digit 1 with digit 0 preceding it: roundness of 902201000 is 3, and roundness of n is 2.

For instance, one may swap the leftmost 0 with 1.

For n = 11000, the output should be
solution(n) = false.

Roundness of n is 3, and there is no way to increase it.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

A positive integer.

Guaranteed constraints:
100 ≤ n ≤ 109.

[output] boolean

true if it's possible to increase n's roundness, false otherwise.

"""

import sys

def swap_digits(n, i, j) :  # num, left index of swap
# {
    tmp = list(str(n))
    tmp1 = tmp[i]
    tmp2 = tmp[j]
    tmp[i] = tmp2
    tmp[j] = tmp1
    
    # print(tmp)

    return tmp
# }

def count_max_consecutive_zeroes(l) :
# {
    cnt = 0
    max = -sys.maxsize

    for i in range(len(l)) :
    # {

        if (l[i] == '0') :
        # {
            cnt = cnt + 1
        # }

        else :
        # {
            if (cnt > max) :
            # {
                max = cnt
            # }

            else :
            # {
                None
            # }

            cnt = 0

        # }

    # }

    return cnt

# }

def solution(n) :
# {
    og = count_max_consecutive_zeroes(swap_digits(n, 0, 0))    # original roundness

    for i in range(len(str(n))) :
    # {
        for j in range(1, len(str(n))):
        # {
            if (i != j) :
            # {
                tmp = count_max_consecutive_zeroes(swap_digits(n, i, j))
                print(i, j, og, tmp)
                
                if (tmp > og) :
                # {
                    return True
                # }

                else :
                # {
                    None
                # }

            # }

            else :
            # {
                None
            # }

        # }

    # }

    return False

# }

# For n = 902200100, the output should be solution(n) = true.
# For n = 11000, the output should be solution(n) = false.
# n = 902200100
# n = 11000
n = 1022220

print(solution(n))
# print(count_max_consecutive_zeroes(swap_consecutive_digits(n, 5)))

"""

********
BONEYARD
********

# swap
# count max consecutive zeros

def swap_consecutive_digits(n, i) :  # num, left index of swap
# {
    tmp = list(str(n))
    tmp1 = tmp[i]
    tmp2 = tmp[i + 1]
    tmp[i] = tmp2
    tmp[i + 1] = tmp1

    return tmp
# }

# print(i, j, swap_digits(n, i, j))
# max = -sys.maxsize

    # print(og)
    og = count_max_consecutive_zeroes(swap_consecutive_digits(n, 0))    # original roundness
    max = -sys.maxsize

    for i in range(1, len(str(n)) - 1) :
    # {
        tmp = count_max_consecutive_zeroes(swap_consecutive_digits(n, i))
        # print(max, tmp)

        if (tmp > max) :
        # {
            max = tmp
        # }

        else :
        # {
            None
        # }

    # }

    print(og, max)

    if (og >= max) :
    # {
        return False
    # }

    else :
    # {
        return True
    # }

# tmp = count_max_consecutive_zeroes(swap_consecutive_digits(n, 0))

    # print(len(str(n)))

# print(l[i])
        # print(len(l))
    

    # print(tmp)

"""