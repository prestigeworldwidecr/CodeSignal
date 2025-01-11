'''

Absolutely splendid, Astronaut! You're managing the catering order queue like a pro! Now, let's slightly alter our scenario.

There is a catering queue that holds meal orders. Implement the check in the while loop to process all the orders from the queue.

So, flex those fingers and let's start coding!

'''

from collections import deque

# Our queue is represented as a deque
catering_queue = deque()

print("Initial queue is empty:", catering_queue)

# We add some orders to the queue by using append method
catering_queue.append('Order1')
catering_queue.append('Order2')
catering_queue.append('Order3')
catering_queue.append('Order4')
catering_queue.append('Order5')
catering_queue.append('Order6')

print("Queue after enqueue operations:", catering_queue)


# We process orders one by one in order of their arrival by using popleft method
# while False :  # TODO: replace False with a proper check:
while (catering_queue) :
# {
    order = catering_queue.popleft()
    print("Processing:", order)
    print("Queue after processing", order, ":", catering_queue)
# }

'''

***** BONEYARD *****

'''