"""

You have k apple boxes full of apples. Each square box of size m contains m × m apples. You just noticed two interesting properties about the boxes:

The smallest box is size 1, the next one is size 2,..., all the way up to size k.
Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
Your task is to calculate the difference between the number of red apples and the number of yellow apples.

Example

For k = 5, the output should be
solution(k) = -15.

There are 1 + 3 * 3 + 5 * 5 = 35 yellow apples and 2 * 2 + 4 * 4 = 20 red apples, making the answer 20 - 35 = -15.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer k

A positive integer.

Guaranteed constraints:
1 ≤ k ≤ 40.

[output] integer

The difference between the two types of apples.

"""

def yellowApples(o) :   #odd
# {
    i = 1
    y = 0
    
    # for (i = 1 i <= o i = i + 2)
    # for i in range(i, o, 2) :
    while (i <= o) :
    # {
        y = y + i * i
        i = i + 2
    # }

    return y

# }

def redApples(e) :  # even
# {
    i = 2
    r = 0
    
    # for (i = 2 i <= e i = i + 2)
    while (i <= e) :
    # {
        r = r + i * i
        i = i + 2
    # }

    return r
# }

def appleDifference(y, r) :
# {
    return r - y
# }

def solution(k) :
# # {
    return appleDifference(yellowApples(k), redApples(k))
# # }

# For k = 5, the output should be solution(k) = -15.
k = 5

print(solution(k))

"""

********
BONEYARD
********

"""