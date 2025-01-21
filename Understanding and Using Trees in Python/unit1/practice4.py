'''

Great job, Voyager! There's only one obstacle left to conquer before we wrap up this lesson.

Now, your challenge is constructing some binary tree from scratch using Python. After that, print out the nodes of this binary tree using in-order traversal.

'''

# TODO: Define your Node class
class Node :
# {
    def __init__(self, value) :
    # {
        self.value = value
        self.children = []
        self.left = None
        self.right = None
    # }

# }

# TODO: Define a binary tree using your Node class
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

# TODO: Implement a function to perform in-order traversal
def in_order_traversal(node):
# {
    print(str(node.value) + ' -> ', end='')

    for child in node.children :
    # {
        # return str(node.value) + ' -> ' + str(print_tree(child))
        in_order_traversal(child)
    # }    

# }

# TODO: Print the nodes of the binary tree using the in-order traversal method
in_order_traversal(root)

'''

***** BONEYARD *****

if (node):
    # {
        in_order_traversal(node.left)
        print(str(node.value) + ' -> ', end='')
        in_order_traversal(node.right)
    # }
    
    else :
    # {
        return None
    # }

'''