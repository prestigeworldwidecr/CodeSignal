'''

Ready to dive into Python MinHeap operations, space explorer?

Imagine you are on a mission to a faraway galaxy. You are observing a sequence of license numbers from the spacecraft passing by your spaceship. You need a quick and efficient way to keep track of these spacecraft using their license numbers and to remove the spacecraft with the smallest license number once it is out of your radar.

To make sense of this situation, you have created a MinHeap, inserted nodes into it, and removed the smallest node.

'''

# Import necessary libraries
import heapq

# Create an empty MinHeap
minHeap = []

# Function to insert nodes maintaining the heap property
def insertNode(node_list):
# {
    for node in node_list:
    # {
        heapq.heappush(minHeap, node)
    # }

# }

# Function to delete node from heap
def deleteNode() :
# {
    try :
    # {
        return heapq.heappop(minHeap)
    # }
    
    except :
    # {
        return None
    # }

# }

# insert nodes into the MinHeap
insertNode([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# print MinHeap after insertions
print("Heap after insertions: ", minHeap)

# Delete a node from MinHeap
deleteNode()

# print MinHeap after deletion
print("Heap after deleting the minimum node: ", minHeap)

'''

***** BONEYARD *****

'''