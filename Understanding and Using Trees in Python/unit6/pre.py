'''

Dear students, today's session is an exciting journey into the world of Binary Search Trees (BSTs)! Up until now, in our Understanding and Using Trees in Python course, you've gained extensive knowledge about a variety of tree structures, explored the Breadth-First Search (BFS) and Depth-First Search (DFS), and learned about Heaps in detail. Today, we're progressing to another fundamental subject that leverages the tree structure to optimize data storage and searching processes — the Binary Search Tree (BST).

In essence, Binary Search Trees are excellent data structures that optimize search operations by appropriately arranging data elements based on certain properties. These trees' "left-small, right-large" order property helps ensure fast search, insertion, and deletion operations. Essentially, BSTs are tree structures designed to make data retrieval and storage efficient and simpler.

The ultimate goal of today's lesson is three-fold. First, we will understand the intricate workings of BSTs; then, we will implement them in Python using the CodeSignal IDE, and finally, we'll apply this knowledge to solve complex algorithmic problems leveraging BSTs. So, without further ado, let's set out on this exciting exploration of BSTs!

Binary Search Trees (BSTs) are named for their binary nodal structure, where each node links to two child nodes — much like a binary tree. However, what differentiates them is a crucial property ingrained in them: every node ensures that the values in its left subtree are less than or equal to its value, and the values in its right subtree are greater than its value. This property facilitates highly efficient search operations.

Let's illuminate this concept with a simple instance. Take a look at the BST below - note that for every node, all elements in the left subtree are smaller than the node value, and all elements in the right subtree are larger than the node value.

Here, 5 sits at the root of the tree, its left subtree contains values 1, 3, and 4, all less than the root value 5, and the right subtree contains values 6 and 9, both larger than 5. The same condition holds for all other nodes in the tree. This simple example provides a clear insight into the underlying logic that governs the BST's node placement.

Now, let's venture into the practical implementation of a BST in Python. We begin by defining a Node class. Here, a Node represents a structure wherein each Node contains a reference point to its left and right children and holds some data — the node's value.

Now that we have a fundamental understanding of BSTs and how to create them in Python, let's introduce three of the essential BST operations: insertion, deletion, and searching.

Insertion: To maintain the key BST property during insertion, a new value x must be carefully positioned. We start at the root and traverse down the BST. If x is less than the current node's value, we go left; if it's greater, we move to the right child. We continue this movement until we find an appropriate spot devoid of a child node, where we place x in a new node at that location.

Searching will help us find if a value exists in the BST. We start at the root and traverse down the tree until we find the key. If the key's value is greater than a node's value, we move right, and if it's smaller, we move left. If we can't locate the key or the tree is empty, our function returns None, indicating that the key is not present in the BST.

Deletion: Deleting a node can be a bit tricky because you must maintain the BST property even after the deletion. A node can be deleted following these steps:

If the node is a leaf node, delete the node outright.
If the node has only one child: Replace the node with its subtree.
If the node has both children: Find its in-order successor (the smallest value in its right subtree) or its in-order predecessor (the largest value in its left subtree) and replace the node with that value. After replacing, delete the in-order successor or predecessor node.

Considering the time and space complexity associated with BST operations is essential, as it gives us a thorough understanding of the efficiency and scalability of these operations in real-world applications.

The performance of BST operations heavily depends on the height of the tree, which is the maximum number of levels in the tree. That's why binary search trees are considered efficient data structures, as they are designed to keep the height minimal.

Here's a breakdown of the time complexity for the key BST operations:

Insertion: The worst-case time complexity is 
O
(
h
)
O(h), where 
h
h is the height of the tree. Since we start from the root and continue to either the left or right child, depending on the node's value, the time complexity is proportional to the height of the tree. The best-case time complexity is 
O
(
log
⁡
n
)
O(logn) if the tree is a complete binary tree (height is 
log
⁡
n
logn in that case).

Searching: The time complexity for the search operation, similar to insertion, is 
O
(
h
)
O(h) in the worst case and 
O
(
log
⁡
n
)
O(logn) in the best case scenario.

Deletion: The worst-case time complexity for deletion is also 
O
(
h
)
O(h), considering we need to search for the node to be deleted first. In the best case, it takes 
O
(
log
⁡
n
)
O(logn) time as well.

The space complexity of all these operations is 
O
(
h
)
O(h) in worst-case conditions, as during the recursive operations (insertion, searching, or deletion), the auxiliary space required by the system stack is equivalent to the height of the tree. However, for a perfectly balanced Binary Search Tree, this would be 
O
(
log
⁡
n
)
O(logn).

It should be noted that BST operations' time complexity can degrade to 
O
(
n
)
O(n) in the worst-case scenario if the BST becomes skewed or unbalanced, meaning all nodes exist on a single side of the root, creating a linear-like structure. In practice, self-balancing BSTs are used to maintain an acceptable height, ensuring operations run in a relatively consistent 
O
(
log
⁡
n
)
O(logn) time - these trees balance themselves after every insertion or deletion operation to keep the height close to 
O
(
log
⁡
n
)
O(logn).

BSTs have a wide range of applications. They can be used to implement an ordered map — given that you traverse them in order, it directly provides the elements sorted according to their natural order. BSTs can also be used to implement sets that have large arithmetic progressions efficiently. Because BSTs ensure a level of optimization in terms of time complexity, they're preferred for many real-life scenarios and applications.

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

root = Node(5)
root.left = Node(3)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)

def insert(root, key) :
# {
    if root is None : 
    # {
        return Node(key) 
    # }
    
    else : 
    # {
        if (root.val < key) : 
        # {
            root.right = insert(root.right, key) 
        # }

        else : 
        # {
            root.left = insert(root.left, key) 
        # }

    # }

    return root

# }

def search(root, key) : 
# {
    if (root is None or root.val == key) : 
    # {
        # None
        return root.val
    # }

    else :
    # {
        return None
    # }
    
    if (root.val < key) : 
    # {
        return search(root.right, key) 
    # }

    else :
    # {
        None
    # }
    
    return search(root.left, key)

# }

def minValueNode(node) :
# {
    # This function finds the node with the smallest value in a BST
    current = node
    
    # The smallest value is located at the leftmost leaf.
    # Therefore, we iterate until the left child node is None
    # while (current.left is not None):
    while (current.left):
    # {
        current = current.left
    # }

    return current

# }

def deleteNode(root, key) :
# {
    # This function deletes the node containing the value key from the BST

    # If the root is None, then the tree is empty.
    # Therefore, we return the root
    if (root is None) :
    # {
        return root
    # }
    
    # The value key is less than the root's value, then it lies in the left subtree
    if (key < root.val) :
    # {
        root.left = deleteNode(root.left, key)
    # }

    # The value key is greater than the root's value, then it lies in the right subtree
    elif (key > root.val) :
    # {
        root.right = deleteNode(root.right, key)
    # }

    else :
    # {
        # If the key is equal to the root's key, then this is the node to be deleted

        # If a node with only one child or no child,
        # the root's right child replaces the root if the left child does not exist
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
        
        # If node has two children, get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    # }

    return root

# }

'''

***** BONEYARD *****

'''