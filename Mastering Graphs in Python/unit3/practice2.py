"""

Great job on running your first DFS traversal! Now, let"s delve further into the cave.

The provided starter code traverses a social networking graph starting at "Alice". However, what if we were to begin the traversal from another node, say "Bob"? Could you adjust the code to initiate the DFS from "Bob"? Implementing this change might result in a new traversal order.

"""

# Define a graph using dictionary
graph = {
            "Alice": set(["Carol", "David"]),
            "Bob": set(["Alice", "Eve"]),
            "Carol": set(["Alice", "Eve"]),
            "David": set(["Alice"]),
            "Eve": set(["Bob","Carol"]),
        }

def DFS(graph, start_node, visited) :
# {
    """
    Function to implement DFS for the graph.
    """
    if (start_node in visited) :
    # {
        return
    # }
    
    else :
    # {
        visited.add(start_node)
        print(start_node, end=" --> ")

        for neighbour in graph[start_node] :
        # {
            if (neighbour in visited) :
            # {
                None
            # }

            else :
            # {
                DFS(graph, neighbour, visited)
            # }

        # }

    # }

# }


visited = set()
# Call our DFS function, starting with "Alice"
DFS(graph, "Bob", visited)  # Depicts the DFS traversal. It could vary basis the order in which neighbors are processed.
print("\nVisited nodes:", visited)

"""

***** BONEYARD *****

"""