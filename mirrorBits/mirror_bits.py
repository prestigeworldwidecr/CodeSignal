"""

Reverse the order of the bits in a given integer.

Example

For a = 97, the output should be
solution(a) = 67.

97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.

For a = 8, the output should be
solution(a) = 1.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer a

Guaranteed constraints:
5 ≤ a ≤ 105.

[output] integer

"""

def solution(a) :
# {
    result = "{0:b}".format(a)
    result = result[::-1]
    result = int(result, 2)
    
    return result
# }

a = 8

print(solution(a))

"""

********
BONEYARD
********

"""