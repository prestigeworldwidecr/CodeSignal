'''

Let's start with our first problem. Imagine you have a list of integers, and your task is to determine the preceding smaller value for every number on the list. If a smaller previous element does not exist, you have to return -1.

Problem 1: Problem Actualization

Now, let's give this problem some context for better understanding its real-world application. Imagine you are working in finance, analyzing historical stock prices. For each day, you would like to know the previous day when the price was lower than the current price. This situation is a perfect instance where our problem comes into play, and solving it would make your everyday job a lot easier.

Problem 1: Naive Approach

While approaching this problem, your initial heuristic might lead you down the path of comparing each number with all its previous numbers. While this method does offer a solution, it's not an efficient one. Would you guess it's time complexity? Exactly, it is 
O
(
N
2
)
O(N 
2
 )! As the scale increases, this approach generates a lot of unnecessary computations, rendering it inefficient for larger data sets.

 Instead of the naive, brute-force approach, a more elegant and efficient solution would involve the use of Stacks. A Stack would allow us to track only relevant numbers, discarding the ones that won't contribute to the solution. This ensures higher accuracy in our solutions and optimizes computational resources.

Now, you might be wondering, "Sure, this approach seems way more efficient, but why does it work? How can we just ignore certain numbers and trust that our stack is leading us to the correct answers?" Well, that's the beauty of this approach.

By popping out the numbers from the stack that are larger than or equal to the current number, we are notifying the process that these numbers can't possibly be the "previous smaller value" for any other number that follows in the list. Why? Because if there is a number smaller than these popped numbers, it would be smaller than our current number as well, and it would inevitably be positioned in between our current number and the popped numbers. As a result, our current number is closer to any forthcoming numbers, fulfilling the 'smaller' and 'most recent' criteria in our quest.

Our second problem requires us to design a stack with a special feature. This stack should be capable of performing all typical operations like pushing an element onto the stack, popping the top element from the stack, and fetching the top element. In addition, it should also support a special function get_min() that returns the smallest element in the stack — all within a time complexity of 
O
(
1
)
O(1).

Problem 2: Problem Actualization

To understand when this problem may come in handy, imagine you are dealing with a stack of papers, each assigned with a different numerical value, and you always need to have access to the paper with the smallest number. In such a scenario, how would you engineer your stack so that the smallest paper can be found instantly? Our get_min() function is the answer to this problem.

The initial heuristic might be to maintain a separate variable to keep track of the minimum element. However, this approach becomes problematic when the minimum element is removed from the stack, as it triggers additional overhead to update the new minimum.

We can solve this issue by maintaining a secondary stack that mirrors the main stack but tracks the minimum values in parallel. When an element is pushed onto the main stack, we check if it's less than or equal to the current top element of the secondary stack. If it is, we also push it onto our secondary stack. This ingenious method paves the way to query the minimum element with a get_min() function at a constant time complexity of 
O
(
1
)
O(1).

Starting from the ground up, we'll build our structure and the MinStack class to house all the method operations:

We'll first initialize two empty lists, stack and min_stack.

This stack stores the added elements, and min_stack holds the minimum values.

Next, we'll shape the push method, which pushes an element onto stack, and if this new element is smaller than or equal to the current smallest element (the top element of min_stack), it is also pushed onto our min_stack.

Our pop method is up next. It removes the top element from the stack, and if the smallest element is being removed, it also pops the corresponding element from the min_stack.



'''

# We start off by initializing an empty Stack and a result list with -1.
result = [-1]
stack = []

# This -1 in the result list serves as a placeholder for the first element, as it has no preceding elements.

# Next, we loop through our list of numbers. For every number, a while loop keeps popping items from the stack until we find a number smaller than the current one or until the stack is empty.

for num in numbers :
# {
    while (stack and stack[-1] >= num) :
    # {
        stack.pop()
    # }

# }

# At this point, if our stack is empty, it means there are no previous smaller elements, so we add -1 to the result list. If the stack is not empty, we add the top element of the stack (i.e., the previous smaller number) to our result list.

# result.append(stack[-1] if stack else -1)  

if (stack) :
# {
    result.append(stack[-1])
# }

else :
# {
    result.append(-1)
# }

stack.append(num)

# Finally, as the first element of the result list was just an initial placeholder and not part of our actual solution, we return the result list from the second element to the end.

## return result[1: : ]

def findSmallerPreceeding(numbers) :
# {    
    result = [-1]
    stack = []

    for num in numbers :
    # {
        while (stack and stack[-1] >= num) :
        # {
            stack.pop()
        # }

    # }

    if (stack) :
    # {
        result.append(stack[-1])
    # }

    else :
    # {
        result.append(-1)
    # }

    stack.append(num)

    return result[1: : ]

# }

class MinStack :
# {
    def __init__(self) :
    # {
        self.stack = []
        self.min_stack = []
    # }

    def push(self, x) :
    # {
        self.stack.append(x)

        if (self.min_stack or x <= self.min_stack[-1]) :
        # {
            None    # do nothing
        # }

        else :
        # {
            self.min_stack.append(x)
        # }

    # }

    def pop(self) :
    # {
        if (self.stack) :
        # {
            if (self.stack[-1] == self.min_stack[-1]) :
            # {
                self.min_stack.pop()
            # }

            else :
            # {
                None
            # }

            return self.stack.pop()
        # }

        else :
        # {
            return None
        # }

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

    def get_min(self) :
    # {
        # return self.min_stack[-1] if self.min_stack else None
        if (self.min_stack) :
        # {
            return self.min_stack[-1]
        # }

        else :
        # {
            return None
        # }
        
    # }

# }

'''

***** BONEYARD *****

while stack and stack[-1] >= num:
            stack.pop()
        result.append(stack[-1] if stack else -1)
        stack.append(num)

'''