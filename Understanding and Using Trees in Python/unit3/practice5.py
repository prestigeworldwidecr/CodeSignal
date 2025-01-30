'''

Well done, space explorer! You're right at the finish line! It's time to conclude our BFS practice with a final task!

Can you independently implement a Python function for Breadth-First Search (BFS)? You will be given an adjacency list representation of a graph and a root node. Your BFS function should return a list of nodes in the order they were visited.

Please follow the steps outlined in the TODO comments of the starter code and apply the knowledge you acquired from this lesson. Remember, you are the commander of this mission, so let's take it to a successful conclusion!

'''

from collections import deque

def BFS(tree, root):
# {
    # TODO: implement BFS for the given tree, starting at node `root`
    visited = []
    queue = deque()
    queue.append(root)

    while (queue) :
    # {
        vertex = queue.popleft()
        visited.append(vertex)

        # TODO: set the current level of vertex ** totally misguided
        
        for child in tree[vertex] :
        # {
            if (child in visited) :
            # {
                None
            # }

            else :
            # {
                queue.append(child)
            # }

        # }

    # }

    print("\nTraversing completed!")

    # TODO: return the list of tree nodes in the order they were visited
    return visited
# }

tree = {
        "computer" : ["printer", "router"],
        "printer" : ["paper", "computer"],
        "router" : ["internet", "computer"],
        "internet" : ["data", "router"],
        "paper" : ["printer"],
        "data" : ["internet"],
        }

print(BFS(tree, "printer")) # Change "computer" to starting node of your choice

'''

***** BONEYARD *****


                # TODO: set the level of the child ** child is vertex
                # level[child] = level[vertex] + 1
                # level.update({child : level_of_vertex})

'''