"""

Write a def that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab"

For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz"

For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb"

For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".

Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.

Guaranteed constraints:
0 ≤ inputString.length ≤ 50.

[output] string

Return inputString, with all the characters that were in parentheses reversed.

"""

def inner_most_substring(inputString) :
# {
    i = 0
    left = -1 # leftParenLocation
    right = -1 # firstRightParenLocation
    tmp = ""
    
    while (i < len(inputString)) :
    # {
        if (inputString[i] == '(' and right == -1) :
        # {
            left = i
        # }

        elif (inputString[i] == ')' and right == -1) :
        # {
            right = i
        # }
        
        else :
        # {
            None
        # }
        
        i = i + 1

    # }

    if (right == -1) :
    # {
        return inputString
    # }

    else :
    # {
        tmp = inputString[0, left] + reverse_string_atom[left + 1, right] + inputString[right + 1, len(inputString)]

        # print(b[2:5])
        # tmp = inputString.substring(0, left) + reverse_string_atom(inputString.substring(left + 1, right)) + inputString.substring(right + 1, inputString.length)

        return inner_most_substring(tmp)
    # }

# }

def reverse_string_atom(inputString) :
# {
    # return inputString.split("").reverse().join("")
    return inputString[::-1]
# }

def solution(inputString) :
# {
    return inner_most_substring(inputString)
# }

inputString = "foo(bar)baz(blim)"
# inputString = "easy"
# print (inputString[::-1])
solution(inputString)

"""

********
BONEYARD
********


"""