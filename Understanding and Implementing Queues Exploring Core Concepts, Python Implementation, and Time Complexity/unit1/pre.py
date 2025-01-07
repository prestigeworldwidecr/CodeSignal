'''

Today's session will be an exciting exploration of the Queue data structure. Much like stacks, which operate on the "Last-In, First-Out" or LIFO principle, queues function on the opposite principle of "First-In, First-Out" or FIFO. Consequently, the first item entered into the queue is also the first one out.

The real-world analogy would be a queue at a grocery store checkout. The person who has been waiting in line the longest is served first, then the next person, and so on. The last person to join the queue will be the last one to be served. In computer science, we utilize the same concept.

In this lesson, we aim to delve deeper into this concept - understanding Queues, uncovering their Pythonic implementation, and analyzing the time and space complexities associated with their functionalities.

At its core, a Queue is a sequential collection of elements that follows a "First-In, First-Out" (FIFO) principle. It operates much like real-world queues or lines, where the first element inserted is the first one to be removed. For example, consider a line of people waiting to buy tickets at a theater. The person who arrives first gets their ticket first. In computer science, a Queue works in exactly the same way.

In Python, we can implement Queues using built-in data types. Indeed, the Python list datatype comes in handy here. Python lists, however, have a significant drawback: the pop(0) method has 
O
(
n
)
O(n) time complexity, while we would like it to be 
O
(
1
)
O(1). There is another Python module named collections that offers deque, a flexible container that serves both as queue and stack implementations. We will use the deque data structure to implement the queue in this lesson.

With Python, implementing a Queue is quite simple. We begin by creating an empty Queue, for which we can use Python's built-in deque.

We can add or enqueue elements to the end of the Queue using the append() method. Similarly, the removal or dequeue of an element from the start of the Queue can be done using the popleft() method.

We added three elements to our queue: Alice, Bob, and Charlie. When we wanted to remove an element, it removed Alice, who was the first member enqueued into our queue, demonstrating the FIFO principle of a queue. Note that we need to use the popleft() method for it.

In order to make smart decisions about data structures, it's important to be mindful of their time and space complexities. In the case of a Queue implemented using the collections.deque, the time complexity for both the enqueue (adding an element at the end of the Queue) and dequeue (removing an element from the start of the Queue) operations is 
O
(
1
)
O(1). This is because dequeue is implemented in a way that is very fast to change the first and the last elements. We will talk about this implementation, called Doubly Linked Lists, in further lessons.

A Queue can be very useful when we need to manage tasks according to their arrival. This can be an efficient strategy in certain types of algorithms and, specifically, in a multitasking environment.

In this example, we're sending multiple print jobs to the printer. The jobs include Document1, Document2, and Picture1. According to our Queue implementation, the printer first prints Document1 as it's the first job added to the queue. Subsequently, Document2 and Picture1 are then printed in the order of their addition to the queue.

Queues can be more versatile than they might seem at first glance. For instance, in Graph theory, the Breadth-First Search (BFS) algorithm makes extensive use of Queues to check nodes across levels in the correct order in a graph traversal problem.

In this brief dive into the world of Queues, you've picked up key fundamentals of Queues, explored their Python implementation, and analyzed their time and space complexities. You've also learned how to manipulate Queues in Python and have considered their practical applications.

That wraps up our theoretical understanding of Queues. In the coming session, we'll be diving into practice problems to solidify your understanding and activate the knowledge you've just gained. I hope you're ready because this is where the fun begins!

'''

from collections import deque

queue = deque()

# Add elements
queue.append('Alice')
queue.append('Bob')
queue.append('Charlie')

print(queue)  # Output: deque(['Alice', 'Bob', 'Charlie'])

# Remove an element
queue.popleft()

print(queue)  # Output: deque(['Bob', 'Charlie'])

from collections import deque

# Printer Queue
printer_queue = deque()

# Send jobs to the printer
printer_queue.append('Document1')
printer_queue.append('Document2')
printer_queue.append('Picture1')

# Start processing jobs
while (printer_queue) :
# {
    job = printer_queue.popleft()
    print("Currently printing:", job)
# }

# Output:
# Currently printing: Document1
# Currently printing: Document2
# Currently printing: Picture1

'''

***** BONEYARD *****

'''