"""

Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string st

A string consisting of lowercase English letters.

Guaranteed constraints:
3 ≤ st.length ≤ 10.

[output] string

"""

def solution(st) :
# {
    result = list(st)
    i = 0

    while (result != result[::-1]) :  # while result isnt a palindrome
    # {
        result.insert(len(st), st[i]) # add the ith letter to the end of result
        i = i + 1
    # }

    return "".join(result)

# }

# For st = "abcdc", the output should be solution(st) = "abcdcba".
st = "abcdc"
print(solution(st))

"""

********
BONEYARD
********

author: tamarack
def solution(st):
    string_list = list(st)
    i = 0
    while string_list != string_list[::-1]:
        string_list.insert(len(st),st[i])
        i += 1
    return "".join(string_list)

tmp = dict(Counter(list(sorted(inputString))))
tmp = list(tmp.values())
result = False

from collections import Counter

def beautiful_palindrome(st) :
# {
    tmp = dict(Counter(list(st)))
    return tmp
# }

"""
