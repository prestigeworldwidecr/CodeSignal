'''

Well done, space explorer! You have conquered the vast expanse of Binary Search Trees (BST). Now, it's time for us to delve even deeper!

Imagine that you have been assigned a task to manage a list of interplanetary ships along with their respective speeds. The list is dynamic, with new ships being constructed and old ones being retired. Consequently, you thought that a BST would be the perfect solution. However, something seems to be amiss, and the list isn't displaying the correct details.

'''

class TreeNode :
# {
    def __init__(self, val) :
    # {
        self.left = None
        self.right = None
        self.val = val
    # }

# }

def bst_insert(root, node):
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
            bst_insert(root.right, node)
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
            bst_insert(root.left, node)
        # }

        else :
        # {
            root.left = node
        # }

    # }

# }

def bst_traversal_inorder(root) :
# {
    if (root) :
    # {
        bst_traversal_inorder(root.left)
        print(root.val)
        bst_traversal_inorder(root.right)
    # }

    else :
    # {
        None
    # }

# }

r = TreeNode(50)
bst_insert(r, TreeNode(30))
bst_insert(r, TreeNode(20))
bst_insert(r, TreeNode(40))
bst_insert(r, TreeNode(70))
bst_insert(r, TreeNode(60))
bst_insert(r, TreeNode(80))

bst_traversal_inorder(r)

'''

***** BONEYARD *****

# print('!', root.val)
    
    if (root is None):
    # {
        print('!', root, node.val)
        # root = node
        return TreeNode(node) 
    # }

    else : 
    # {
        # print('!', root.val, node.val, type(root.val), type(node.val))
        print('@', root.val)
        
        if (root.val < node.val) :
        # {
            root.right = bst_insert(root.right, node) 
            # return root.right
        # }

        else : 
        # {
            root.left = bst_insert(root.left, node) 
            # return root.left
        # }

    # }

    return root

# print('!')

elif (root.val < node.val) :
    # {
        # if root.right is None:
        if (root.right) :
        # {
            bst_insert(root.right, node)
        # }

        else :
        # { 
            root.right = None
        # }

    # }

    else :
    # {
        # if root.left is None:
        if (root.left) :
        # {
            bst_insert(root.left, node)
        # }

        else:
        # {
            root.left = None
        # }

    # }
    

'''