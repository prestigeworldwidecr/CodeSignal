'''

Bravo, space explorer! You're making great progress. Now, imagine that you are the chief engineer at the space station. Your task is to manage the takeoff queue for spaceships, with the spaceship holding the largest license number initiating takeoff first.

However, a problem arises: the spaceship scheduled to be the first for takeoff is suddenly experiencing technical issues. Due to this unexpected setback, the team must now remove it from the queue and schedule the next one for takeoff.

The piece of code provided below is intended to handle this situation. However, it is not working as expected. Can you identify and correct the bug?

'''

# Import necessary libraries
import heapq

# Create an empty MaxHeap
maxHeap = []

# A function to insert nodes into the MaxHeap while maintaining the heap property
def insert(nodes) :
# {
    for node in nodes :
    # {
        heapq.heappush(maxHeap, -node)
    # }

    print("Max Heap after insertion:", maxHeap)
# }

# A function to delete the largest node from the MaxHeap
def delete() :
# {
    largest = heapq.heappop(maxHeap) * -1
    print("Max Heap after deletion of largest node:", maxHeap)
# }

# Spaceships identified by the last 2 digits of their license numbers
spaceships = [28, 14, 35, 55, 68, 72, 47, 19, 11, 32]

insert(spaceships)  # Add all spacecrafts to the queue

# print("Max Heap after insertion:", maxHeap)

delete() # Delete the spacecraft with the largest license number

'''

***** BONEYARD *****

# maxHeap.remove(max(maxHeap))

heapq.heapify(nodes)
    
    maxHeap.append(node)
    # heapq = maxHeap
    # maxHeap = heapq.heapify(nodes)

def insert(nodes) :
# {
    heapq.heapify(nodes)
    
    for node in heapq.nlargest(len(nodes), nodes):
    # {
        maxHeap.append(node)
    # }

    # heapq = maxHeap

    print("Max Heap after insertion:", maxHeap)
    # maxHeap = heapq.heapify(nodes)
# }

# A function to delete the largest node from the MaxHeap
def delete() :
# {
    # largest = heapq.heappop(maxHeap)
    maxHeap.remove(max(maxHeap))
    print("Max Heap after deletion of largest node:", maxHeap)
# }

'''