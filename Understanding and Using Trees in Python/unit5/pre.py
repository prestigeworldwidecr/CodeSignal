'''

Welcome to this enriching session! Today, we will delve deeper into heaps by applying them to two intriguing problems. This will help you understand how heaps, a form of tree structure, can create efficient solutions to practical problems. Before we begin, remember that heaps are a type of priority queue where parent nodes always have values lesser (in a Min Heap) or greater (in a Max Heap) than their child nodes. This property is the foundation of our problem-solving approach with heaps.

Consider this scenario: You're working on an algorithm for a real-time analytics engine that calculates the median value of a continuously growing dataset. For instance, an ad tech company might need to analyze click-stream data in real time. Our first problem is to create a data structure that supports adding a number while ensuring efficient retrieval of the median at any given point.

Note: A median value is the middle number in a data set when arranged in ascending order. If there is an even number of data points, the median is the average of the two numbers in the middle. It is a measure of central tendency used in statistics.

One initial approach could be to save each incoming number in a Python list. Whenever we need the median, we can sort the list and compute it. However, as the list length increases, the time to sort the list also grows as sorting has a time complexity of 
O
(
n
log
⁡
n
)
O(nlogn) per each median search request. Thus, this approach becomes less efficient when we want to add and retrieve the median frequently.

One initial approach could be to save each incoming number in a Python list. Whenever we need the median, we can sort the list and compute it. However, as the list length increases, the time to sort the list also grows as sorting has a time complexity of 
O
(
n
log
⁡
n
)
O(nlogn) per each median search request. Thus, this approach becomes less efficient when we want to add and retrieve the median frequently.

Efficient Approach
A smarter way to solve this problem is to maintain two heaps - a max heap to store the smaller half of the numbers and a min heap for the larger half.

If the heaps are kept balanced in their size, finding the median can be done in 
O
(
1
)
O(1) time - you need just the maximal value from the first half (Max Heap), and the minimal value from the second half (Min Heap) - these two elements should be enough to calculate the median value.

New element addition at the same time can be done in 
O
(
log
⁡
n
)
O(logn) time: the new element can be just added to the first half heap (Max Heap), but after that heaps should potentially be rebalanced to keep their sizes differ by at most 1. However, due to the fact that after new element addition heap sizes differ by at most 2, moving just a single element from one heap to another should be enough, and this balancing can be done in 
O
(
log
⁡
n
)
O(logn) time.

Let's delve into the implementation specifics. We'll use Python's built-in module heapq, which allows us to create a standard min heap. By storing numbers as negatives, we can simulate a max heap.

First, we initialize two empty lists, which will serve as our heaps.

addNum(num: int) -> None: When a new number arrives, we store the number in the large heap (MinHeap). We maintain the balance between the heaps by removing the smallest element from large and pushing it into small (our simulated max heap). If large has fewer elements than small, we balance it by pushing the largest element from small to large.

findMedian() -> float: Finally, since large contains the larger elements, if large has more elements than small, the median is the smallest element in large. Otherwise, the median is the average of the smallest element in large and the largest in small.

'''

import heapq

class MedianFinder :
# {
    def __init__(self) :
    # {
        self.heaps = [], []
    # }

    def addNum(self, num):
    # {
        small = self.heaps 
        large = self.heaps

        heapq.heappush(small, -heapq.heappushpop(large, num))

        if (len(large) < len(small)) :
        # {
            heapq.heappush(large, -heapq.heappop(small))
        # }

        else :
        # {
            None
        # }

    # }

    def findMedian(self):
    # {
        small = self.heaps
        large = self.heaps

        if (len(large) > len(small)) :
        # {
            return float(large[0])
        # }

        else :
        # {
            None
        # }
        
        # We subtract `small[0]` from `large[0]`, because `small` consists of negative values
        return float((large[0] - small[0]) / 2.0)
    
    # }

# }

'''

***** BONEYARD *****

'''