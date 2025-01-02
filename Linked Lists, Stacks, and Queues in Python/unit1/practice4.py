'''

Fantastic work, Stellar Navigator! You have grasped the basic operations of a stack. Now, let's incorporate a twist into our journey.

In the realm of stacks, the operation known as peek is crucial; it enables us to examine the top element without removing it. Regrettably, the code required to perform the peek operation appears to have vanished in the cosmic dust. Could you assist in retrieving this operation?

Remember, our task is merely to inspect the top element of the stack without removing it!

'''

class Stack :
# {
    def __init__(self) :
    # {
        self.stack = []
        self.maxSize = 10
    # }

    def push(self, item) :
    # {
        if (len(self.stack) < self.maxSize) :
        # {
            self.stack.append(item)
            print("Pushed", item, "to the stack")
        # }

        else :
        # {
            raise Exception("Stack Overflow. Cannot push more items to the stack.")
        # }

    # }

    def pop(self) :
    # {
        if (len(self.stack) > 0) :
        # {
            popped_element = self.stack.pop()
            print("Popped element:", popped_element)
            return popped_element
        # }

        else :
        # {
            raise Exception("Stack Underflow. The stack is empty.")
        # }

    # }

    # TODO: Implement a method to peek the top element of the stack
    # remember, you just have to look at the top element, not remove it

    def is_empty(self) :
    # {
        return len(self.stack) == 0
    # }

    def get_size(self) :
    # {
        return len(self.stack)
    # }

    def peek(self) :
    # {
        if (self.is_empty()) :
        # {
            print("The stack is empty.")
        # }

        else :
        # {
            print("The top element of the stack is:", self.stack[-1])
        # }

    # }

# }

my_stack = Stack()

for i in range(1, 7) :
# {
    my_stack.push(i)
# }

# TODO: Call the peek function to view the top element of the stack
print() # for spacing
print("Operations after attempting to pop the top element:")
my_stack.pop()

# TODO: Again, call the peek function to view the new top element of the stack
stack_size = my_stack.get_size()
print() # for spacing
print("Operations when attempting to pop all elements:")

for _ in range(stack_size) :
# {
    my_stack.pop()
# }

# TODO: Try to peek into an empty stack
my_stack.peek()

'''

***** BONEYARD *****

if (my_stack.is_empty()) :
# {
    print("The stack is empty.")
# }

else :
# {
    print("The stack is not empty.")
# }

'''