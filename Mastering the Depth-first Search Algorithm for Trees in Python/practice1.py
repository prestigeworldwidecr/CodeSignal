'''

Great job absorbing the intricacies of Depth-first Search (DFS)! Now, let's see this algorithm in action in a way that you might encounter while managing a project hierarchy or exploring nested structures in real life.

Imagine we're examining a company's departmental structure, and you're presented with the organizational tree. Can you figure out how to navigate through the departments from the head office down to the different teams?

Right now, just hit the Run button to witness how the DFS algorithm traverses this hierarchy from the top to the bottom. Keep an eye on how it goes deep before going wide!

'''

class Node :
# {
    def __init__(self, value) :
    # {
        self.value = value
        self.children = []
    # }

# }

def add_edges(tree, node, child_values) :
# {
    for value in child_values :
    # {
        node.children.append(Node(value))
    # }

# }

def dfs(node, visited=None):
# {
    if (visited):
    # {
        None
    # }

    else :
    # {
        visited = set()
    # }
    
    visited.add(node.value)
    print(node.value, end=' -> ')

    for child in node.children:
    # {
        if (child.value in visited) :
        # {
            None
        # }

        else :
        # {
            dfs(child, visited)
        # }

    # }

# }

# Constructing a tree
root = Node('Head Office')
add_edges(root, root, ['Marketing', 'Sales', 'R&D'])

node_marketing = root.children[0]
add_edges(root, node_marketing, ['SEO', 'Content'])

node_sales = root.children[1]
add_edges(root, node_sales, ['Domestic', 'International'])

# Perform DFS traversal
print("DFS Traversal:")
dfs(root)
print("end")

'''

***** BONEYARD *****

'''