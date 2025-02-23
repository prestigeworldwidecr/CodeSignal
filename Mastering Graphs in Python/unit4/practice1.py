'''

Alright, Space Voyager! Think of an undirected graph, like a cosmic web of stars and galactic highways. Imagine you're a space entity trying to find closed circuits, or cycles, from a star back to itself without retracing any pathway.

Your mission is to create a function has_cycles(graph) that checks if there are any cycles in the graph. But here is the catch: not all the stars are connected with others with space routes, and there is a possibility that the given graph is disconnected. It basically means that there could be two or more vertices that have no path from one to another at all!

Modify the cycle-detecting algorithm to handle such cases.

'''

def has_cycle(graph):
# {
    visited = set()

    # implement this
    # return False
    return dfs(next(iter(graph)), visited, graph, None)
# }

def dfs(vertex, visited, graph, parent):
# {
    visited.add(vertex)

    for neighbor in graph[vertex]:
    # {
        # implement this
        if (neighbor in visited):
        # {
            None
        # }
            
        elif (neighbor != parent) :
        # {
            return True
        # }
        
        else :
        # {
            if dfs(neighbor, visited, graph, vertex):
            # {
                return True   
            # }

            else :
            # {
                None
            # }

        # }
        
    # }

    return False

# }

# Test the function
graph = {
            'A': ['B', 'C'],
            'B': ['A'],
            'C': ['A', 'D'],
            'D': ['C'],
            'E': ['G', 'K'],
            'K': ['G', 'E'],
            'G': ['K', 'E']
        }

print(has_cycle(graph))

'''

***** BONEYARD *****

'''