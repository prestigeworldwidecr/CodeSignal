'''

Cosmonaut, you've done an impressive job implementing the binary search! Now, let's consider a situation in which we're working with a sorting algorithm for a social media platform. This platform contains a feature to find the position of a user's age within a sorted list. However, we've noticed that the current algorithm fails and never finishes. Can you spot the issue and fix it, to make sure the algorithm returns that the age of 30 is not in the list?

'''

# Implementation of Binary Search on a specific use case

# List of sorted ages in a social media platform
ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

def binary_search_iterative(data, target) :
# {
    low = 0
    high = len(data)

    # search until the length of the interval > 1
    while high - low > 1 :
    # {
        mid = (low + high) // 2

        # Continue our search in [low, mid)
        if target < data[mid] :
        # {
            high = mid 
        # }

        # Continue our search in [mid, high)
        else :
        # {
            low = mid
        # }

     # }
      
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

# Let's say we want to find out what position a 30-year-old holds in our sorted list of ages
age_query = 30
result = binary_search_iterative(ages, age_query)

if result is not None :
# {
    print("Age of", age_query, "is found at position", result, "in the age list.")
# }

else :
# {
    print("No profile is found with age", age_query, ".")
# }

'''

********
BONEYARD
********

elif target < data[mid] :
        # {
            high = mid
        # }


'''