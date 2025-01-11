'''

Champion code breaker! You've been assigned a task to implement a task management system. However, it seems the system doesn't function correctly, preventing your squad from proceeding with their tasks as expected.

The tasks currently added to the queue are not displayed properly, and the system doesn't provide any indication upon task completion. Your role is to locate the mistake and rectify it!

Must you identify and rectify the problem within the provided code to ensure tasks are performed consecutively and each task’s completion is confirmed accordingly. Let's get cracking. Remember, your entire team is relying on you!

'''

# Import required libraries
import time
from collections import deque

# Define an empty deque to represent our queue
queue = deque([])

# The initial queue is empty
print("Initial queue: ", queue)

# We add some elements to the queue
queue.append("Task1")
queue.append("Task2")
queue.append("Task3")

print("Queue after enqueue operations: ", queue)

# Additional tasks join the queue while processing earlier tasks
queue.append("Task4")
queue.append("Task5")

print("Queue after adding more tasks: ", queue)

# Process tasks one by one
while (queue) :
# {
    # This should always remove the first task
    # current_task = queue.pop()
    current_task = queue.popleft()
    print("\nNow performing:", current_task)

    # Simulate time delay for performing a task
    for i in range(3, 0, -1) :
    # {
        print(current_task, "will be complete in", i, "seconds...", end='\r')
        time.sleep(1)
    # }

    print("\n", current_task, "is complete!")
    print("Queue after dequeue operation: ", queue)

# }

# Queue should be empty after all tasks are done
assert len(queue) == 0, "The queue should be empty after all tasks have been performed"

print("\nAll tasks have been performed! The queue is now empty.")

'''

***** BONEYARD *****

'''