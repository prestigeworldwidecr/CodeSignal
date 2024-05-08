"""

Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.

"""

def solution(inputString) :
    str1 = []
    rev = []

    for i in inputString :
       str1.append(i)

    rev = reversed(str1)
    return str1 == list(rev)

# solution("racecar")
# solution("taco")

"""

########
BONEYARD
########

# print(list(l))
# print(reversed(list(["racecar"])))

l = ["racecar", "taco"]
l = reversed(l)

l1 = [inputString]
    l2 = [inputString]

# print (inputString[1])
    # print (j)

# print(inputString[i])
       # i = 0
    # j = len(inputString) - 1
    
# print(str1 == list(rev))

"""
