"""

Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.

Example

For a = 2 and b = 6, the output should be
solution(a, b) = false;
For a = 2 and b = 3, the output should be
solution(a, b) = true.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer a

Guaranteed constraints:
0 ≤ a ≤ 20.

[input] integer b

Guaranteed constraints:
0 ≤ b ≤ 20.

[output] boolean

true if the pseudocode will never stop, false otherwise.

"""

def is_infinite_process(a, b):
# {
    flag = a > b
    cur = ""
    result = False
    cnt = 0

    while(True) :
    # {

        if (a == b) :
        # {
            return False
        # }
            
        elif (flag != cur) :
        # {
            return True
        # }

        else :
        # {
            result = False
            a = a + 1
            b = b - 1
            cur = a > b
        # }

        if (a != b) :
        # {
            None
        # }

        else :
        # {
            return result
        # }

    # }

    return result

# }

def solution(a, b) :
# {
    return is_infinite_process(a, b)
# }

a = 2
b = 6

print(solution(a, b))

"""

********
BONEYARD
********

"""