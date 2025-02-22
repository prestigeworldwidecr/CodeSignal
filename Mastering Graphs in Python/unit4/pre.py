'''

Hello and welcome to the next lesson of our course, "Solving Algorithmic Problems with DFS." In previous lessons, we introduced Graphs and their representations, venturing into one of the most predominant procedures in Graph theory — Depth-First Search. Today, we'll learn how to use Depth-First Search to solve a common problem: determining if there is a cycle in the graph.

Detecting cycles in a graph is a common problem that has applications in various domains. It is particularly useful in network routing, deadlock detection in operating systems, and in mathematical problems such as finding the presence of loops in a mathematical sequence.

In a graph, a cycle exists if we can start at a node, traverse along the edges, and return to the same node without retracing any edge. Our task is to construct a DFS function has_cycle(graph), which will check for a cycle in the given graph and return true if a cycle is found and false if the graph is acyclic.

Graphs can be represented in multiple ways, but for this lesson, we will use adjacency list representation for simplicity and efficiency.

We traverse the graph starting from an initial node, and for every visited node, we check if it is being revisited during the DFS exploration. If it is, then a cycle has been detected. Hence, we return true. If no cycle is found after exploring all the nodes, we return false. This approach has a linear time complexity of 
O
(
V
+
E
)
O(V+E), where 
V
V is the number of vertices (nodes) and 
E
E is the number of edges in the graph.

Note: to avoid finding degenerate cycles (A -> B -> A), we will provide a parent vertex (the vertex we came from) to the dfs function on top of the current vertex we are at. This way, when reaching the next vertex from the current one, we first check if we're trying to reach the parent. If yes - we skip this edge, if not, and the vertex is already visited - we indeed found the cycle.

The solution to this problem requires, first and foremost, implementing the DFS function. In this function, we mark the current node as visited and then check for each adjacent node. If the adjacent node is visited and it is not the parent of the current node, we find a cycle and return true. If the adjacent node is not visited, we recursively call the DFS function for that node.

Here is the modified dfs function for this task:

The function adds the current vertex to visited nodes. It then explores neighbors of vertex. If the neighbor was not visited before, the function recursively visits the neighbor, specifying vertex as its parent. If the neighbor is already in the visited and it is not the parent of the current vertex, it means that a cycle has been found, and it returns True. If all the neighbor nodes are explored without finding a cycle, it returns False (indicating no cycle found from the vertex).

Then, we introduce a has_cycle function to wrap the dfs function call:

Note that in case the graph is connected, it is enough to call the DFS function from any node just once. Do you have an idea how the above code should be changed to handle graphs consisting of more than one connected component?

'''

def dfs(vertex, visited, graph, parent) :
# {
    visited.add(vertex)

    for neighbor in graph[vertex] : 
    # {
        if (neighbor in visited) : 
        # {
            None
        # }
            
        elif (neighbor != parent) :
        # {
            # The parent is already visited, but the parent -> vertex -> parent cycle is degenerate
            return True
        # }
        
        else :
        # {
            if dfs(neighbor, visited, graph, vertex) : 
            # {
                return True
            # }

            else :
            # {
                None
            # }

        # }
        
    return False

# }

def has_cycle_connected(graph) :
# {
    visited = set()

    # Starting DFS from the first vertex in the graph
    return dfs(next(iter(graph)), visited, graph, None)
# }

def has_cycle_connected(graph):
# {
    visited = set()

    # Starting DFS from the first vertex in the graph
    return dfs(next(iter(graph)), visited, graph, None)
# }

def dfs(vertex, visited, stack, graph, parent):
# {
    visited.add(vertex)

    for neighbor in graph[vertex]:
    # {
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

    return False

# }

graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B'],
        }
print(has_cycle_connected(graph))
# Output: True

'''

***** BONEYARD *****

'''