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

def solution(s1, s2) :
# {

    t = 0

    for i in set(s1) :
    # {
        for j in set(s2) :
        # {
            if (i == j) :
            # {
                t = t + min(s1.count(i), s2.count(j))
            # }
            
            else :
            # {
                None
            # }

        # }

    # }

    return t

# }

s1 = "aabcc"
s2 = "adcaa"

print(solution(sorted(s1), sorted(s2)))

"""

def solution(s1, s2):
    count = 0
    commons = set(s1) & set(s2)
    for i in commons:
        count += min(s1.count(i), s2.count(i))
    return count
        


########
BONEYARD
########

# sort
# count w/dict, compare

# print(s2.count(j))
# print(s1.count(i))

# solution (s1, s2)
# print(set(s1.count(s1)))

create_character_count_dict(s1, s2)

def create_character_count_dict(s1, s2) :
# {
    d1 = {}
    d2 = {}
    total = 0

    for i in range(len(s1)) :
    # {
        if (s1[i] in d1) :
        # {
            d1[s1[i]] = d1[s1[i]] + 1
        # }

        else :
        # {
            d1[s1[i]] = 1
        # }

    # }

    for i in range(len(s2)) :
    # {
        if (s2[i] in d2) :
        # {
            d2[s2[i]] = d2[s2[i]] + 1
        # }

        else :
        # {
            d2[s2[i]] = 1
        # }

    # }

    if (len(s1) >= len(s2)) :
    # {
        for key, value in d1.items() :
        # {
            print (key, value)
        # }

        for i in range(len(d2)) :
        # {
            for j in range (len(d1)) :
            # {
                print(d1.keys()[1])

                if (s1[i] == s2[j]) :
                # {
                    #total = total + 1
                    # j = len(s1) # match, go to next letter in s2
                # }

                else :
                # {
                    None
                # }

            # }

        # }

    # }

    else :
    # {
        print(2)
    # }

    # print (d1.iteritems())

# }



return sorted(d1)

t = determine_common_character_count(create_character_count_dict(s2),
                                            create_character_count_dict (s1))

t = determine_common_character_count(create_character_count_dict(s1),
                                            create_character_count_dict (s2))

# https://stackoverflow.com/questions/21986194/how-to-pass-dictionary-items-as-function-arguments-in-python
def determine_common_character_count(d1, d2) :
# {
    total = 0

    print (d1)

    return total
# }

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