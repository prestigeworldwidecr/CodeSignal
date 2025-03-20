'''

Aye, aye, Voyager! We're going to navigate a graph today. Imagine you're in a galaxy full of interstellar trade routes, and you want to find the shortest path from your home planet to every other planet. Your map is a graph where each planet is a node, and each route is an edge. It's a normal nice galaxy: connected, unweighted, and undirected. You can write your map as an adjacency list where each node is a planet, and its list is the neighboring planets you can reach.

Your task, should you choose to accept, is to navigate from your home planet to all the other planets in the shortest time (or, in graph speak, find the shortest path from the start node to every single node). You'll bring back a dictionary, where keys are the nodes and values are the shortest paths as lists of nodes visited.

The edge case? There are none! Every planet is reachable from every other planet, and it’s an undirected, unweighted, connected graph. Remember, no teleportation is allowed; you have to follow those paths!

'''

from collections import deque

def shortestPaths(n, graph, start):
# {
    queue = deque([[start]])
    visited = set([start])

    shortest_paths = {
                        start: [start]
                    }

    # implement this
    while (queue) :
    # {
        path = queue.popleft()
        node = path[-1]
        shortest_paths[start] = path

        if (node == None) :
        # {
            return shortest_paths
        # }

        else :
        # {
            None
        # }

        for neighbor in graph[node] :
        # {
            if (neighbor in visited) :
            # {
                None
            # }

            else :
            # {
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append(new_path)
                shortest_paths[neighbor] = new_path
            # }

        # }

    # }
    
    return shortest_paths
# }

# Test cases:

# We describe a simple graph with 3 nodes and 3 edges.
graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }

print(shortestPaths(3, graph, 1)) 
# Expected output: {1: [1], 2: [1, 2], 3: [1, 3]} 
# Explanation: The paths from node 1 to nodes 2 and 3 are direct edges. 

graph = {
            1: [2],
            2: [1, 3],
            3: [2]
        }

print(shortestPaths(3, graph, 1)) 
# Expected output: {1: [1], 2: [1, 2], 3: [1, 2, 3]} 
# Explanation: The path from node 1 to node 3 includes node 2, as there's no direct edge to node 3.

graph = {
            1: [2, 3, 4],
            2: [1, 3],
            3: [1, 2, 4], 
            4: [1, 3]
        }

print(shortestPaths(4, graph, 1)) 
# Expected output: {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 4]} 
# Explanation: There are direct edges from node 1 to all other nodes.

'''

***** BONEYARD *****



                
                
        
        # i = start
        # distance = queue.popleft()
        # start = path
        # shortest_paths[n] = path
        # n = i
                # n = n + 1
                # queue.append((distance + 1, new_path))
                # print(new_path)
                # n = n - 1
                # shortest_paths[n] = new_path
                # i = i + 1
                # shortest_paths[i] = new_path
                # print('!', n, new_path, i)
            # n = i

    # distance = queue.popleft()
    
    if (node == end) :
    # {
        # return distance, path
        return shortest_paths
    # }

    else :
    # {
        None
    # }

'''