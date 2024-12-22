'''

A hearty welcome to our learners! Building on the foundation of our previous lesson on the importance of data structures, today we're venturing into the depths of a fundamental data structure in software engineering: the "Stack". Drawing parallels from the real world, a Stack operates just like a stack of plates. The last plate you put (push) on the stack will be the first one you take (pop) off. It's this simple principle that makes Stacks so powerful and widely used.

In this lesson, our learning objectives are to conceptualize Stacks, understand how to implement them, analyze their time and space complexity, and learn how to manipulate Stacks to solve algorithmic problems.

As today's lesson concludes, you will have gained the ability to implement a Stack in Python, understand its basic operations, and possess a robust knowledge of its applications in real-world scenarios.

Take a moment to visualize a real-life stack of plates. The logic behind Stacks in the realm of computer science mirrors this real-world stack closely. A Stack follows the principle of "Last In, First Out" (LIFO), meaning the most recent item you place on the Stack will be the first one to be removed. All elements in a Stack are added and removed from the top.

As a real-world comparison, consider the Stack to be a stack of books. You can only add (push) a book to the top of the stack, and similarly, to remove (pop) a book, you must do so from the top of the stack. Suppose you need to access a specific book in the middle of the stack. In that case, you must remove (pop) all the books placed above it first.

We can utilize Python's built-in list datatype to implement a Stack. To build a Stack, we need to define the following three basic operations:

push - Adds an element to the top.
pop - Removes and returns the top element.
peek - Returns the top element without removing it.
Translating our understanding into Python code, these operations can be implemented as follows:

To better understand the concept, consider a scenario where we have an empty stack. We push 'A', 'B', and 'C' onto it, making 'C' our top element. We then pop the top element, 'C', from the stack, and 'B' becomes the new top element.

In Python, we use append() to push an element and pop() without an index to extract an element from the stack.

A situation to consider is when there are no elements to pop. In this instance, the pop() will throw an IndexError. To prevent this, we should check if the Stack is empty before popping elements. This circumstance, where there's nothing left to pop, is referred to as Stack Underflow. Conversely, if the Stack has reached its maximum capacity and we try to add an item to it, it's referred to as Stack Overflow.

Let's unravel the complexities (pun intended!) behind these Stack operations. All three of our basic operations — push, pop, and peek — have a time complexity of 
O
(
1
)
O(1), meaning they take constant time to complete, regardless of the size of the Stack.

Contrarily, the space complexity is 
O
(
n
)
O(n), where 
n
n is the number of elements in the Stack. This is considering an average scenario where elements are continually added and then removed from the Stack.

Now that we've understood the fundamentals of Stack and its operations, let's focus on manipulating our Stack to gain a deeper understanding. We'll start by emptying our Stack and then confirm that it is indeed empty.

In Python, we can check if the Stack is empty by checking its length. Let's create a helper function named isEmpty(stack):

Having understood our Stack's manipulations, let's explore some real-world applications of Stacks. They are used widely in numerous areas, including parsing expressions, navigating browser history, implementing the "undo" operation in text editors, and more.

Consider this scenario: We have a text editor that stores the history of text changes. Our task is to use a Stack to implement the "undo" feature — when the user performs an "undo" operation, the text reverts to its previous version - the last historic change stored in the stack. Here’s an example:

'''

# Create an empty stack
stack = []

# Push elements
stack.append('A')
stack.append('B')
stack.append('C')

print(stack) # Output: ['A', 'B', 'C']

# Pop an element
topElement = stack.pop()
print("Popped Element:", topElement) # Output: 'C'

# New top of the stack
newTopElement = stack[-1]
print("Top Element after Pop:", newTopElement) # Output: 'B'

def is_empty(stack) :
# {
    return len(stack) == 0
# }

# Create an empty stack
stack = []

print(is_empty(stack))
# Output: True; as our stack is currently empty

stack.append('D')

print(is_empty(stack))
# Output: False; now our stack has an element 'D'

# Fetch the size of the stack
stack_size = len(stack)

print("Size of Stack:", stack_size)
# Output: 1; length of stack is 1

# Create a stack to store text changes
# The stack stores all historical versions of editor states, excluding the current state
text_stack = []

# The user inputs text
text_stack.append("Hello, world!")
text_stack.append("Hello, CodeSignal!")

print(text_stack)
# Output: ["Hello, world!", "Hello, CodeSignal!"]

# Check if the stack is empty before performing "undo"
if (is_empty(text_stack)) :
# {
    print("Cannot perform undo operation. There are no historic changes.")
# }

else :
# {
    # The user performs an "undo" operation
    previous_text = text_stack.pop() # Retrieve the last historic change
    print("After ""undo"", the text is: ", previous_text)
# }

# Output: After "undo", the text is: Hello, CodeSignal!

'''

***** BONEYARD *****

'''