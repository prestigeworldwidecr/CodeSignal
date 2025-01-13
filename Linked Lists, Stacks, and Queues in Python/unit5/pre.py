'''

In our journey to understand the advanced practical applications of the queue data structure in Python, we are now prepared to apply our knowledge to solve some common interview questions based on queue operations. Today's session is focused on working through two such problems. Let's get cracking!

In the domain of data structure manipulation, understanding how we can handle queue operations efficiently is fundamental. For our first problem, consider a queue of integers. Our task is to reorganize the elements by interleaving the first half of the queue with the second half. Essentially, if our queue initially is [1, 2, 3, 4, 5, 6], after interleaving it becomes [1, 4, 2, 5, 3, 6]. The problem tests how we can shrewdly manipulate a queue data structure to reorder its elements in a specific manner.

Problem 1: Naive Approach and Its Pitfalls

A naive approach to solving this problem might be to dequeue all the elements into another data structure like a list or a stack, perform the reordering operation, and then enqueue the elements back into the queue. However, this method introduces non-optimal time and space complexity due to the extensive use of auxiliary space, and it doesn't adhere to the spirit of the queue data structure, which typically only allows FIFO (First-In-First-Out) operations.

The most efficient way to solve this problem involves exploiting advanced queue operations to our advantage. Specifically, the idea is to split the queue into two halves, then repeatedly dequeue an element from each half and enqueue it back into the queue until all elements from both halves are exhausted. This procedure accomplishes the interleaving using only a constant amount of additional space and in linear time, adhering to the FIFO spirit of the queue.

The solution to the problem can be built as follows:

Create a function interleave_queue that takes a queue as an argument.
Calculate the midpoint. If the queue's length is odd, round up to make sure the second half is larger.
Perform the interleaving operation by repeatedly dequeuing one element from the first half and one from the second half, then enqueue the two elements back into the queue in the original order.
The function should return the interleave queue.

We initialize a new deque named first_half to temporarily store the first half of the queue items for the interleaving operation.

These two lines perform the operation of subtracting elements from the beginning of the original queue and adding them into the first_half queue until we reach the midpoint of the original queue. Note that we don't need a second_half, as we remove elements from the original queue.

If there is an odd number of elements, we move the middle element to the end.

These lines are responsible for the actual interleaving. The while loop runs as long as first_half isn't empty. Within the loop, we remove (dequeue) an item from the start of both first_half and queue (in that order), then add (enqueue) them to the end of queue. This continues until first_half is exhausted.

This Python function interleave_queue() manipulates a deque as a queue. It performs the interleaving operation by repeatedly dequeuing an element from the first half and one from the second half, then enqueuing the two elements back into the deque in order. The deque is finally returned after the interleaving operation is finished.

Moving on to the next problem, we step into the domain of real-time data analysis, where we encounter a continuous stream of data rather than isolated pieces of data. Here, you are given a stream of integers and are required to calculate a moving average of a specific window size m for each number in the stream. This is a classic problem in financial programming and data science, and understanding this problem will enable you to build more advanced data analysis models. While the problem is not directly related to queues, it requires manipulating a queue in a complex scenario and can be faced during a technical interview.

Problem 2: Naive Approach and Its Pitfalls

A naive approach to this problem would involve continually updating the list with every new data point, removing the oldest data point if the window size is exceeded, and recalculating the average for every new data point. However, recalculating the average again and again can be computationally expensive, particularly when dealing with large data streams.

We can optimize this process by maintaining a sum that accumulates with every new data point added to the window. When the window size reaches our predetermined size m, the oldest data point is automatically removed from the window as a new data point enters. Thus, with each new data point entering the window, we simply subtract the oldest data point removed and add the new data point to our maintained sum.

To solve this problem:

Instantiate your queue and set it up to retain the last m numbers. Initialize a total variable that will help keep track of the sum of the numbers in the window, and also set up an instance variable size that will keep track of the value m provided at the start of the analysis.
For every incoming number, keep adding it to your queue. Every time a number is added to the queue, subtract the oldest number from the total sum if the size of the queue has reached m.
Return the moving average, calculated by dividing the total sum by the current size of the window.
The function has a time complexity of 
O
(
1
)
O(1) and a space complexity of 
O
(
m
)
O(m) because it stores m numbers.

Here is the Python code for the approach outlined above:

The MovingAverage class uses a list to simulate a queue. It consistently adds new values to the queue while removing the earliest added value in cases where the queue's size has reached its limit, i.e., size.

'''

from collections import deque

first_half = deque()

for _ in range(half_size) :
# {
    first_half.append(queue.popleft())
# }

if (N % 2 == 1) :
# {
    queue.append(queue.popleft())
# }

while (first_half) :
# {
    queue.append(first_half.popleft())

    if (queue) : 
    # {
        queue.append(queue.popleft())
    # }

    else :
    # {
        None
    # }

# }

def interleave_queue(queue) :
# {
    half_size = len(queue) // 2
    first_half = deque

    for _ in range(half_size) :
    # {
        first_half.append(queue.popleft())
    # }

    while (first_half) :
    # {
        queue.append(first_half.popleft())

        if (queue) : 
        # {
            queue.append(queue.popleft())
        # }

        else :
        # {
            None
        # }
    # }
    
    return queue

# }

class MovingAverage :
# {
    def __init__(self, size) :
    # {
        self.queue = deque
        self.size = size
        self.total = 0
    # }

    def calculate_moving_average(self, val) :
    # {
        if (len(self.queue) == self.size) :
        # {
            # self.total -= self.queue.popleft()
            self.total = self.total - self.queue.popleft()
        # }

        else :
        # {
            None
        # }

        self.queue.append(val)
        # self.total += val
        self.total = self.total + val

        return round(self.total / len(self.queue), 2)
    
    # }

# }

'''

***** BONEYARD *****

'''