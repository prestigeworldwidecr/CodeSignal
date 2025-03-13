'''

You're doing great, Space Adventurer! Let's continue exploring the universe of algorithms. We've just completed a BFS traversal starting from Node 'A'. However, the universe may appear differently from other perspectives.

For instance, what would occur if we initiated our BFS traversal from Node 'B'? What kind of observation and differences can see see after changing the starting vertex?

Now it's time for you to tweak the code and witness this different perspective slightly. Prepare for launch!

'''

# Import the necessary libraries
from collections import deque

def BFS_Traversal(graph, start) :
# {
    visited = set() 
    queue = deque([start])

    while (queue) :
    # {
        vertex = queue.popleft()

        for neighbor in graph[vertex] :
        # {

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

graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }

print(BFS_Traversal(graph, 'B')) # {'B', 'C', 'F', 'A', 'E', 'D'}

'''

***** BONEYARD *****

'''