'''

Ahoy! You've found a treasure trove, Coding Pirate! Your quest takes you deeper into the secrets of the given tree. Now, you've been entrusted with adding a plum to our fruit tree.

But wait! You can't just drop it anywhere. It must be placed in its rightful position: directly under the pear. On top of that, the implementation of the print_tree is missing. We need to fill it in!

Can you code these additions?

Suggestions
Give me an example
Hint, please

'''

class TreeNode :
# {
    def __init__(self, value) :
    # {
        self.value = value
        self.children = []
    # }

    def add_child(self, child_node) :
    # {
        self.children.append(child_node)
    # }
    
    def remove_child(self, child_node) :
    # {
        # self.children = [child for child in self.children if child is not child_node]
        for child in self.children:
        # {
            if (child) :
            # {
                None
            # }

            else :
            # {
                self.childen = child
            # }

        # }

    # }      

# }

# Define the tree
tree_root = TreeNode("Apple")
root_left = TreeNode("Banana")
root_right = TreeNode("Cherry")
tree_root.add_child(root_left)
tree_root.add_child(root_right)

root_left.add_child(TreeNode("Date"))
root_left.add_child(TreeNode("Elderberry"))

root_right.add_child(TreeNode("Pear"))
root_right.add_child(TreeNode("Grape"))

# TODO: Add a plum under pear
root_right.children[0].add_child(TreeNode("Plum"))

def print_tree(node) :
# {
    # TODO: print the whole tree, first printing the root, and then all its children recursively

    print(str(node.value) + ' -> ', end='')

    for child in node.children :
    # {
        # return str(node.value) + ' -> ' + str(print_tree(child))
        print_tree(child)
    # }

# }  

print_tree(tree_root)

'''

# print('@', node.value, node.children[0].value, node.children[1].value, node.children[0].children[0].value, node.children[0].children[1].value, node.children[1].children[0].value, node.children[1].children[1].value, node.children[1].children[0].children[0].value)

# for child in node.value:
    
for i in range(len(node.children)) :
    # {
        # print(node[i].value)
        print(node.children[i].value)
    # }

        if (child) :
        # {
            print(child)
        # }

        else :
        # {
            # node.childen = child
            # print(child.value)
            None
        # }

for child in node.children :
    # {
        print(str(node.value) + ' -> ', end='')
        print_tree(child)
    # }
print('!')
    return node

        # self.left = None
        # self.right = None

***** BONEYARD *****

if (node) :
    # {
        print_tree(root_left)
        print(str(node.value) + ' -> ', end='')
        print_tree(root_right.children)
    # }
        
    else :
    # {
        return None
    # }

    def add_child(self, child_node) :
    # {
        self.children.append(child_node)
    # }

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Performs an inorder traversal of a binary tree and returns the values in a list.

    Args:
        root: The root node of the tree.

    Returns:
        A list containing the values of the nodes in inorder traversal. Returns an empty list if the root is None.
    """
    if not root:
        return []

    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result


def print_tree_inorder(root):
    """Prints the tree's values using inorder traversal."""
    inorder_values = inorder_traversal(root)
    print("Inorder Traversal:", inorder_values)

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print_tree_inorder(root)  # Output: Inorder Traversal: [4, 2, 5, 1, 3]

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)
print_tree_inorder(root2) # Output: Inorder Traversal: [3, 2, 1]

root3 = None # Empty Tree
print_tree_inorder(root3) # Output: Inorder Traversal: []

root4 = TreeNode(1)
root4.right = TreeNode(2)
root4.right.right = TreeNode(3)
print_tree_inorder(root4) # Output: Inorder Traversal: [1, 2, 3]

'''