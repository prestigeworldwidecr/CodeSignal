'''

Strap in, astronaut; it's time for an exciting challenge. Imagine you are given two queues of integers such as queue1 = [1, 2, 3, 4, 5] and queue2 = [6, 7, 8, 9, 10]. Your task is to create a new queue that interleaves these two input queues. When you're done, your new queue should look like this: [1, 6, 2, 7, 3, 8, 4, 9, 5, 10].

Consider the following points while creating your solutions:

You should not modify the original queues; instead, create a new one.
Both queues are guaranteed to be filled with at least one element, and they will always be of the same size.
Edge case alert! What happens when the queues only have one element, or they are very large? Make sure your solution takes care of these scenarios as well. Good luck!

'''

from collections import deque

def interleave_queues(queue1, queue2) :
# {
    m = max(len(queue1), len(queue2))
    interleave_queue = deque()
    
    # implement this
    for i in range(m) :
    # {
        if (queue1) :
        # {
            interleave_queue.append(queue1.popleft())
        # }

        else :
        # {
            None
        # }

        if (queue2) :
        # {
            interleave_queue.append(queue2.popleft())
        # }

        else :
        # {
            None
        # }

    # }
        
    return list(interleave_queue)
# }

# Test cases
print(interleave_queues(deque([1, 2, 3, 4, 5]), deque([6, 7, 8, 9, 10]))) 
# Expected output: [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]
print(interleave_queues(deque([1]), deque([2])))
# Expected output: [1, 2]
print(interleave_queues(deque([1, 3, 5]), deque([2, 4, 6]))) 
# Expected output: [1, 2, 3, 4, 5, 6]

'''

***** BONEYARD *****

# print('!', max(len(queue1), len(queue2)))

if (len(queue1) == m) :
        # {
            interleave_queue.append(queue1.popleft())

            if (len(queue2) >= i) :
            # {
                interleave_queue.append(queue2.popleft())
            # }

            else :
            # {
                None
            # }

        # }

        else :
        # {
            # interleave_queue.append(queue1.popleft())

            if (len(queue1) >= i) :
            # {
                interleave_queue.append(queue1.popleft())
            # }

            else :
            # {
                None
            # }

            interleave_queue.append(queue2.popleft())

        # }

'''