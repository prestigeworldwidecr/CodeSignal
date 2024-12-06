'''

Woohoo! You're doing incredibly well with Quick Sort! Now, let's embark on a little debugging mission!

Imagine this scenario: You're tasked with sorting a list of 15 numbers in ascending order. You chose Quick Sort for the job, but something seems wrong. The output isn't as expected. Hmm...

It appears there's a bug in the code. Can you identify and rectify it? Here's your chance to shine as the bug squasher!

'''

import random 

def partition(arr, low, high) :

    pivot = arr[low]
    i = low + 1
    j = high
    done = False

    while not done :
    # {
        # while (i <= j and arr[i] >= pivot) :
        while (i <= j and arr[i] <= pivot) :
        # {
            # i += 1
            i = i + 1
        # }

        # while (arr[j] <= pivot and j >= i) :
        while (arr[j] >= pivot and j >= i) :
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
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        # }

    # }

    # arr[low], arr[j] = arr[j], arr[low]
    tmp = arr[low]
    arr[low] = arr[j]
    arr[j] = tmp

    return j

def quick_sort(arr, low, high) :
# {
    if (low < high) :
    # {
        split_point = partition(arr, low, high)
        quick_sort(arr, low, split_point - 1)
        quick_sort(arr, split_point + 1, high)
    # }
    
    else :
    # {
        None
    # }

# }

# Generate a list of random numbers between 10 and 50
# random_list = [random.randint(10, 50) for i in range(15)]
random_list = []

for i in range(15) :
# {
    random_list.append(random.randint(10, 50))
# }

print("Original List: ", random_list)

quick_sort(random_list, 0, len(random_list) - 1)

print("List After Quick Sort: ", random_list)

'''

********
BONEYARD
********

'''