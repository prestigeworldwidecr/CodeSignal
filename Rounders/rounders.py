"""

We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach. This means that at each step we take the last non 0 digit of the number and round it to 0 or to 10. If it's less than 5 we round it to 0 if it's larger than or equal to 5 we round it to 10 (rounding to 10 means increasing the next significant digit by 1). The process stops immediately once there is only one non-zero digit left.

Example

For n = 15, the output should be
solution(n) = 20;

For n = 1234, the output should be
solution(n) = 1000.

1234 -> 1230 -> 1200 -> 1000.

For n = 1445, the output should be
solution(n) = 2000.

1445 -> 1450 -> 1500 -> 2000.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ value ≤ 10^8.

[output] integer

The rounded number.

"""

def solution(n) :
# {
    tmp = list(str(n))
    result = ""

    for i in range(len(tmp) - 1, 0, -1) :
    # {
        if (int(tmp[i]) >= 5 and i > 0) :
        # {
            tmp[i - 1] = int(tmp[i - 1]) + 1
            tmp[i] = 0
        # }

        else :
        # {
            if (i > 0) :
            # { 
                tmp[i] = 0
            # }

            else :
            # {
                None
            # }

        # }

    # }
    
    for i in range(len(tmp)) :
    # {
        result = result + str(int(tmp[i]))
    # }

    # print(str(tmp))
    return int(result)

# }

n = 15     # the output should be solution(n) = 20;
n = 1234   # the output should be solution(n) = 1000.
n = 1445   # the output should be solution(n) = 2000.
# n = 7001

print(solution(n))

"""

********
BONEYARD
********

"""