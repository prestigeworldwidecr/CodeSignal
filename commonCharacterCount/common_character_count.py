"""

Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer

"""

# sort
# count w/dict, compare

def create_character_count_dict(s) :
# {
    d = {}

    for i in range(len(s)) :
    # {
        if (s[i] in d) :
        # {
            d[s[i]] = d[s[i]] + 1
        # }

        else :
        # {
            d[s[i]] = 1
        # }

    # }

    return sorted(d)

# }

def determine_common_character_count(s1, s2) :
# {
    None
# }

def solution(s1, s2) :
# {

    if (len(s1) >= len(s2)) :
    # {
        determine_common_character_count(s1, s2)
    # }

    else :
    # {
        determine_common_character_count(s2, s1)
    # }
# }

s1 = "aabcc"
s2 = "adcaa"

solution (s1, s2)


"""

########
BONEYARD
########


# print(len(s1))
# print(create_character_count_dict(s2))

# print(s1, s2)
# print(max(len(s1), len(s2)))

# "nothing"
# d.update(s[i] = s[i], )
            
# "nothing"
# print(s[i])

# print(s1, s2, dic1)
# print(s1[0])

# for i in range()

# dic1 = {}
# dic1 = dict()

dic1 = dict({
                "name": "pizza",
                "size": 16,
                "location": "Chapultepec"
            })

sandwich_type = ("Reuben", "Club", "Triple Play")
food_type = ("sandwich")

dic1 = dict.fromkeys(sandwich_type, food_type)

"""