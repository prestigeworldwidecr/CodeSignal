"""

Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

Guaranteed constraints:
3 ≤ inputString.length ≤ 100.

[output] string

"""

def got_digits(inputString) :
# {
    result = ""

    for i in range(len(inputString)) :
    # {
        if (inputString[i].isdigit() or inputString[i] == 0) :
        # {
            result = result + inputString[i]
        # }

        else :
        # {
            return result
        # }
    # }

    return result

# }

def solution(inputString) :
# {
    return got_digits(inputString)
# }

inputString = "123aa1"  # solution(inputString) = "123"
# inputString = "0123456789"  # "0123456789"
print(solution(inputString))

"""

********
BONEYARD
********

"""