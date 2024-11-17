'''

Implementation of Binary Search in Python
To translate binary search into Python code, devise a function that takes in the sorted list and the target element. Start by establishing the boundaries of your search. Then, repeatedly halve the list until either the element is found or the list is exhausted. Let's implement binary search iteratively in Python:

In this function, the index of the target in the sorted list is returned. If the target is not found, the function returns None.

Similarly, we can implement binary search using recursion — a function that calls itself until a base case is met.

In the recursive version, the while loop is replaced by recursive calls to the function itself. The algorithm remains the same: find the middle, compare it with the target, and determine the next step.

Analyzing Binary Search Complexity
Binary search has excellent performance when it comes to time complexity - 
O
(
log
⁡
n
)
O(logn). This logarithmic time behavior makes binary search ideal for large datasets. This is because, with each comparison, binary search eliminates half of the elements, reducing the search time exponentially.

Regarding space complexity, the iterative version of binary search has a space complexity of 
O
(
1
)
O(1) as it only uses a fixed amount of space to store the data. However, the recursive version has higher space complexity — 
O
(
log
⁡
n
)
O(logn) — since it uses additional space in the form of a call stack during recursive tasks.

Bonus Exercise: Binary Search to Solve an Advanced Problem
With a clear understanding of binary search, we can now use it to solve a complex problem — searching for a target element in a rotated sorted list. This involves figuring out the rotation point and applying binary search accordingly.

Consider a list like this [7, 8, 9, 2, 3, 4]. This list was sorted from 2 to 9, but then it was rotated to the fourth position. Suppose we want to search for the number 3. We can see that it's in the latter half, but how does our algorithm determine this?

As a bonus exercise, try to apply binary search to solve this question! We will cover the analysis of this question in the next lessons.

'''

def binary_search_iterative(data, target) :
# {
    # We will search in the interval [low, high), where the right border is excluded
    low = 0
    high = len(data)

    while high - low > 1 : # search until the length of the interval > 1
    # {
        mid = (low + high) // 2

        if target < data[mid] :
        # {
            high = mid # Continue our search in [low, mid)
        # }

        else:
        # {
            low = mid # Continue our search in [mid, high)
        # }
    
    # }

    if (data[low] == target) :
    # { 
        return low
    # }

    else :
    # {
        return None
    # }

    # return low if data[low] == target else None

# }

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

'''

********
BONEYARD
********

'''