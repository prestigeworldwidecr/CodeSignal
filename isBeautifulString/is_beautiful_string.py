"""

A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be solution(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be solution(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be solution(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ inputString.length ≤ 50.

[output] boolean

Return true if the string is beautiful, false otherwise.

"""

from collections import Counter

def beautiful_count(inputString) :
# {
    tmp = dict(Counter(list(sorted(inputString))))
    tmp = list(tmp.values())
    result = False

    for i in range(len(tmp) - 1) :
    # {
        if (tmp[i] < tmp[i + 1]) :
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

def beautiful_order(inputString) :
# {
    tmp = sorted(set(inputString))
    diff = ord(tmp[len(tmp) - 1]) - ord(tmp[0])
    result = False
    
    if (diff == len(tmp) - 1 and tmp[0] == 'a') :
    # {
        result = True
    # }

    else :
    # {
        return False
    # }

    return result

# }

def solution(inputString) :
# {  
    return beautiful_order(inputString) and beautiful_count(inputString)
# }

# For inputString = "bbbaacdafe", the output should be solution(inputString) = true.
# For inputString = "aabbb", the output should be solution(inputString) = false.
# For inputString = "bbc", the output should be solution(inputString) = false.
inputString = "bbbaacdafe"
# inputString = "aabbb"
# inputString = "bbc"

print(solution(inputString))

"""

********
BONEYARD
********

# print(tmp[i])
# tmp = list(sorted(inputString))

def play_with_my_dict(inputString) :
# {
    # print(inputString)
    # tmp = {}
    # tmp[inputString[0]] = 1
    # print(tmp)
    tmp = list(sorted(inputString))
    tmp = dict(Counter(tmp))
    
    for values in tmp.values() :
    # {
        print(values)
    # }

# }

# return beautiful_order(inputString)
# play_with_my_dict(inputString)
# print("!", tmp[0].values())
# print(values, values[0])
# tmp = list(inputString)
>>> l = ["a","b","b"]
>>> from collections import Counter
>>> Counter(l)
Counter({'b': 2, 'a': 1})

from collections import Counter
>>> z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
>>> Counter(z)
Counter({'blue': 3, 'red': 2, 'yellow': 1})

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

# print(sorted(inputString))
for i in range(len(inputString)) :
# {
    None
# }

print(list(inputString))


"""