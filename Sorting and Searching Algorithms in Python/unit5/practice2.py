'''

You did an excellent job sorting with Quick Sort! What would happen if we changed the sorting order? The code provided generates an ascending sequence of numbers from 1 to 30. Could you modify it to sort in descending order, resulting in a sequence from 30 down to 1? Keep in mind that even a minor adjustment can lead to a significant impact!

'''

import random

def partition(lst, low, high) :
# {

    '''
    Helper function to partition the list on the basis of pivot
    '''
    pivot = lst[high]
    idx = low - 1
    tmp = -1

    for i in range(low, high) :
    # {
        # if (lst[i] <= pivot) :
        if (lst[i] >= pivot) :
        # {
            idx = idx + 1
            # lst[idx], lst[i] = lst[i], lst[idx]
            
            tmp = lst[idx]
            lst[idx] = lst[i]
            lst[i] = tmp
        # }

        else :
        # {
            None
        # }

    # }

    # lst[idx + 1], lst[high] = lst[high], lst[idx + 1]
    
    tmp = lst[idx + 1]
    lst[idx + 1] = lst[high]
    lst[high] = tmp

    # lst[idx + 1] = lst[high]
    # lst[high] = lst[idx + 1]

    return idx + 1

# }

def quick_sort(lst, low, high) :
# {
    '''
    Applying Quick Sort
    '''
    if (len(lst) == 1) :
    # {
        return lst
    # }

    else :
    # {
        None
    # }
    
    if low < high :
    # if high < low :
    # {
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)
        # quick_sort(lst, high, pi + 1)
        # quick_sort(lst, pi - 1, low)

    # }

    else :
    # {
        None
    # }

# }

# Generate a list of numbers from 1 to 30
# numbers = [i for i in range(1, 31)]
numbers = []

for i in range(1, 31) :
# {
    numbers.append(i)
# }

# Print the original list
print("Original List:", numbers)

# Use Quick Sort on the list
quick_sort(numbers, 0, len(numbers) - 1)

# Print the sorted list
print("Sorted List:", numbers)

'''

********
BONEYARD
********

idx = lst[high]
    pivot = low - 1

# # if pivot <= lst[i] :
numbers = numbers [ : : -1]

            lst[i] = lst[idx]
            lst[idx] = lst[i]

'''