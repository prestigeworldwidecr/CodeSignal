'''

Great job, Space Voyager! You've just seen how the Breadth-First Search algorithm operates on a graph representing a network of planets.

Now, let's suppose that the starting point for our BFS traversal isn't Mars but rather Saturn. A mischievous cosmic wind at play, perhaps? Could you modify the code for us so that we can correct our flight path and kickstart the BFS traversal from Saturn instead?

'''

from collections import deque

# Representing the tree as an adjacency list
graph = {
            "Mars" : ["Jupiter", "Saturn"],
            "Jupiter" : ["Mars", "Neptune", "Uranus"],
            "Saturn" : ["Mars", "Venus", "Mercury"],
            "Neptune" : ["Jupiter"],
            "Uranus" : ["Jupiter", "Earth"],
            "Venus" : ["Saturn"],
            "Mercury" : ["Saturn"],
            "Earth" : ["Uranus"]
        }

# BFS Function
def BFS(graph, root) :
# {
    visited = [] # List to keep track of visited nodes
    queue = deque()
    queue.append(root) # Start with the root node

    while (queue) : # While there are nodes to visit.
    # {
        vertex = queue.popleft() # Visit the first node in the queue
        print(vertex, "has been visited")
        visited.append(vertex) # Add it to the visited nodes list

        for neighbour in graph[vertex] : # Add all unvisited children to the queue
        # {
            if (neighbour in visited) :
            # {
                None
            # }

            else :
            # {
                queue.append(neighbour)
            # }

        # }

    # }

    return visited

# }

print("\nOrder of visited planets: ", BFS(graph, "Saturn")) # Start at Mars

'''

***** BONEYARD *****

'''