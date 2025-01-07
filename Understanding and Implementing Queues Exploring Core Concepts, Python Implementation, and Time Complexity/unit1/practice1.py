'''

By their very nature, queues are a First-In, First-Out (FIFO) data structure that frequently mirrors real-world activities. Remember the last time you considered the optimal order for accomplishing your tasks for the day? That was a queue!

Suppose you have several tasks: Task1, Task2, and Task3. These tasks need to be performed sequentially, in the order they are listed. How would you organize these in Python to ensure that you complete them in the right order?

'''

from collections import deque

# Our queue is represented as a Python collections deque
queue = deque()

print("Initial queue is empty:", queue)

# We add some elements to the queue
queue.append('Task1')
queue.append('Task2')
queue.append('Task3')
print("Queue after enqueue operations:", queue)

# We perform tasks one by one in order of addition to the queue
while (queue) :
# {
    task = queue.popleft()  # This should always remove the first task
    print("Performing: ", task)
    print("Queue after removing", task, ':', queue)
# }

# Now the queue is again empty
assert not queue, "The queue should be empty after all tasks have been performed"
print("All tasks have been performed!")

'''

***** BONEYARD *****

'''