'''

Congratulations on your progress thus far, compadre! Now, let's delve deeper into the realms of Merge Sort. Consider that you are a space linguist who has intercepted alien messages; however, the words in these messages are all jumbled up. To decipher these messages, you must sort them in some order. Fortunately, the Merge Sort algorithm is, in theory, an ideal candidate for this job.

The current code attempts to create a list of random lower-case alphabets and then sort them using Merge Sort. However, it seems the sort isn't working as intended. Could you analyze the provided code and fix the issue? Good luck, young padawan!

'''

import string
import random

def merge_sort(arr) :
# {
    if (len(arr) <= 1) :
    # {
        return arr
    # }

    else :
    # {
        None
    # }

    mid = len(arr) // 2
    left = arr[ : mid: ]
    right = arr[mid : : ]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# }

def merge(left, right) :
# {
    res = []
    left_index = 0
    right_index = 0

    # print("Left: ", left, "Right: ", right)

    while (left_index < len(left) and right_index < len(right)) :
    # {
        if (left[left_index] < right[right_index]) :
        # {
            res.append(left[left_index])
            # left_index += 1
            left_index = left_index + 1
        # }

        else :
        # {
            res.append(right[right_index])
            # right_index += 1
            right_index = right_index + 1
        # }

    # }

    # If we reach the end of either array, append the leftover elements from the other array
    if (left) :
    # {
        res.extend(left[left_index: : ])
    # }

    else :
    # {
        None
    # }

    if (right) :
    # {
        res.extend(right[right_index: : ])
    # }

    else :
    # {
        None
    # }

    return res

# }

# Generate a list of 20 random lowercase alphabets
# random_alphabets = [random.choice(string.ascii_lowercase) for _ in range(20)]

random_alphabets = []

for i in range(20) :
# {
    random_alphabets.append(random.choice(string.ascii_lowercase))
# }

print("Original List: \n", random_alphabets)

# Apply merge sort
sorted_alphabets = merge_sort(random_alphabets)

print("\nSorted List: \n", sorted_alphabets)

'''

********
BONEYARD
********


    # left_index = (0, 0)
    # right_index = (0, 0)

'''