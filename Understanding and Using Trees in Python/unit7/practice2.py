'''

Alright, Space Wanderer! Let's keep the learning train moving. Or should I say, rocket? Let's dig into Binary Search Trees (BSTs) again. Your mission is to seek out the k-th largest element in a BST. Bet you wonder what that means, eh? Well, let's say if k is 1, you're looking for the grandest, the maximum element. If k is 2, you seek the one right below it, and so on.

Imagine you're searching for life forms on planets, and k is their rank. Sounds fun, right? But remember, these aren't just any ol' trees, they're BSTs - each node's left child is smaller, and the right child is larger.

Your inputs are a root node reference of your BST and an integer k. Be on the lookout for edge cases, like an empty tree or when k is larger than the tree's size. As for your outputs, you should return the kth largest element's value.

'''

class Node :
# {
    def __init__(self, val, left=None, right=None) :
    # {
        self.val = val
        self.left = left
        self.right = right
    # }

# }

def kth_largest(root, k, tree) :
# {
    if (root and k > len(tree)) :
    # {
        tree.append(root.val)
    # }

    elif (len(tree) == k) :
    # {
        print('!@', tree[k - 1])
        return tree[k - 1]
    # }

    else :
    # {
        None
    # }

    if (root.right) :
    # {
        kth_largest(root.right, k, tree)  # Traverse the right subtree
    # }

    else :
    # {
        None
    # }

    if (root.left) :
    # {
        kth_largest(root.left, k, tree)   # Traverse the left subtree
    # }

    else :
    # {
        None
    # }

# }

# Creating the BST
root = Node(50) 
root.left = Node(20)
root.right = Node(60) 
root.left.left = Node(10) 
root.left.right = Node(30)
root.right.left = Node(55)
root.right.right = Node(70)
root.left.right.left = Node(25)
root.left.right.right = Node(35)
root.right.right.left = Node(65)
root.right.right.right = Node(80)

print(kth_largest(root, 5, []))  # Expected output: 55

# print(kth_largest(root, 10))  # Expected output: 20
# print(kth_largest(root, 3))  # Expected output: 65
# print(kth_largest(root, 7))  # Expected output: 35
# print(kth_largest(root, 2))  # Expected output: 70

'''

***** BONEYARD *****

# print(root.val)  # Process the current node (root)
        # print(root.val, tree, len(tree), k)
        # return tree[k - 1]
        # print('!', tree, len(tree), k)

# Now, let's test the function with the new binary tree
# print(kth_largest(root, 1))  # Expected output: 80

# tree = right_root_left_traversal(root)
# print(tree)

        if (root.right) :
        # {
            # print("crap")
            count = count + 1
        # }

        else :
        # {
            # count = count + 1
            print("poop")
        # }


# print('!', tree)
        # tree.append(root.val)
        

 """
    Performs a right-root-left traversal of a binary search tree (BST).

    Args:
        root: The root node of the BST.
    """

def kth_largest_in_bst(root, k) :
# {
    """
    Finds the k-th largest element in a Binary Search Tree (BST).

    Args:
        root: The root of the BST.
        k: The desired rank (k-th largest).

    Returns:
        The k-th largest element, or None if k is invalid or the tree is empty.
    """

    # if not root or k <= 0:  # Handle invalid input
    #    return None

    if (root or k >= 0) :
    # {
        # count = 0
        # print('!', k, root)

        return reverse_inorder(root, k, 0)
    # }

    else :
    # {
        return None
    # }

    # count = [0]  # Use a list to make count mutable in the recursive function

    # return reverse_inorder(root)

# }

def reverse_inorder(node, k, count) :
# {
    print('!', node.val, k, count)
    
    if (node) :
    # {
        right_result = reverse_inorder(node.right, k, count)

        if (right_result) : # Found in right subtree
        # {
            return right_result
        # }

        # count[0] += 1
        count = count + 1

        if (count == k) :
        # {
            return node.val
        # }

        else :
        # {
            None
        # }

        left_result = reverse_inorder(node.left, k, count)

        return left_result
    # }
    
    else :
    # {
        return count
    # }

# }

def kth_largest_in_bst(root, k):
    """
    Finds the k-th largest element in a Binary Search Tree (BST).

    Args:
        root: The root of the BST.
        k: The desired rank (k-th largest).

    Returns:
        The k-th largest element, or None if k is invalid or the tree is empty.
    """

    if not root or k <= 0:  # Handle invalid input
        return None

    count = [0]  # Use a list to make count mutable in the recursive function

    def reverse_inorder(node):
        if not node:
            return None

        right_result = reverse_inorder(node.right)
        if right_result is not None:  # Found in right subtree
            return right_result

        count[0] += 1
        if count[0] == k:
            return node.data

        left_result = reverse_inorder(node.left)
        return left_result

    return reverse_inorder(root)

def countNodes(root) :
# {    
    if (root) :
    # {
        return 1 + countNodes(root.right) + countNodes(root.left)
    # }
    
    else :
    # {
        return 0
    # }

# }

def kthLargest(root, k) :    
# {
    print(root.val, k)
    
    if (root) :
    # {
        right_nodes = countNodes(root.right)
    # }

    else :
    # {
        right_nodes = 0
    # }

    if (k == right_nodes + 1) :
    # {
        return root.val
    # }
    
    elif (k <= right_nodes) :
    # {
        return kthLargest(root.right, k)
    # }
    
    else :
    # {
        return kthLargest(root.right, k - 1 - right_nodes) 
    # }

# }

    # implement this
    # The number of nodes in the right subtree of the root
    
    # print(root.val, k, right_nodes)
    
    # If k is equal to the number of nodes in the right subtree plus 1, 
    # That means we must return the root's value as we've reached the k-th smallest

def right_root_left_traversal(root) :
# {
    """
    Performs a right-root-left traversal of a binary search tree (BST).

    Args:
        root: The root node of the BST.
    """
    if root is None:
        return

    right_root_left_traversal(root.right)  # Traverse the right subtree
    print(root.data, end=" ")  # Process the current node (root)
    right_root_left_traversal(root.left)   # Traverse the left subtree
# }

    # return 1 + countNodes(root.left) + countNodes(root.right)
    # return 1 + countNodes(root.right) + countNodes(root.left)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def right_root_left_traversal(root):
    """
    Performs a right-root-left traversal of a binary search tree (BST).

    Args:
        root: The root node of the BST.
    """
    if root is None:
        return

    right_root_left_traversal(root.right)  # Traverse the right subtree
    print(root.data, end=" ")  # Process the current node (root)
    right_root_left_traversal(root.left)   # Traverse the left subtree


# Example usage:
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print("Right-Root-Left Traversal:")
right_root_left_traversal(root)  # Output: 7 6 5 4 3 2 1
print()


# If there are more than k nodes in the right subtree,
    # The k-th smallest must be in the left subtree.

# If there are less than k nodes in the right subtree,
    # The k-th smallest must be in the right subtree.

# left_nodes = countNodes(root.left) if root else 0
        # left_nodes = countNodes(root.left)

'''