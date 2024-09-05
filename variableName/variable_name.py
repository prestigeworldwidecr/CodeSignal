"""

Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;

For name = "qq-q", the output should be
solution(name) = false;

For name = "2w2", the output should be
solution(name) = false.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string name

Guaranteed constraints:
1 ≤ name.length ≤ 10.

[output] boolean

true if name is a correct variable name, false otherwise.

"""

def all_valid_characters(name) :
# {
    result = None

    for i in range(len(name)) :
    # {
        if (name[i].isletter() or name[i].isdigit()) :
        # {
            result = True
        # }

        else :
        # {
            return False
        # }

    # }

    return result
# }

def solution(name) :
# {
    result = None
    
    if (name[0].isletter()) :
    # {
        result = all_valid_characters(name)
    # }

    else :
    # { 
        return False
    # }
    
    return result

# }

# For name = "var_1__Int", the output should be solution(name) = true;
# For name = "qq-q", the output should be solution(name) = false;
# For name = "2w2", the output should be solution(name) = false.

name = "var_1__Int"
name = "qq-q"
name = "2w2"

print(solution(name))

"""

********
BONEYARD
********

"""