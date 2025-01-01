'''

Bravo! You've begun your journey with Stacks and have successfully implemented the push and pop operations. Now, let's delve further and hone your debugging skills through a case study.

Imagine you are maintaining a library system. Your stack represents a stack of books, and thankfully, the existing system can successfully add a new book (push operation) or remove a book (pop operation) from the stack.

However, there is a problem - each time a book is popped, the system doesn't display the correct book that should now be on top.

Can you discern what's wrong and fix the system permanently? Best of luck!

'''

class Stack :
# {
    def __init__(self) :
    # {
        self.stack = []
        self.maxSize = 10  # assuming a stack size limit for this example
    # }

    def push(self, item) :
    # {
        if (len(self.stack) < self.maxSize) :
        # {
            self.stack.append(item)
        # }

        else :
        # {
            print("Stack Overflow. Cannot add more items.")
        # }

    # }

    def pop(self) :
    # {
        if (len(self.stack) > 0) :
        # {
            print("Pop element:", self.stack[len(self.stack) - 1])
            return self.stack.pop()
        # }

        else :
        # {
            print("Stack Underflow. Stack is empty.")
            return None  # return a None value when the stack is empty
        # }

    def printStack(self) :
    # {
        print(self.stack)
    # }

# }

# create a Stack object
s = Stack()

# Push elements
for i in range(1, 4) : # we deliberately try to add elements in the range 1 to 3
# {
    print("Pushing Book", i, "into the stack")
    s.push(i)
# }

# Print the stack
print("Stack after pushing elements:")
s.printStack()

# Pop an element
topElement = s.pop()
print("Popped book: Book", topElement)

# Print the stack
print("Stack after popping an element:")
s.printStack()

'''

***** BONEYARD *****

'''