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
{
    
}

inputString = "aabb" # For inputString = "aabb", the output should be solution(inputString) = true.
solution(inputString)

"""

********
BONEYARD
********

andrew_pudge -- return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1

"""