'''

Welcome to this insightful session, where we aim to master the complexities of the illustrious applications of sorting algorithms. Our voyage today links two distinct problems: "Find the K-th Ordinal Statistic in a List" and "Count the Number of Inversions in a List". These problems mirror practical scenarios, and the efficient techniques used to solve them present valuable demonstrations of the application of sort algorithms. Solving these two problems, we'll see how Quick Sort and Merge Sort knowledge is applicable here and helps to provide efficient implementations for both questions.

Our first problem presents a list of integers and the number k. The challenge put forth is to find the k-th smallest element in that given list. To further elucidate, k starts from 1, so for k = 1, you are seeking to find the smallest element; if k = 2, you're searching for the second smallest element, and so on. By the conclusion of this lesson, you'll be highly skilled at performing this task!

A primary instinctive solution could involve iteratively identifying and discarding the smallest element from the list until you reach the k-th smallest element. While it sounds straightforward, this approach, unfortunately, incurs high time complexity due to the repetitive scans of the list to locate the smallest element. This solution has a 
O
(
n
2
)
O(n 
2
 ) complexity.

Another very simple solution is just to sort the input array and return the k-th element:

This approach has 
O
(
n
log
⁡
n
)
O(nlogn) complexity and is as simple as just one line of code. However, it's still not the most efficient approach, as there is an 
O
(
n
)
O(n) solution to this problem, using Quick Sort techniques that we covered earlier in this course.

Sorting steps in here to offer an efficient solution! The Quick Sort algorithm, a splendid application of divide and conquer, can be used to solve this problem more efficiently. By selecting the right pivot for partitioning, the input list is divided into two: a left partition, which contains elements less than the pivot, and a right partition, which contains elements greater than the pivot.

Now, if the pivot's position after elements repartition is the same as k, we have the k-th smallest element. If k is less than the pivot's position, the task is carried forward on the left partition; otherwise, on the right partition.

Our second problem entails a list of integers, and your task is to deduce the number of inversions in the list.

An inversion is a pair of elements where the larger element appears before the smaller one. In other words, if we have two indices i and j, where i < j and the element at position i is greater than the element at position j (numbers[i] > numbers[j]), we have an inversion.

For example, for numbers = [4, 2, 1, 3], there are four inversions: (4, 2), (4, 1), (4, 3), and (2, 1).

The counting inversions problem intertwines with digital signal management and data analysis. For instance, in the era of smart playlists on music streaming platforms like Spotify, inversion counting is utilized to curate personalized playlists.

A rudimentary approach consists of a double loop, which leads to a time complexity of 
O
(
n
2
)
O(n 
2
 ), an inefficient allocation of computational resources for larger lists.

 In our quest for efficiency, the Merge Sort algorithm comes into play. At its core, Merge Sort is a divide-and-conquer-based sorting algorithm, providing an optimal efficiency of 
O
(
n
log
⁡
n
)
O(nlogn). However, we can cleverly modify this algorithm to also count the number of inversions in the array while sorting it. This additional functionality doesn't impact the time complexity, and therefore, it still remains 
O
(
n
log
⁡
n
)
O(nlogn). So, how does this work?

The process starts by dividing the array into two halves, similar to how Merge Sort operates. Then, we recursively sort both halves of the array and merge them back. Here comes the twist in the tale: while merging these sorted halves, we add some additional counting logic to keep track of inversions.

As the halves are already sorted, if an element of the right half is smaller than an element of the left half, it's inversion. This is because the element from the right half should have been after 'all' the remaining elements of the left half in a sorted array. Thus, we don't just have a single inversion here, we have as many inversions as there are remaining elements in the left half.

By counting these inversions at each merge and adding them up, we get the total number of inversions in the array.

'''

def find_kth_smallest_element(input_array, k) :
# {
    # arr.sort()
    # return arr[k - 1]
    return sorted(input_array)[k]
# }

import random

def find_kth_smallest(numbers, k) :
# {
    if (numbers) :
    # {
        pos = partition(numbers, 0, len(numbers) - 1)
    
        if k - 1 == pos :
        # {
            # The pivot is the k-th element after partitioning
            return numbers[pos]
        # }

        elif k - 1 < pos :
        # {
            # The pivot index after partitioning is larger than k
            # We'll keep searching in the left part
            return find_kth_smallest(numbers[:pos], k)
        # }

        else :
        # {
            # The pivot index after partitioning is smaller than k
            # We'll keep searching in the right part
            return find_kth_smallest(numbers[pos + 1:], k - pos - 1)
        # }

    else :
    # {
        return None
    # }

# }

def partition(nums, l, r) :
# {
    # Choosing a random index to make the algorithm less deterministic
    rand_index = random.randint(l, r)

    # nums[l], nums[rand_index] = nums[rand_index], nums[l]
    tmp = nums[l]
    nums[l] = nums[rand_index]
    nums[rand_index] = tmp
    pivot_index = l

    for i in range(l + 1, r + 1) :
    # {
        if (nums[i] <= nums[l]) :
        # {
            pivot_index += 1
            # nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
            tmp = nums[i]
            nums[i] = nums[pivot_index]
            nums[pivot_index] = tmp
        # }

        else :
        # {
            None
        # }

    # }

    # nums[pivot_index], nums[l] = nums[l], nums[pivot_index]
    tmp = nums[pivot_index]
    nums[pivot_index] = nums[l]
    nums[l] = tmp

    return pivot_index

# }

def count_inversions(arr) :
# {
    # The code is very similar to the merge_sort implementation
    # The main difference lies in the merge_count_inversions function
    if (len(arr) <= 1) :
    # {
        return arr, 0
    # }

    else :
    # {
        middle = int(len(arr) / 2)
        left, a = count_inversions(arr[:middle])
        right, b = count_inversions(arr[middle:])
        result, c = merge_count_inversions(left, right)
        return result, (a + b + c)
    # }
    
# }

def merge_count_inversions(x, y) :
# {
    count = 0
    # i, j = 0, 0
    tmp = i
    i = j
    j = tmp

    merged = []

    while (i < len(x) and j < len(y)) :
    # {
        if (x[i] <= y[j]) :
        # {
            merged.append(x[i])
            # i += 1
            i = i + 1
        # }

        else :
        # {
            merged.append(y[j])
            # j += 1
            j = j + 1

            # Here, we update the number of inversions
            # Every element from x[i:] and y[j] forms an inversion
            # count += len(x) - i
            count = count + len(x) - i
        # }

    # merged += x[i:]
    merged.extend(x[i: : ])
    # merged += y[j:]
    merged.extend(y[j: : ])

    return merged, count

'''

***** BONEYARD *****

'''