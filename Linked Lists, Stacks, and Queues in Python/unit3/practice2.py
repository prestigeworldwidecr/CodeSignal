'''

Alright! Let's play with a stack now. You have to create a step-up version of it that not only allows you to add or remove elements but also find out the greatest element in there, all in no time. Let me lay it out for you:

Design a stack that supports the following operations:

push(x): like pushing a spaceship into a wormhole, this shoves an element x into your stack.
pop(): Ah, like popping a bubble, this pulls out the top element of the stack
top(): lets you sneak a peek at the top element without moving it anywhere.
get_max(): fetches the giant among all, the maximum element in the stack!
All of your inputs will be integers, including the naughty negative ones, and for edge cases, if the stack is empty when pop(), top(), or get_max() is called, just return -1. After everything’s done and dusted, you’ll deliver the space rock, I mean the result, also in pure integer form. Let's see you bend the rules of ordinary stacks!

'''

class MaxStack :
# {
    def __init__(self) :
    # {
        self.stack = []
        self.max_stack = []
    # }

    def push(self, x) :
    # {
        # implement this
        None
    # }
    
    def pop(self) :
    # {
        # implement this
        None
    # }

    def top(self) :
    # {
        # return self.stack[-1] if self.stack else None
        if (self.stack) :
        # {
            return self.stack[-1]
        # }

        else :
        # {
            return None
        # }

    # }

    def get_max(self) :
    # {
        # return self.max_stack[-1] if self.max_stack else None
        if (self.max_stack) :
        # {
            return self.max_stack[-1]
        # }

        else :
        # {
            return None
        # }
        
    # }

# }

# A few print statements to test the implementation
stack = MaxStack()
stack.push(5)
print(stack.get_max())  # Expected: 5
stack.push(1)
print(stack.get_max())  # Expected: 5
stack.push(6)
print(stack.get_max())  # Expected: 6
stack.pop()
print(stack.get_max())  # Expected: 5

'''

***** BONEYARD *****

'''