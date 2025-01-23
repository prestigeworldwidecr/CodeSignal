'''

Great work on your BFS tasks! You've excelled in traversing trees. However, let's delve a little deeper. Imagine that you're managing a company's team tree chart. Each node represents a staff member. Here, '1' is the CEO, with '2', '3', and '4' as managers, and the remainder are team members.

Your goal is to follow the chain of command from the top down, starting with the CEO. However, the current code isn't producing the correct output. Can you identify and correct the problem?

'''

from collections import deque

# Define BFS function
def BFS(graph, root) :
# {
    visited = [] # List to keep track of visited nodes
    queue = deque() # A queue to add nodes for visiting
    queue.append(root) # Start with the root node

    while (queue) : # While there are nodes to visit.
    # {
        vertex = queue.popleft() # Visit the first node in the queue
        print(vertex, "has been visited")
        visited.append(vertex) # Add it to the visited nodes list

        # Now add all unvisited children to the queue
        for child in graph[vertex] :
        # {
            if (child in visited) :
            # {
                None
            # }

            else :
            # {
                # visited.append(child)
                queue.append(child)
            # }

        # }

    # }

    return visited

# }

# Define the adjacency list of our graph
graph = {
        '1': ['2', '3', '4'],
        '2': ['1', '5', '6'],
        '3': ['1', '7', '8'],
        '4': ['1', '9', '10'],
        '5': ['2'],
        '6': ['2', '11'],
        '7': ['3'],
        '8': ['3'],
        '9': ['4'],
        '10': ['4'],
        '11': ['6']
    }

# Call the BFS function
print(BFS(graph, '1'))

'''

***** BONEYARD*****

'''