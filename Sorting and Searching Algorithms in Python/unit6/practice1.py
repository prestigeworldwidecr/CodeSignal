'''

Congratulations on making it this far! Are you ready for some fun with sorting?

Suppose you work in a location where you receive codes that are all jumbled up. You're required to sort them before processing. Isn't this a perfect situation to employ our Merge Sort? What if we generate some random strings and attempt to sort them?

'''

# Import necessary modules
import random

def merge_sort(lst) :
# {
    # If it's a single element or an empty list, it's already sorted
    if (len(lst) <= 1) :
    # {
        return lst
    # }

    else :
    # {
        None
    # }

    # Find the middle point
    mid = len(lst) // 2

    # Recursively sort both halves
    left_half = merge_sort(lst[0 : mid: ])
    right_half = merge_sort(lst[mid: len(lst): ])

    # Merge the two sorted halves
    return merge(left_half, right_half)

# }

def merge(left, right) :
# {
    result = []
    i = 0
    j = 0

    # Compare the smallest unused elements in both lists and append the smallest to the result
    while (i < len(left) and j < len(right)) :
    # {
        if (left[i] < right[j]) :
        # {
            result.append(left[i])
            # i += 1
            i = i + 1
        # }

        else :
        # {
            result.append(right[j])
            # j += 1
            j = j + 1
        # }

    # }

    # Once we've exhausted one list, append all remaining elements from the other list to the result
    result.extend(left[i: : ])
    result.extend(right[j: : ])
    
    return result

# }

# Generate a list of 20 random strings of length 5
# random_strings = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)) for i in range(20)]
random_strings = []

for i in range(20):
# {
    random_strings.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k = 5)))
# }
    

print("Original List of random strings: \n", random_strings)

# Apply merge sort
sorted_strings = merge_sort(random_strings)

print("\nSorted List of strings: \n", sorted_strings)

'''

********
BONEYARD
********

'''