'''

Given a space map of planets (represented as nodes) and space routes (represented as edges between nodes), your task is to find a path to invite all your friends (across various planets), starting from Earth to your galactic party. The provided code is designed to use BFS traversal to execute this task, but it seems there is a bug impeding its proper operation.

'''

# Import necessary libraries
from collections import deque

def BFS(graph, start_node):
# {
    # Create an empty set for visited nodes and a queue for BFS
    visited = set()
    queue = deque([start_node])

    print("The BFS traversal, starting at node", start_node, "displays nodes in this order: ")

    # Loop until the queue is empty
    while (queue) :
    # {
        node = queue.popleft()  # Remove a node from the front of the queue
        print(node, end=" ")  # Print the visited node

        for neighbor in graph[node] :  # Visit all the node's neighbors
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

    return visited

# }

print()

# Graph representation as an adjacency list
graph = {
            "Earth": ["Mars", "Jupiter"], 
            "Mars": ["Neptune", "Pluto"],
            "Jupiter": ["Venus", "Saturn"], 
            "Neptune": [],
            "Pluto": [],
            "Venus": ["Uranus"],
            "Saturn": [],
            "Uranus": []
        }

# Initiate BFS traversal starting from "Earth"
BFS(graph, "Earth")

'''

***** BONEYARD *****

'''