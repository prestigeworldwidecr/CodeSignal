'''

Welcome to our space lab, fellow astronaut!

Have you ever wondered how we, as humans, organize information? We use systems similar to those in a library – categorizing from small to big, distinguishing between fiction and non-fiction, arranging alphabetically, etc. In the sphere of digital data management, we utilize a particular tree-like structure known as a Binary Search Tree (BST). The purpose of this structure is to order data for efficient retrieval.

Consider it as a family tree - just for numbers! Today's mission isn't complicated – we've already completed the rigorous calculations. Your sole task is to press the Run button to observe the BST in action!

'''

class Node :
# {
    def __init__(self, val) :
    # {
        self.left = None
        self.right = None
        self.val = val
    # }

# }

def insert_BST(root, node) :
# {
    if (root) :
    # {
        None
    # }

    else :
    # {
        root = node
        return None
    # }
    
    if (root.val < node.val) :
    # {
        # if root.right is None :
        if (root.right) :
        # {
            insert_BST(root.right, node)
        # }

        else :
        # {
            root.right = node
        # }

    # }

    else :
    # {
        # if root.left is None :
        if (root.left) :
        # {
            insert_BST(root.left, node)
        # }

        else :
        # {
            root.left = node
        # }

    # }

# }

def in_order_traversal(root) :
# {
    if (root) :
    # {
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)
    # }

    else :
    # {
        None
    # }
    
# }
        
def delete_node_with_val(root, val) :
# {
    # if root is None :
    if (root) :
    # {
        None
    # }
    
    else :
    # {
        return root
    # }

    if (val < root.val) :
    # {
        root.left = delete_node_with_val(root.left, val)
    # }

    elif (val > root.val) :
    # {
        root.right = delete_node_with_val(root.right, val)
    # }

    else :
    # {
        if (root.left is None) :
        # {
            temp = root.right
            root = None
            return temp
        # }
        
        elif (root.right is None) :
        # {
            temp = root.left
            root = None
            return temp
        # }

        else :
        # {
            None
        # }
        
        temp = find_min_value_node(root.right)
        root.val = temp.val
        root.right = delete_node_with_val(root.right, temp.val)

    # }

    return root

# }

def find_min_value_node(node) :
# {
    current = node

    # while (current.left is not None) :
    while (current.left) :
    # {
        current = current.left
    # }

    return current

# }

# Driver Code:
root = Node(6)
insert_BST(root, Node(8))
insert_BST(root, Node(2))
insert_BST(root, Node(5))
insert_BST(root, Node(4))
insert_BST(root, Node(9))

print("In-order traversal:")
in_order_traversal(root)

print("In-order traversal after deleting:")
root = delete_node_with_val(root, 2)
in_order_traversal(root)

'''

***** BONEYARD *****

'''