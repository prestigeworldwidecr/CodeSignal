"""

Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.

"""

def solution(inputString) :
# {
    cnt = 0

    for i in set(inputString) :
    # {
        cnt = cnt + inputString.count(i) % 2
    # }

    return cnt < 2  # can't have more than one solo letter

# }

inputString = "aabb" # For inputString = "aabb", the output should be solution(inputString) = true.
inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"  # false
print(solution(inputString))

"""

********
BONEYARD
********

# print(i, inputString.count(i) % 2, cnt)
# print(i, inputString.count(i) % 2)
        # print(i)
        # print(set(inputString))

andrew_pudge -- return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1

"""