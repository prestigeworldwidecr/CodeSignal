"""

Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 109.

[output] boolean

true if all digits of n are even, false otherwise.

"""

def even_digits_only(n) :
# {
    tmp = str(n)
    result = False

    for i in range(len(tmp)) :
    # {
        # print("!", tmp[i])
        
        if (int(tmp[i]) % 2 != 0) :
        # {
            return False
        # }

        else :
        # {
            result = True
        # }

    # }

    return result
# }

def solution(n) :
# {
    return (even_digits_only(n))
# }

# For n = 248622, the output should be solution(n) = true;
# For n = 642386, the output should be solution(n) = false.

n = 248622
n = 642386

print(solution(n))

"""

********
BONEYARD
********

# print("!", n)
# print(result)
# print("@", n, tmp)

"""