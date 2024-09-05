"""

Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
solution(n) = 0;
For n = 100, the output should be
solution(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
5 ≤ n ≤ 109.

[output] integer

"""

def solution(n) :
# {
    # tmp = 0
    sum = 0

    if (n < 10) :
    # {
        return 0
    # }

    else :
    # {
        for i in str(n) :
        # {
            sum = sum + int(i)
        # }
    # }

    return solution(sum) + 1

# }

n = 5;  # the output should be solution(n) = 0;
# n = 100 # the output should be solution(n) = 1.
# n = 91  # the output should be solution(n) = 2.

print(solution(n))

"""

********
BONEYARD
********

def digit_degree(n, cnt) :
# {
    tmp = str(n)
    
    if (len(tmp) == 1) :
    # {
        return 0 + cnt
    # }

    else :
    # {
        return 1 + digit_degree(sum_individual_digit(n), 0)
    # }

# }

def sum_individual_digit(n) :
# {
    tmp = str(n)
    sum = 0

    for i in range(len(tmp)) :
    # {
        sum = sum + int(tmp)
    # }

    return sum
# }

def solution(n) :
# {
    return digit_degree(n, 0)
# }

"""