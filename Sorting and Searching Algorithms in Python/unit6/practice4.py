'''

Congratulations, Adventurer, on efficiently sorting the alphabet! Now, let's delve deeper and sort more complex data.

Suppose we have intercepted alien messages again, but this time, the strings contain both lowercase letters and numbers. The goal remains the same - we need to sort the strings in a specific order using Merge Sort to decode these messages.

Unfortunately, some parts of the sorting code are missing! Can you complete the code to sort these alphanumeric strings successfully?

Prepare yourself, and let's begin the decoding process!

'''

# Import necessary modules
import random
import string

def merge_sort(lst) :
# {
    if (len(lst) <= 1) :
    # {
        return lst
    # }

    else :
    # {
        None
    # }

    mid = len(lst) // 2
    left_half = lst[ : mid: ]
    right_half = lst[mid : : ]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # TODO: Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right) :
# {
    result = []
    i = 0
    j = 0

    # print("Left: ", left, "Right: ", right)

    # TODO: implement the merging mechanism here
    while (i < len(left) and j < len(right)) :
    # {
        if (left[i] < right[j]) :
        # {
            result.append(left[i])
            i = i + 1
        # }

        else :
        # {
            result.append(right[j])
            j = j + 1
        # }

    # }

    # If we reach the end of either array, append the leftover elements from the other array
    if (left) :
    # {
        result.extend(left[i: : ])
    # }

    else :
    # {
        None
    # }

    if (right) :
    # {
        result.extend(right[j: : ])
    # }

    else :
    # {
        None
    # }

    return result

# }

# Generate a list of 20 random alphanumeric characters.
# random_alphanumeric = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
random_alphanumeric = []

for i in range(20) :
# {
    random_alphanumeric.append(random.choice(string.ascii_letters + string.digits))
# }

print("Original List of random alphanumeric characters:\n", random_alphanumeric)

# Apply merge sort
sorted_alphanumeric = merge_sort(random_alphanumeric)

print("\nSorted List of alphanumeric characters:\n", sorted_alphanumeric)

'''

########
BONEYARD
########



    # print(type(left_half))
    # print(type(right_half))

'''