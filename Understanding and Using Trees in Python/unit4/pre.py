'''

Topic Announcement and Overview
Greetings, learners! We are currently in the fifth lesson of our "Understanding and Using Trees in Python" course. So far, we have navigated the depths of tree structures, and today, we continue our expedition by climbing one of its fascinating branches - the Heap.

Heaps are versatile data structures with applications across various domains, simplifying tasks, such as forming efficient priority queues or sorting arrays, and further demonstrating their relevance in solving complex mathematical and computer science problems. This lesson will delve into heaps, exploring their types, the operations we can perform on them, and their applications in Python.


A heap is a complete binary tree that satisfies a special property known as the heap property. Essentially, the heap property stipulates that if P is a parent node of C, the value of node P is either greater than or equal to (in the case of a Max Heap) or lesser than or equal to (in a Min Heap) the value of node C. In simpler terms, in a Max Heap, each parent node is greater than or equal to its child node(s), and in a Min Heap, each parent node is less than or equal to its child node(s).

For a visual representation, consider the following example of a Max Heap:

In the above example, the parent nodes hold greater values than their respective child nodes, validating it as a Max Heap.

At the same time, the heap in the example below is a Min Heap.

Heaps support numerous operations, such as:

1. Insert: Inserting a new node in a heap may disrupt the heap property. To maintain the heap property after each insertion, the node is swapped with the parent node if the heap property is violated. This process continues until the heap property is retained for all nodes.

2. Delete: The deletion of a node also disrupts the heap property. After deleting a node, the heap property is restored either by swapping the node with its parent, similar to the Insert operation or by swapping it with one of its children. The swapping process continues until the heap property is retained for all nodes.

3. Extract: Extracting the maximum (for Max Heap) or minimum (for Min Heap) is a constant-time operation, as the maximum or the minimum element is always at the root of the heap.

The "Heapify" method is an intriguing function used to rearrange elements in heap data structures. It assists in preserving the heap property within the heap. In Python, this operation can be executed using the heapify() function. Here's how we can implement a min heap using a list:

This heapify() function converts a regular list into a heap. It rearranges the list in place to satisfy the heap property. In the resulting heap, the smallest element is positioned at index 0. But how do we program other heap operations such as extract, insert, or delete?

Python offers a vast range of libraries, including a built-in module, heapq, which allows for the creation and manipulation of heaps with ease.

In the given snippet, the heappush(heap, ele) function is used to insert elements while maintaining the heap invariant, heappop(heap) function deletes the smallest element, and the nsmallest(n, iterable[, key]) function returns n smallest elements from the iterable or heap.

Heaps can also be useful for efficiently sorting elements in the array. This sorting is called heap sort algorithm. This algorithm essentially splits into two basic parts:

Build a MinHeap out of the array
Repeatedly remove the minimum element from the heap and insert it into the sorted array while ensuring the heap retains the MinHeap property.
Heap sort is a comparison-based sorting algorithm and is particularly efficient when dealing with large datasets due to its 
O
(
n
log
⁡
n
)
O(nlogn) time complexity - the algorithm removes the minimal element in 
O
(
log
⁡
n
)
O(logn) time and repeats this operation 
n
n times.

The heapify function transforms our list into a min-heap, and we continue extracting the minimum element until our heap becomes empty, resulting in a sorted list. Let's see how Python's built-in heapq module simplifies heap-sort:

Exceptional progress, learners! You've made it through heaps, their operations, and their Python implementation. We've unearthed what heaps are, their different variations, the various operations one can perform on heaps, and how these can be conveniently implemented in Python using the heapq module.

Heaps embody one of the fundamental concepts in the realm of data structures, and a solid understanding of how they work is crucial for efficiently tackling complex problem statements. However, we've only just started. There is so much more to discover about heaps and their capabilities.

'''

import heapq

minHeap = [4, 7, 2, 8, 1, 3] 
heapq.heapify(minHeap)

# Display the heap
print("Heapify method: ", minHeap)
# Output: Heapify method:  [1, 4, 2, 8, 7, 3]

# import heapq

heap = []

# Insert in heap
heapq.heappush(heap, 4)
heapq.heappush(heap, 9)
heapq.heappush(heap, 6)

print("Heap after insertion: ", heap)
# Output: Heap after insertion:  [4, 9, 6]

# Delete the smallest element from the heap
heapq.heappop(heap)
print("Heap after deletion: ", heap)
# Output: Heap after deletion:  [6, 9]

# Extract the smallest element
smallest = heapq.nsmallest(1, heap)[0]
print("Smallest element in the heap: ", smallest)
# Output: Smallest element in the heap:  6

def heap_sort(arr) :
# {}
    import heapq
    heapq.heapify(arr)
    # return [heapq.heappop(arr) for _ in range(len(arr))]

    for _ in range(len(arr)) :
    # {
        heapq.heappop(arr)
    # }

    return heapq

# }

print(heap_sort([3, 2, 1, 7, 8, 4]))
# Output: [1, 2, 3, 4, 7, 8]

'''

***** BONEYARD *****

'''