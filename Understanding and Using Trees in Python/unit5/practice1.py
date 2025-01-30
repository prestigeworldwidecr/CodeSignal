'''

Alright, it's time for a real challenge! Suppose you're working with a big stream of data, and your task is to support two operations on it:

Add a new integer number to the stream
Calculate the middle element value: in case the number of elements in the stream is odd, that's the middle element if stream elements are sorted, in case the number of elements is even, that's the largest element out of two middle stream elements.
For example, middleEl([1, 2, 3, 4, 5]) = 3 and middleEl([1, 2, 3, 4, 5, 6]) = 4.
Create a method, add_num(num: int) -> None, that takes an integer num as an argument and adds it to our data heap. Also, whip up another one, middle_element() -> int, which doesn't take any input but returns the middle element in the data.

Remember, the idea is to keep it simple! No complex phrases or highfalutin lingo, just clean, understandable, and practical code in your solution. And never mind edge cases or unusual inputs; our input data is always squeaky clean for this one! So put on your thinking cap and show me your moves!

'''

import heapq

class MiddleElementFinder :
# {
    def __init__(self) :
    # {
        self.heaps = [], []
    # }

    def add_num(self, num: int) -> None :
    # {
        # implement this
        small = self.heaps[0]
        large = self.heaps[1]

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

    def middle_element(self) -> int :
    # {
        # implement this
        small = self.heaps[0]
        large = self.heaps[1]

        if (len(large) > len(small)) :
        # {
            return float(large[0])
        # }

        else :
        # {
            None
        # }
        
        # We subtract `small[0]` from `large[0]`, because `small` consists of negative values
        print(large[0], small[0])

        return float((large[0] - small[0]) / 2.0)
    # }
    
# }

# Let's test the code
estimate_finder = MiddleElementFinder()
estimate_finder.add_num(5)
estimate_finder.add_num(10)
estimate_finder.add_num(3)
estimate_finder.add_num(1)
estimate_finder.add_num(7)

print(estimate_finder.middle_element()) # Expected output: 5

'''

***** BONEYARD *****

# heapq.heappush(list(small), -heapq.heappop(max(large)))
# print(MiddleElementFinder)

'''