"""

You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you construct an array of all the integers from a to b inclusive. You need to count the number of 1s in the binary representations of all the numbers in the array.

Example

For a = 2 and b = 7, the output should be
solution(a, b) = 11.

Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111], which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer a

Guaranteed constraints:
0 ≤ a ≤ b.

[input] integer b

Guaranteed constraints:
a ≤ b ≤ 10.

[output] integer

"""

def build_inclusive_array(a, b) :
# {
    tmp = list()

    for i in range(a, b + 1) :
    # {
        tmp.append("{0:b}".format(i))
    # }

    # print (tmp)

    return tmp

# }

def range_bit_count(a) :
# {
    cnt = 0

    for i in range(len(a)) :
    # {
        tmp = a[i]

        for j in range(len(tmp)) :
        # {
            # print(tmp[j], cnt)
            
            if (tmp[j] == '1') :
            # {
                cnt = cnt + 1
            # }

            else :
            # {
                None
            # }

        # }

    # }

    return cnt

# }

def solution(a, b) :
# {
    return range_bit_count(build_inclusive_array(a, b))
# }

a = 2
b = 7

print(solution(a, b))

"""

********
BONEYARD
********

"""