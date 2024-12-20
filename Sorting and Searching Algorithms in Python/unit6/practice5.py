'''

Excellent work, Space Voyager! You're on the brink of mastering the art of Merge Sort. Let's make the ultimate transition into hyperspeed.

With your newly acquired skills, your task is to generate input data to sort and sort this data using Merge Sort. This function is important, as sorting alphanumeric characters is a common necessity in real-world scenarios.

Follow the insightful guidance provided by the TODO comments present in the starter code. May your coding journey unfold smoothly!

'''

import random
import string

# TODO: Define a merge_sort function that takes data to sort and returns the sorted data
def merge_sort(lst) :
# {
    # TODO: If the alphanumeric array has one or no elements, it is already sorted. So, return the array immediately.
    if (len(lst) <= 1) :
    # {
        return lst
    # }

    else :
    # {
        None
    # }

    # TODO: Next, divide the array into two equal parts.
    mid = len(lst) // 2
    left_half = lst[ : mid: ]
    right_half = lst[mid : : ]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # TODO: Sort the left and right parts of the array with the merge_sort function.
    left_half = lst[ : mid: ]
    right_half = lst[mid : : ]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # TODO: After sorting both halves of the array, combine them together using the merge function.
    return merge(left_half, right_half)

# }

# TODO: In the merge function, take two sorted arrays as inputs
def merge(left, right) :
# {
    result = []
    i = 0
    j = 0

    # print("Left: ", left, "Right: ", right)

    # TODO: While both arrays have elements in them, compare the first element of each.
    # If the first element of the left array is smaller, add it to the result array and remove it from the left array.

    # Otherwise, do the same with the right array.
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

    # TODO: If the left or right array still has elements, add them to the result array.
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

# TODO: Generate some random data to sort
random_alphanumeric = []

for i in range(20) :
# {
    random_alphanumeric.append(random.choice(string.ascii_letters + string.digits))
# }

# TODO: Print the original data
print("Original List of random alphanumeric characters:\n", random_alphanumeric)

# TODO: Use your merge_sort function to sort the data
sorted_alphanumeric = merge_sort(random_alphanumeric)

# TODO: Print the sorted data
print("\nSorted List of alphanumeric characters:\n", sorted_alphanumeric)

'''

**********  BONEYARD  **********

'''