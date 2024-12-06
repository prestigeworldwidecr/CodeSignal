'''

Great job, Ace Coder! Yet, there's more in store! Let's enhance our Quick Sort programming adventure!

Imagine you have a list of 15 random numbers between 1 and 50, but they are all scrambled. Your challenge is to implement a function that sorts this list, utilizing the Quick Sort algorithm we've just explored.

Specifically, you are to complete missing pieces of code that will execute Quick Sort on your list and print the sorted array.

'''

import random 

# TODO: Implement the Quick Sort function
def quick_sort(arr) :
# {
    if (len(arr) <= 1) :
    # {
        return arr
    # }

    else :
    # {
        pivot = arr[len(arr) // 2]

        # TODO: fill in the missing code
        pivot = arr[random.randint(0, len(arr) - 1)]

        # left = [x for x in arr if x < pivot] # elements less than `pivot`
        left = []
        # middle = [x for x in arr if x == pivot] # elements equal to `pivot`
        middle = []
        # right = [x for x in arr if x > pivot] # elements larger than `pivot`
        right = []

        for i in arr :
        # {
            if (i < pivot) :
            # {
                left.append(i)
            # }

            elif (i == pivot) :
            # {
                middle.append(i)
            # }
            
            elif (i > pivot) :
            # {
                right.append(i)
            # }

            else :
            # {
                None 
            # }

        # }

    # }    
    
    return quick_sort(left) + middle + quick_sort(right)

# }

# random_numbers = [random.randint(1, 50) for _ in range(15)]
random_numbers = []

for i in range (15) :
# {
    random_numbers.append(random.randint(1, 50))
# }

print("Unsorted List: ", random_numbers)

# TODO: Use the Quick Sort function to sort the list and print the sorted list
print("Sorted List: ", quick_sort(random_numbers))

'''

********
BONEYARD
********

middle = [] # len(arr) // 2
    middle.append(pivot)
    i = len(arr) // 2 - 1
    j = len(arr) // 2 + 1
    left = arr[0: i: ]
    right = arr[j: len(arr): ]

'''