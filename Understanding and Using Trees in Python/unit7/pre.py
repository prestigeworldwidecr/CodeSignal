'''

Welcome to today's lesson! In this practice-based session, we'll unravel the mysteries of Binary Search Trees (BSTs). We will focus on two well-known interview problems related to BSTs. Solving these problems will solidify your understanding of trees and provide you with hands-on experience that will be invaluable during future job interviews. Think of this as mock interviews before the real one! So, let's put on our problem-solving hats and dive right in!

Here is the first problem: we need to write a function that checks if a BST is balanced. The tree is balanced if for each vertex, the size of the left subtree differs from the size of the right subtree by at most 1.

You might wonder, "Why do we need to do this?". Well, this problem frequently appears in job interviews because checking the balance of a tree optimizes search operations.

Interestingly, consider trying to balance on one foot. If the weight on your left and right sides is not equal, you'll topple over, right? Similarly, a binary tree is considered balanced when the left and right sides are equal, or at least the difference is no more than one. Isn't that fascinating?

So, let's discuss the naive approach to solving this problem. One could start by calculating the heights of all subtrees and then checking whether the heights of each node's left and right subtrees differ by no more than one. While this approach is functional, it is inefficient since it involves traversing the entire tree multiple times and making duplicate calculations.

But don't worry, there's a more efficient way! Instead of traversing the tree multiple times, we can use recursion to do it all in one sweep. We calculate the heights of the subtrees while simultaneously checking the balance condition. So, essentially, we're hitting two birds with one stone!

Let's dive into the actual code. Checking if a tree is balanced involves examining all its nodes. However, we can approach this more efficiently. Instead of calculating the height of each node separately, which involves repeated traversal, we can implement a check_balance function that computes both the height of the tree and checks balance in one recursive traversal. The function should return an indicator is_balanced = False when the tree is unbalanced to allow for early termination without visiting all nodes. Here's what the updated solution would look like:

This solution performs with 
O
(
n
)
O(n) time complexity, where 
n
n is the number of nodes in the tree, as each node is visited only once.

Imagine needing to identify the player with the k-th best result while constructing a leaderboard for a game. We're expected to find this kth smallest element in a Binary Search Tree (BST) where the players' scores are stored for efficient retrieval.

We're dealing with a BST where each player's score represents a node. Our goal is to identify the k-th smallest score, which translates to the k-th smallest element within the BST.

A simplistic, blunt approach involves storing all the elements in an array. We then sort it and return the kth element. This brute force method, however, has a time complexity of 
O
(
n
log
⁡
n
)
O(nlogn) due to the sorting operation. It also necessitates extra space, thus revealing a space complexity of 
O
(
n
)
O(n). There must be a more efficient method, right?

A more efficient and memory-friendly strategy to address this task entails employing a recursive method without explicit in-order traversal.

This approach involves counting the number of nodes in the left subtree of the root. If the count of nodes matches k - 1, the root value is the k-th smallest element we're looking for. If the k is smaller or equal to the count, the k-th smallest is in the left subtree. If the k is larger, then the k-th smallest is in the right subtree, and we adjust k accordingly.

Let's create the function kthSmallest, where we utilize a recursive solution to retrieve the k-th smallest score directly:

Please note that this code snippet relies on a helper function, countNodes, which returns the count of nodes in a given tree. The main function compares the total nodes in the left subtree with k and decides whether the kth smallest is in the left subtree or right subtree or if it is the root itself.

This approach has 
O
(
k
)
O(k) time complexity, as we visit at most k vertices in the tree.

Well done! You've navigated the ins and outs of binary search trees! You've successfully learned how to validate the balance of a BST and how to find the second minimum value in a BST. These concepts are highly relevant for any software engineering job interview. Let's give you a round of applause for mastering these concepts!

'''

def is_balanced(root) -> bool:
# {
    # returns (height, is_balanced)
    def check_balance(node) -> (int, bool) :
    # {
        if (node) :
        # {
            None
        # }

        else :
        # { 
            return 0, True
        # }

        left_height = check_balance(node.left) 
        left_balanced = check_balance(node.left)

        if (left_balanced) :
        # {
            None
        # }

        else :
        # {
            return -1, False
        # }
        
        right_height = check_balance(node.right) 
        right_balanced = check_balance(node.right)

        if (right_balanced):
        # {
            None
        # }

        else :
        # {
            return -1, False            
        # }

        height = max(left_height, right_height) + 1
        is_balanced = abs(left_height - right_height) <= 1

        return height, is_balanced
    
    # }

    height, balanced = check_balance(root)

    return balanced

# }

def kthSmallest(root, k) :
# {
    # The number of nodes in the left subtree of the root
    # left_nodes = countNodes(root.left) if root else 0
    if (root) :
    # {
        left_nodes = countNodes(root.left)
    # }

    else :
    # {
        left_nodes = 0
    # }
    
    # If k is equal to the number of nodes in the left subtree plus 1, 
    # That means we must return the root's value as we've reached the k-th smallest
    if (k == left_nodes + 1) :
    # {
        return root.val
    # }
    
    # If there are more than k nodes in the left subtree,
    # The k-th smallest must be in the left subtree.
    elif (k <= left_nodes) :
    # {
        return kthSmallest(root.left, k)
    # }
    
    # If there are less than k nodes in the left subtree,
    # The k-th smallest must be in the right subtree.
    else :
    # {
        return kthSmallest(root.right, k - 1 - left_nodes) 
    # }

# }

def countNodes(root) :
# {    
    if (root) :
    # {
        None
    # }
    
    else :
    # {
        return 0
    # }

    return 1 + countNodes(root.left) + countNodes(root.right)

# }

'''

***** BONEYARD *****

'''