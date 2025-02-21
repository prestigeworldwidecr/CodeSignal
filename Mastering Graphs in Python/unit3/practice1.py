'''

Are you ready to map out your journey through the States as a future graph whizz? Imagine that you are planning a road trip, starting from Washington, but unsure where to go next.

Why not use Depth-First Search (DFS) to plan the route?

This task challenges you to run a Python program that navigates a graph of inter-state connections using DFS. Understanding the output of this program will give you a tangible understanding of DFS!

'''

graph = {
            "Washington": set(["California", "Nevada"]),
            "California": set(["Washington", "Oregon"]),
            "Nevada": set(["Washington", "Oregon"]),
            "Oregon": set(["California", "Nevada"])
        }

def DFS(graph, start, visited) :
# {
    if (start in visited) :  # if the node has already been visited, just return the visited set
    # {
        return
    # }

    else :
    # {
    
        visited.add(start)
        print(start, end=" ")

        for state in graph[start] :
        # {
            if (state in visited) :
            # {
                None
            # }

            else :
            # {
                DFS(graph, state, visited)
            # }

    # }

# }

# Call the DFS function starting with 'Washington'
visited = set()
DFS(graph, "Washington", visited)  # Output: Washington Nevada Oregon California
print("\nVisited states:", visited)  # Print all visited states

'''

***** BONEYARD *****

'''