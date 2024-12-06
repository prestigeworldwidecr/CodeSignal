'''

Well done, Space Voyager! You've made superb progress with Quick Sort. Now, gear up for the final challenge, in which you will create your Quick Sort universe from scratch!

Your mission is to devise a Quick Sort function that can sort a list of 20 random numbers in descending order. Use all the knowledge about Quick Sort that you've accumulated to accomplish this task.

Look at the starter code and follow the instructions in the TODO comments. It's time to set your coding thrusters to the max!

'''

import random

# TODO: Define the 'quick_sort_desc' and 'partition_desc' functions to implement Quick Sort in descending order
def partition_desc(l, low, high) :
# {
    pivot = l[low]
    i = low + 1
    j = high
    done = False

    while not done :
    # {
        # while (i <= j and arr[i] >= pivot) :
        while (i <= j and l[i] >= pivot) :
        # {
            # i += 1
            i = i + 1
        # }

        # while (arr[j] <= pivot and j >= i) :
        while (l[j] <= pivot and j >= i) :
        # {
            # j -= 1
            j = j - 1
        # }

        if (j < i) :
        # {
            done = True
        # }

        else :
        # {
            # arr[i], arr[j] = arr[j], arr[i]
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp
        # }

    # }

    # arr[low], arr[j] = arr[j], arr[low]
    tmp = l[low]
    l[low] = l[j]
    l[j] = tmp

    return j
# }

def quick_sort_desc(l, low, high) :
# {
    if (low < high) :
    # {
        split_point = partition_desc(l, low, high)
        quick_sort_desc(l, low, split_point - 1)
        quick_sort_desc(l, split_point + 1, high)
    # }
    
    else :
    # {
        None
    # }

    return l

# }

# Generate a list of 20 random numbers between 50 and 100
# random_numbers = [random.randint(50, 100) for _ in range(20)]
random_numbers = []

for i in range(20) :
# {
    random_numbers.append(random.randint(50, 100))
# }

print("Unsorted List: ", random_numbers)

# TODO: Use the Quick Sort function to sort the list in descending order and print the sorted list
print("Sorted List: ", quick_sort_desc(random_numbers, 0, len(random_numbers) - 1))

'''

********
BONEYARD
********

tmp = len(random_numbers) - 1
print(type(random_numbers[0]), type(tmp))

'''