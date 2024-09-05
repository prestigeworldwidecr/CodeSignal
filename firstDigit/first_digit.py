"""

Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
solution(inputString) = '1';
For inputString = "q2q-q", the output should be
solution(inputString) = '2';
For inputString = "0ss", the output should be
solution(inputString) = '0'.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A string containing at least one digit.

Guaranteed constraints:
3 ≤ inputString.length ≤ 10.

[output] char

"""

def solution(inputString) :
# {
    for i in range(len(inputString)) :
    # {
        if (inputString[i].isdigit()) :
        # {
            return inputString[i]
        # }

        else :
        # {
            None
        # }

    # }
    
# }

# For inputString = "var_1__Int", the output should be solution(inputString) = '1';
# For inputString = "q2q-q", the output should be solution(inputString) = '2';
# For inputString = "0ss", the output should be solution(inputString) = '0'.
inputString = "var_1__Int"
inputString = "q2q-q"
inputString = "0ss"
print(solution(inputString))

"""


********
BONEYARD
********

return filter(str.isdigit, inputString)

    

"""