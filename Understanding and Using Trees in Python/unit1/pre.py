'''

Welcome, Explorer! Today, we will delve deeper into the fascinating world of tree-based data structures. Building upon our comprehensive understanding of these structures, we're ready to enhance our knowledge further. Today's lesson focuses on Binary and Non-Binary Trees: their basic structure, implementation, complexity analyses, and the core operations performed on them.

As a reminder, tree data structures possess an impressive versatility that allows them to tackle many complex problems. For instance, managing hierarchies of employees in a large organization or efficiently storing words in a spell-checking system — these real-world scenarios naturally form tree-like structures!

Starting with a brief overview, a tree in computer science is a non-linear data structure representing a hierarchical and connected arrangement of entities known as nodes. A binary tree is a specific type of tree data structure where each node has, at most, two children: one left child and one right child.

On the other hand, a non-binary tree, also known as a multi-way tree, can have more than two children per node.

Before we jump into tree implementation, let's familiarize ourselves with key concepts and facts about tree data structures essential for beginners learning about trees.

Terminology:

Root: The topmost node in a tree.
Edge: The connection between one node to another.
Leaf: A node that doesn't have any children.
Depth of a Node: The number of edges from the node to the tree's root node.
Height of a Tree: The maximal depth of the tree nodes.
Subtree: Any node and its descendants form a subtree of the original tree.
Tree properties:

Path: A sequence of nodes and edges connecting a node with a descendant.
Acyclic: Trees cannot have cycles, which are paths where the start and end points are the same.
Connected: All nodes in a tree are connected by paths.
E
=
V
−
1
E=V−1: For any tree, the number of edges (
E
E) is always one less than the number of vertices (
V
V), illustrating the tree's connectivity without cycles.

Now that we've refreshed our understanding of what binary and non-binary trees are let's illustrate how to implement them using Python. In Python, tree structures can be constructed using class-based representations. A class is essentially a blueprint for creating objects. Objects have member variables and exhibit behaviors associated with them.

Consider the binary tree. Below is the Node class, representing a single node in a binary tree. Each Node object can hold a value and has two pointers, left and right, initially set to None.

For a non-binary tree, we can use a list to hold the links to the child nodes since their number isn't fixed.

We can create individual nodes, link them as children or parents, and construct our desired trees.

In order to gain a practical understanding of the concepts presented so far, let's take a look at some examples of binary and non-binary trees along with their traversals.

For our binary tree, let's use a simple structure with three levels of vertices.

Trees are dynamic data structures permitting several operations, such as insertion (adding a new node), deletion (removing an existing node), and traversal (accessing or visiting all nodes in a specific order).

Traversal of the binary tree is a process of visiting all nodes of a tree and possibly printing their values. Since all nodes are connected via edges (links), we always start from the root (head) node. We cannot randomly access a node in a tree. There are three ways to traverse a tree:

In-order Traversal: In this method, the left subtree is visited first, then the root, and later the right subtree. We should always remember that every node may represent a subtree itself.
Pre-order Traversal: In this method, the root node is visited first, then the left subtree, and finally the right subtree.
Post-order Traversal: In this method, the root node is visited last, hence the name. We first traverse the left subtree, then the right subtree, and finally, the root node.

Usually, information is inserted into a tree as a node. In a binary tree, a new node is inserted as the left or the right child of an existing node. An algorithm for inserting a node can be established by identifying an appropriate location for the new node. Deleting a node from a tree structure requires identifying the node, studying its properties, and subsequently transforming the tree structure.

In these examples, the add_child and remove_child methods enable us to add a node and remove a node in the tree, respectively.

For binary trees, the worst-case time complexity for searching, insertion, or deletion is 
O
(
n
)
O(n), where 
n
n is the number of nodes. This complexity arises because, in the worst case, you might have to traverse all nodes. However, in ideal circumstances (where the tree is perfectly balanced), operations on binary trees run in 
O
(
log
⁡
n
)
O(logn) time.

Comparatively, for non-binary trees, searching for or deleting a node can still be 
O
(
n
)
O(n), but insertion may be more efficient — 
O
(
1
)
O(1) — if we keep track of where the next insertion should happen; if we don't, the complexity is the same as in binary tree.



'''

class Node :
# {
    def __init__(self, value) :
    # {
        self.value = value
        self.left = None
        self.right = None
    # }

# }

class Node :
# {
    def __init__(self, value) :
    # {
        self.value = value
        self.children = []
    # }

# }

# Creating nodes for the tree.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# Creating nodes for the tree.
root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[2].children = [Node(7)]

def in_order_traversal(node):
# {
    if (node is None):
    # {
        return None
    # }
    
    else :
    # {
        in_order_traversal(node.left)
        print(str(node.value) + ' -> ', end='')
        in_order_traversal(node.right)
    # }

# }

in_order_traversal(root)
# Output: 4 -> 2 -> 5 -> 1 -> 3 -> 6 ->

class TreeNode :
# {
    def __init__(self, value):
    # {
        self.value = value
        self.children = []
    # }

    def add_child(self, child_node):
    # {
        self.children.append(child_node)
    # }

    def remove_child(self, child_node):
    # {
        # self.children = [child for child in self.children if child is not child_node]
        for child in self.children :
        # {
            if (child is not child_node) :
            # {
                self.children = child
            # }

            else :
            # {
                None
            # }
            
        # }

    # }

# }

'''

***** BONEYARD *****

'''