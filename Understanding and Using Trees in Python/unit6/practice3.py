'''

errific progress, brave coder! Let's reinforce your understanding of Binary Search Trees (BST) by crafting and traversing one.

Given the numerical sequence [50, 20, 70, 10, 30, 60, 80], can you construct a BST and then search values in it? This operation is commonplace when striving to maintain ordered lists efficiently; you'll find yourself utilizing it quite often.

'''

class Node :
# {
    def __init__(self, val) :
    # {
        self.left = None
        self.right = None
        self.val = val
    # }

    def __str__(self) :
    # {
        # return f'Node({self.val})'
        return self.val
    # }

# }

def insert_BST(root, node) :
# {
    # TODO: Insert a node into the BST
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

def search_BST(root, value) : 
# {
    # TODO: Perform the search for value in the BST
    if (root is None or root.val == value) : 
    # {
        None
    # }

    else :
    # {
        return root.val
    # }
    
    if (root.val < value) : 
    # {
        return search_BST(root.right, value) 
    # }

    else :
    # {
        # None
        return search_BST(root.left, value)
    # }
    
    # return search_BST(root.left, value)
# }
        
r = Node(50)
insert_BST(r, Node(20))
insert_BST(r, Node(70))
insert_BST(r, Node(10))
insert_BST(r, Node(30))
insert_BST(r, Node(60))
insert_BST(r, Node(80))

print(search_BST(r, 70)) # returns Node(70)
print(search_BST(r, 30)) # returns Node(30)
print(search_BST(r, 80)) # returns Node(80)
print(search_BST(r, 40)) # returns None
print(search_BST(r, 50)) # returns Node(50)
print(search_BST(r, 90)) # returns None

'''

***** BONEYARD *****

'''