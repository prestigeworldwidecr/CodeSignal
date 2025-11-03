'''

You are working on a NASA project and have been provided with two lists of celestial bodies. List1 and List2 each contain n names of celestial bodies, where n varies from 1 to 1000000, inclusive.

You need to generate a list to indicate whether a celestial body from List1 is found in List2 and eventually return this list. The condition is to optimize your solution using Python's built-in set data structure, rather than simple list iteration.

For the sake of simplicity and to keep our data manageable, let's assume the names of celestial bodies are represented as lowercase English alphabets and can vary from 1 to 10 characters in length, inclusive.

The order of entries in your result should directly correspond to the order of celestial bodies in List1. For example, the first boolean in your list should denote whether the first celestial body of List1 is present in List2 or not.

For instance, let's consider two lists:

list1 = ["mars", "jupiter", "venus", "earth"]
list2 = ["earth", "mars", "neptune"]

Your function, to be named check_presence(list1, list2), should return:

[True, False, False, True]

This indicates that "mars" and "earth" from List1 are found in List2.

Your task involves figuring out a method to accurately and efficiently perform this query, utilizing the properties of Python's set data structure to optimize the execution time of your code compared to the straightforward iteration over members of List1 for their presence in List2.

'''

def solution(list1, list2) :
# {
    # TODO: implement the solution and return the result list.
    result = [False] * len(list1)
    set2 = set(list2)

    for i in range(len(list1)) :
    # {
        if (list1[i] in set2) :
        # {
            result[i] = True
        # }

        else :
        # {
            None
        # }

    # }

    return result

# }

list1 = ["mars", "jupiter", "venus", "earth"]
list2 = ["earth", "mars", "neptune"]

# [True, False, False, True]

print(solution(list1, list2))

'''

***** BONEYARD *****

# print(result)

# tmp = "mars"

# print(list[0], list2, tmp in list2)


# tmp = list[i]

# print(i, tmp, list[i], tmp in list2)


'''