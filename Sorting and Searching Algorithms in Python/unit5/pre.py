'''

Hello, and welcome to another exciting session! Today, we're venturing into the world of Quick Sort, an especially vital algorithm in the realm of computer science. Quick Sort is generally regarded as one of the fastest and most efficient algorithms for sorting large data sets. In this lesson, we aim to delve into the nuts and bolts of Quick Sort's implementation and its complexity analysis.

Just to give you an idea of what to expect, imagine having a large pile of student test scores that need to be sorted in ascending order. As the number of students (or the data size) increases, sorting using basic algorithms becomes computationally expensive. That's when Quick Sort steps in — a divide-and-conquer algorithm that makes the sorting process quicker and more efficient, hence its namesake.

By the end of this lesson, you'll have a solid grasp of the Quick Sort algorithm, be able to implement it in Python, and understand how to analyze its time and space complexities.

The Quick Sort algorithm is notable for its approach to sorting an array — or a Python list. Quick Sort begins by selecting a pivot from the provided list, then separates the remaining elements into two groups — those less than the pivot and those greater than it, keeping their order in the initial array. This process is replicated recursively until the entire list is sorted.

For instance, consider a task like sorting books on a shelf alphabetically. You can think of Quick Sort as picking one book — let's call it the pivot book. You then move all books that come before it alphabetically to its left and those that come after it to its right. The same process is applied to the group of books on the left and the right of the pivot book continuously until all books are arranged in order.

Understanding the theory is excellent, but the understanding becomes profound when we put the theory into practice. Therefore, let's dive in and write the Python code for Quick Sort, making it as clear and understandable as possible.

First, we'll define a function named quick_sort that will take a list as input and return a sorted version of that list. The elements lesser than the pivot will move to its left, and the elements greater than the pivot will move to its right. Let's translate this into Python code:

Upon executing the script, the function will return [2, 3, 5, 6, 7, 9, 10, 11, 12, 14], which is a sorted version of the input list. This result aligns with the sorted list we obtained when we manually went through the sorting process.

The time complexity of an algorithm gives us an idea of how the runtime will increase relative to the input size. For Quick Sort, the time complexity can be described as 
O
(
n
log
⁡
n
)
O(nlogn) for average and best-case scenarios and 
O
(
n
2
)
O(n 
2
 ) for the worst-case scenario. The worst-case scenario arises when the pivot divides the array predominantly into one large sub-array and one small sub-array instead of equal halves. However, the efficient partitioning scheme ensures the average case is much more likely in practice, making Quick Sort one of the most efficient sorting algorithms in practical use.

As a workaround to achieve a higher probability of 
O
(
n
log
⁡
n
)
O(nlogn) complexity, the pivot can be chosen as a random element, not always as a middle one, to make the choice less deterministic:

Space complexity refers to the amount of memory an algorithm needs to complete its run. With Quick Sort, the space complexity stems primarily from its recursive nature. Each recursive call requires additional space on the call stack, proportional to the depth of recursion. However, Quick Sort averages an excellent space complexity of 
O
(
log
⁡
n
)
O(logn).

It is possible to implement quick sort without using recursion; in that case, the additional space complexity will be 
O
(
1
)
O(1).

Owing to its efficiency, Quick Sort is extensively used in real-world applications. In computing sciences, it is commonly employed for tasks like sorting a list of names, sorting a list of numbers, or similar tasks where sorting data is essential. Efficient sorting of data is integral to areas such as database management, resource allocation tasks, and many more scientific computations.

'''

import random

def quick_sort(arr) :
# {
    if len(arr) <= 1 :
    # {
        # if the array contains 0 or 1 element, it's already sorted
        return arr
    # }

    else :
    # {
        # pivot = arr[len(arr) // 2] # select a pivot as a middle element
        pivot = arr[random.randint(0, len(arr) - 1)]
        left = [x for x in arr if x < pivot] # elements less than `pivot`
        middle = [x for x in arr if x == pivot] # elements equal to `pivot`
        right = [x for x in arr if x > pivot] # elements larger than `pivot`
        return quick_sort(left) + middle + quick_sort(right)
    # }

# }

print(quick_sort([9, 7, 5, 11, 12, 2, 14, 3, 10, 6]))

'''

********
BONEYARD
********

# pivot = arr[random.randint(0, len(arr) - 1)]

'''