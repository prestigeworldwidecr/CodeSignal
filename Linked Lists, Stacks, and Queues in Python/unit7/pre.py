'''

Welcome to our exciting course, "Linked Lists, Stacks, and Queues in Python". Here, we aim to decode and comprehend the fundamentals and advanced concepts of Python's data structures. In this lesson, we delve deeper into applying two basic operations on Linked Lists – traversing through a list and calculating its length. These operations are akin to taking a walk down a street and counting the number of houses you have passed.

First, we define our goal and understand why we perform it. We then have a go at it using a straightforward approach before learning the efficient technique to accomplish it like a pro!

While walking down a street, imagine you had to document each house but in reverse order. This presents a similar scenario, but instead, we are dealing with a linked list. The task is to traverse the list in reverse form and print all the elements.

Problem 1: Application

Traversing a list in a reverse manner is often encountered when you need to know the last state or the most recent actions in a scenario. For instance, in a browser history, the most recent web pages are usually at the top of your browsing history. In such a situation, you would need to traverse the list from the tail to the head.

Problem 1: Naive Approach

A simplistic approach to the problem might be to create an array from the Linked List, reverse it, and iterate over it. However, this approach is not efficient because creating an array requires extra space, leading to higher memory usage. Furthermore, reversing an array requires additional time complexity.

To traverse a Linked List in reverse, we start from the tail node and move up to the previous node until we reach the head. However, because linked lists are generally singly linked lists and do not provide a direct way to access previous nodes, we must take a different approach. We can push all nodes onto a stack and then pop them out. This will give us the nodes in reverse order.

Unlike a book where you can quickly flip to the previous page, we have to navigate through the 'book' once (in other words, traverse the Linked List from head to tail), but 'mark' every page we visit (push every node on a stack). We then revisit the marked pages in reverse order (pop each node from the stack).

In this Python code, we start at the head of our Linked List and use a while loop to push every node into our stack until we have reached the tail. We then use another while loop to pop each element from the stack until it's empty, effectively printing the data in reverse order.

The second problem in our journey is about finding the length of our Linked List. If our linked list were a playlist, our task would be to determine the number of songs in it.

Problem 2: Application

In many real-world scenarios, one might need to evaluate the length of a Linked List. For instance, if you run a call center and have a queue of calls waiting to be addressed, knowing the number of pending calls helps manage your resources more effectively.

Problem 2: Naive Approach

One might think of using Python's len() function to find the length of our custom linked list object. However, len() only works with Python's built-in list type, so our Linked List would be beyond its capabilities.

To determine the length of a Linked List, we employ a strategy similar to our traversal. The difference, however, is that we use a counter during our 'journey' from the head to the tail and increment it each time we visit a new node. This counter then gives us the total number of nodes in the Linked List, hence, its length.

In this piece of code, we set current_node to self.head and a counter length to 0. We then start our traversal from the head node, and for every node we traverse, we increment our counter length by 1. This process continues until we reach a node that does not point towards the next Node – a node where next = None. The final value of the counter length gives us the length of our Linked List.

'''

class Node :
# {
    def __init__(self, data=None):
    # {
        self.data = data
        self.next = None 
    # }

# }

class LinkedList :
# {
    def __init__(self):
    # {
        self.head = None
    # }

    def LinkedList_reverseTraversal(self):
    # {
        node = self.head
        stack = []

        while (not node):
        # {
            stack.append(node.data)
            node = node.next
        # }

        while (stack) :
        # {
            print(stack.pop())
        # }

    # }

# }

class Node :
# {
    def __init__(self, data=None):
    # {
        self.data = data
        self.next = None 
    # }

# }

class LinkedList :
# {
    def __init__(self):
    # {
        self.head = None
    # }

    def LinkedList_length(self):
    # {
        current_node = self.head
        length = 0

        while (not current_node) :
        # {
            # length += 1
            length = length + 1
            current_node = current_node.next
        # }

        return length
    # }

# }

'''

***** BONEYARD *****

'''