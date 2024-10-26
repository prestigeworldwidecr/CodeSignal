'''

Hey there, Space Voyager! Your mission, should you choose to accept it, involves anagrams - those fun jumbled-up words. You'll be given two arrays of words. Your task? Find the unique words in the first array that can rearrange their letters to match at least one word in the second array. Like transforming 'cinema' into 'iceman'. Cool, right?

The input will be two lists of words; they can be of any size, and words may repeat. As for the output, we need a list of unique words from the first list that have anagrams in the second one. Make sure the spaceship does not crash into an asteroid, and check that there aren't any duplicate words in the output. As for edge cases, watch out for case sensitivity and one-letter words!

It's time to go where no programmer has gone before boldly. Happy coding!

'''

def alphabetize(list) :
# {
    for i in range(len(list)) :
    # {
        list[i] = ''.join(sorted(list[i]))
    # }

    return list

# }

def find_anagram_words(list_1, list_2) :
# {
    # implement this
    
    result = set()

    list_1 = list(dict.fromkeys(list_1))
    list_2 = list(dict.fromkeys(list_2))
    list_2 = alphabetize(list_2)

    # print(list_1, list_2)

    for i in list_1 :
    # {

        # print(i, sorted(i), list_2)
        tmp = ''.join(sorted(i))

        if (tmp in list_2) :
        # {
            result.add(i)
            # print(tmp, result)
        # }

        else :
        # {
            None
        # }

    # }

    result = list(result)

    return result
# }

print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
# print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
# print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []

'''

********
BONEYARD
********

# print(i)

    # s1 = set(alphabetize(list_1))
    # s2 = set(alphabetize(list_2))

    # print(s1, s2)
    # print(alphabetize(list_1), alphabetize(list_2))
    # print(list_1, list_2)

# print(alphabetize(list_1), alphabetize(list_2))
# print(s1, s2)

'''