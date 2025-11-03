'''

You will be given a string s consisting of lowercase English letters, and a character list letters. Both the string s and the list letters have lengths ranging from 
1
1 to 
1000000
1000000. Your task is to return a list containing the characters that are common to both the character string s and the character list letters.

Each element of the character string and each element in the list letters are characters ranging from a to z.

Suppose you are given a string:

s = "hello"

and a list of characters:

letters = ['h', 'a', 'e', 'i', 'o', 'u']

Your function common_characters(s, letters) should sift through both the character array and the list, extracting the common characters between them.

The expected output in this case should be:

['e', 'h', 'o']

You should return the result in alphabetical order.

'''

def solution(s, letters) :
# {
    # TODO: implement
    s1 = list(s)
    s1 = set(s1)
    s2 = set(letters)

    return sorted(s1 & s2)
# }

s = "hello"
letters = ['h', 'a', 'e', 'i', 'o', 'u']
# ['e', 'h', 'o']

print(solution(s, letters))

'''

***** BONEYARD *****

'''