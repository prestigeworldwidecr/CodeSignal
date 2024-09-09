"""

Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
solution(s) = "2a3bc".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string s

String consisting of lowercase English letters.

Guaranteed constraints:
4 ≤ s.length ≤ 15.

[output] string

Encoded version of s.

"""

def solution(s) :
# {
    s = s + str(0)
    cnt = ''
    cur = ''
    result = ''

    for i in s :
    # {
        if (i != cur) :
        # {
            if (cnt == 1) :
            # {
                result = result + str(cur)
            # }

            else :
            # {
                result = result + str(cnt) + str(cur)
            # }

            cur = i
            cnt = 1

        # }

        else :
        # {
            cnt = cnt + 1
        # }

    # }

    return result

# }

# For s = "aabbbc", the output should be solution(s) = "2a3bc".
s = "aabbbc"

print(solution(s))

"""

********
BONEYARD
********

author: solasky
def solution(s):
    s+='0'
    a=''
    count=''
    constant=''
    for x in s:
        if x!=constant:
            if count==1:
                a+=str(constant)
            else:
                a+=str(count)+str(constant)
            constant=x
            count=1
        else:
            count+=1
    return a

    
    cur = s[0]
    next = s[1]
    cnt = 0
    result = []

    for i in range(len(s)) :
    # {
        # print(i)
        cur = s[i]
        cnt = cnt + 1

        print(i, s[i], i + 1, len(s))

        if (i + 1 <= len(s)) :
        # {
            next = s[i + 1]
        # }

        else :
        # {
            None
        # }

        if (next != cur) :
        # {
            if (cnt == 1) :
            # {
                None
            # }

            else :
            # {
                result.append(cnt)
            # }

            cnt = 0
            result.append(cur)

        # }

        else :
        # {
            None
        # }

    # }

    return result


# print(cur)
from collections import Counter
# print(counts[i], letters[i])
# print(counts, letters)

tmp = dict(Counter(list(s)))
    counts = list(tmp.values())
    letters = list(tmp)
    result = ""

    for i in range(len(tmp)) :
    # {
        if (counts[i] == 1) :
        # {
            result = result + letters[i]
        # }
        
        else :
        # {
            result = result + str(counts[i]) + letters[i]
        # }

    # }

    return result

"""