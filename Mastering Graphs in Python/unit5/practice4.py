'''

Great job navigating the vast galaxies of algorithms, Voyager! Now, let's dive deeper and apply our BFS knowledge to unravel the mysteries of a new graph.

Your task is to complete the Breadth-First Search (BFS) traversal function. This function should start the traversal from a specific node and cover all other nodes that are reachable from the start node in the given graph.

Can you fill in the missing pieces of code to initiate BFS traversal from node C?

'''

from collections import deque

def BFS(graph, start):
# {
    visited = set()
    queue = deque([start])  # ___ # initialize BFS starting state

    traversal_history = []

    while (queue) :
    # {
        vertex = queue.popleft()
        traversal_history.append(vertex)

        # TODO: process vertex's neighbors
        for neighbor in graph[start] :  # Visit all the node's neighbors
        # {
            # queue.append(neighbor)  # Enqueue the neighbor

            if (neighbor in visited):
            # {
                None
            # }

            else :
            # {
                visited.add(neighbor) 
                queue.append(neighbor)
            # }

        # }

    # }
                
    return traversal_history

# }

graph = {
            'A': ['B', 'C', 'D'],
            'B': ['F', 'G'],
            'C': ['H', 'I'],
            'D': ['J'],
            'F': [],
            'G': ['K', 'L'],
            'H': [],
            'I': [],
            'J': [],
            'K': [],
            'L': ['M', 'N'],
            'M': [],
            'N': []
        }

print(BFS(graph, 'C'))

'''

***** BONEYARD *****

'''