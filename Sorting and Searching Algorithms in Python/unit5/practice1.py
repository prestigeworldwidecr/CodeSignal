'''

Hey, Galactic Pioneer! Are you ready to dive into our first Quick Sort practice?

Let's imagine that you have a list of 20 random numbers ranging between 1 and 100. These numbers need to be sorted efficiently, and that task is perfectly suited for Quick Sort, which is fast and reliable.

Note that we used a slightly different approach for partitioning here - take some time to go through and learn it! If something is not clear, feel free to ask me to clarify it for you!

'''

# Import required libraries
import random

def partition(arr, low, high) :
# {
    # this method partitions arr[low..high] to move all elements <= arr[high] to the left
    # and returns the index of `pivot` in the updated array
    pivot = arr[high]
    i = low - 1

    for j in range(low, high) :
    # {
        if (arr[j] <= pivot) :
        # {
            i = i + 1
            # arr[i], arr[j] = arr[j], arr[i]
            arr[i] = arr[j]
            arr[j] = arr[i]
        # }

        else :
        # {
            None
        # }

    # }

    # arr[i + 1], arr[high] = arr[high], arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = arr[i + 1]

    return i + 1

# }

def quick_sort(arr, low, high) :
# {
    if (low < high) :
    # {
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    # }

    else :
    # {
        None
    # }

# }
        
# Generate a list of random numbers between 1 and 100
# random_list = random.sample(range(1, 101), 20)
random_list = []

for i in range(1, 101) :
# {
    random_list.append(i)
# }

print("Unsorted list:", random_list)

quick_sort(random_list, 0, len(random_list) - 1)
print("Sorted list with Quick Sort:", random_list)

'''

********
BONEYARD
********

'''