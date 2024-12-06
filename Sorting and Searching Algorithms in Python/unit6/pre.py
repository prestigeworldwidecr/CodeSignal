'''

Greetings! Today, we are delving into the deep realm of the Merge Sort algorithm. As our journey unfolds, we will explore its core principles, examine its implementation in Python, and start to comprehend its complexities.

Do you recall when we dealt with Binary Search? Those lessons centered around the strategic organization and efficient retrieval of information. Now, we transition into sorting, an essential aspect of data organization. Merge Sort exemplifies an efficient method of sorting information. Imagine receiving an unorganized deck of cards and needing to shuffle them perfectly in a specific order. Merge Sort operates in a similar way. Let's unravel the intricacies of this innovative sorting algorithm.

Merge Sort is a reliable, stable algorithm that employs the Divide and Conquer strategy. It splits an unsorted list into two sublists, recursively sorts each of them, and then merges these sorted sublists to create a sorted list.

To put it in real-world terms, suppose you have a shuffled deck of playing cards and want to sort it. One approach is to divide the deck into two, sort each half, and then merge the halves to get a sorted deck. That's the fundamental concept behind Merge Sort. The idea becomes increasingly clear as we apply it in practice.

Let's put Merge Sort into action. For the simplest case — an empty list or a list with one element — it's already sorted. If the list has more than one element, we divide it into two lists, each approximately half the size of the original, sort both halves recursively, and merge them into a single sorted list.

In the above code, the merge_sort() function partitions the list and recursively sorts both halves. The merge() function merges two sorted lists into a single sorted list.

To gain a comprehensive understanding of how Merge Sort works, it's beneficial to examine the key operation — merging two sorted lists.

Merge Sort's distinguishing technique is merging two sorted lists. Let's consider two sorted lists: [1, 5, 6, 8] and [2, 3, 7, 9]. Our objective is to merge them into one sorted list, which allows us to understand how Merge Sort operates.

Here's how we do it:

Maintain two pointers, each initialized to the start of either list.
Compare the elements each pointer points to. Add the smallest element to our final list and advance that list's pointer by one step - this element is the smallest throughout all remaining elements in both arrays.
Repeat this process until we've appended all the elements from one of the lists to the final list.
Once we've exhausted the elements of one list, we append the leftover elements from the other list to the resulting list.

This crucial mechanism drives the assembly of Merge Sort.

The time complexity of Merge Sort is 
O
(
n
log
⁡
n
)
O(nlogn) in all cases — best, average, and worst. This consistent efficiency is an advantage over other algorithms, such as Quick Sort, which can degrade to a time complexity of 
O
(
n
2
)
O(n 
2
 ) under unfavorable conditions.

To recap, a time complexity of 
O
(
n
log
⁡
n
)
O(nlogn) implies that the running time increases linear-logarithmically with the size of the input. This characteristic makes Merge Sort highly efficient at handling large data sets.

The space complexity of Merge Sort is 
O
(
n
)
O(n), due to the auxiliary space used for the temporary arrays while merging the elements. This requirement is crucial to keep in mind and can be a deciding factor when selecting an algorithm in situations with limited memory.

Now that we understand Merge Sort's mechanics, it's time to apply it to solve a real-world problem. Let's start with a straightforward task: sorting a list of randomly generated numbers. We'll use Python's random module to generate the list.

We've covered a lot today, so let's recap what we've learned. Merge Sort is a reliable and efficient sorting algorithm. It repeatedly partitions the list until we have lists that are trivially sorted and then merges those lists back into larger sorted lists until the entire list is sorted. Also, we discussed the algorithm's time and space complexity — 
O
(
n
log
⁡
n
)
O(nlogn) and 
O
(
n
)
O(n), respectively. Finally, we saw how Merge Sort sorts a real-world list of numbers.

Imagine dealing with a set of logistical data, where each data point is a package to be delivered, and each package has a deadline. Sorting this data by the delivery deadline could significantly streamline your logistics process — a task for which Merge Sort is ideally suited.

'''

def merge_sort(lst) :
# {
    # If it's a single element or an empty list, it's already sorted
    if (len(lst) <= 1) :
    # {
        return lst
    # }

    # Find the middle point
    mid = len(lst) // 2

    # Recursively sort both halves
    left_half = merge_sort(lst[0: mid: ])
    right_half = merge_sort(lst[mid: len(lst): ])

    # Merge the two sorted halves
    return merge(left_half, right_half)

# }

def merge(left, right) :
# {
    result = []
    i = 0
    j = 0

    # Compare the smallest unused elements in both lists and append the smallest to the result
    while (i < len(left) and j < len(right)) :
    # {
        if (left[i] < right[j]) :
        # {
            result.append(left[i])
            # i += 1
            i = i + 1
        # }

        else :
        # {
            result.append(right[j])
            # j += 1
            j = j + 1
        # }

    # }

    # Once we've exhausted one list, append all remaining elements from the other list to the result
    # Here, we append both lists, as at least one is an empty list
    result.extend(left[i: : ])
    result.extend(right[j: : ])
    return result

# }

import random

# Generate a list of 100 random numbers between 1 and 1000
# random_numbers = [random.randint(1, 1000) for i in range(100)]
random_numbers = []

for i in range(100) :
# {
    random_numbers = random.randint(1, 1000)
# }

print("Original List: ", random_numbers)

# Outputs: Original List: [402, 122, 544, 724, 31, 515, 845, 2, 168, 311, 262, 498, 421, 25, 757, 171, 795, 634, 115, 572, 232, 94, 547, 177, 823, 607, 571, 403, 274, 527, 951, 971, 161, 771, 877, 969, 650, 37, 723, 497, 520, 571, 948, 886, 542, 795, 580, 933, 155, 692, 559, 259, 907, 516, 294, 625, 152, 287, 75, 614, 719, 10, 828, 157, 574, 257, 853, 271, 873, 745, 233, 519, 272, 405, 541, 912, 294, 737, 940, 154, 49, 77, 464, 416, 738, 143, 364, 223, 385, 201, 636, 493, 757, 10, 792, 555, 384, 362, 101, 109]

# Sort the list
sorted_numbers = merge_sort(random_numbers)

print("\nSorted List:", sorted_numbers)

# Outputs: Sorted List: [2, 10, 10, 25, 31, 37, 49, 75, 77, 94, 101, 109, 115, 122, 143, 152, 154, 155, 157, 161, 168, 171, 177, 201, 223, 232, 233, 257, 259, 262, 271, 272, 274, 287, 294, 294, 311, 362, 364, 384, 385, 402, 403, 405, 416, 421, 464, 493, 497, 498, 515, 516, 519, 520, 527, 541, 542, 544, 547, 555, 559, 571, 571, 572, 574, 580, 607, 614, 625, 634, 636, 650, 692, 719, 723, 724, 737, 738, 745, 757, 757, 771, 792, 795, 795, 823, 828, 845, 853, 873, 877, 886, 907, 912, 933, 940, 948, 951, 969, 971]

'''

********
BONEYARD
********

'''