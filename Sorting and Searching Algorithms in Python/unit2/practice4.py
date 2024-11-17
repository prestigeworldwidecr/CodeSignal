'''

Excellent work, astronaut! As the final step in our exploration of Binary Search, you have a mission to undertake!

Consider this exciting real-life scenario: you possess a sorted list of grades for a class, and a student is eager to ascertain his/her position within the list. Your assignment is to implement Binary Search on this list to locate the specific position of a given grade.

Prepare yourself for an exciting journey!

'''

# TODO: Given a sorted list of grades in a class, implement Binary Search on this list
grades = [35, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

def binary_search_recursive(data, target, low, high) :
# {
    if (high - low <= 1) :
    # {
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
    
    else :
    # {
        None
    # }

    mid = (low + high) // 2

    if target < data[mid] :
    # {
        return binary_search_recursive(data, target, low, mid)
    # }

    else :
    # {
        return binary_search_recursive(data, target, mid, high)
    # }

# }

# TODO: Implement the Loop-based Binary Search function without recursion
def binary_search_iterative(data, target) :
# {
    # We will search in the interval [low, high), where the right border is excluded
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
        else:
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

# TODO: Set a query for a student's grade for your search
binary_search_iterative(grades, 50)


# TODO: Invoke the Binary Search function. If you find the grade, print the position in the grade list; if not, print a not found message.
result = binary_search_recursive(grades, 50, 0, len(grades) - 1)

if (result is None) :
# {
    print("not found message.")
# }

else :
# {
    print("the position in the grade list:", result)
# }

'''

********
BONEYARD
********


# def binary_search_iterative(data, target)
# grades = [35, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

def binary_search_recursive(data, target, low, high) :

'''