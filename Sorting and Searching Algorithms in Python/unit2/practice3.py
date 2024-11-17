'''

Well done, space explorer! You've made great progress. Now, let's elevate the challenge.

In the provided starter code, there's a use-case scenario for a national spelling bee competition. The primary task is determining the position that a word of a specific length would hold in our sorted list of word lengths. To make this process efficient, we use Binary Search.

However, the code for a critical aspect of our binary search — a recursive method — is missing. Could you write the code for this missing piece?

Are you ready to dive deeper into the world of Binary Search? Let's go!

'''

# Implementation of Binary Search on a specific use case

# List of sorted word lengths in a dictionary
# Lengths from 1 to 500
# word_lengths = [i for i in range(1, 501)]
word_lengths = []

for i in range(1, 501) :
# {
    word_lengths.append(i)
# }

# TODO: Implement the recursion-based binary_search_recursive method
def binary_search_recursive(data, target, low, high) :
# {
    if (high - low <= 1) :
    # {
        # return low if data[low] == target else None
        if (data[low] == target) :
        # {
            return low
        # }

        else :
        # {
            return None
        # }

    # }
    
    else :
    # {
        None
    # }

    mid = (low + high) // 2

    if target < data[mid] :
    # {
        return binary_search_recursive(data, target, low, mid)
    # }

    else :
    # {
        return binary_search_recursive(data, target, mid, high)
    # }

# }

# Suppose there is a spelling bee, and a contestant is given a word.
# The contestant knows the word is in the dictionary, so let's find what position the length of this word would hold in our sorted list of word lengths
word_length_query = 237
result = binary_search_recursive(word_lengths, word_length_query, 0, len(word_lengths))

if (result is not None) :
# {
    print("Words of length", word_length_query, "are found at position", result, "in the word lengths list.")
# }

else :
# {
    print("No words are found with length", word_length_query, ".")
# }

'''

********
BONEYARD
********

'''