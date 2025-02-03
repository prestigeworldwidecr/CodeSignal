'''

Hey there, brainiac! Ready for your next stellar challenge? Picture this - a binary search tree (BST). Your mission, should you choose to accept it, orbits around a certain calculation. You need to craft an ingenious function that finds the biggest difference between the heights of left and right subtrees, considering all nodes in the given BST. The difference is always a non-negative number, i.e. the difference between 3 and 4 is 1, as well as the difference between 4 and 3.

Imagine a node as a mini tree with a left and right child forming its subtrees. And remember, in the cosmos of BST, the left child is always lesser, and the right is always greater!

Your function will take in the root of this BST, where the root node consists of integers. It will then output a single integer, the grandest difference in heights of two subtrees across all nodes.

'''

class TreeNode :
# {
    def __init__(self, x) :
    # {
        self.val = x
        self.left = None
        self.right = None
    # }

# }

def max_height_diff(root) :
# { 
    def height(node) :
    # {
        if (node) :
        # {
            return max(height(node.left), height(node.right)) + 1
        # }

        else :
        # { 
            return 0
        # }

    # }

    if (root) :
    # {
        None
    # }

    else :
    # {
        return 0
    # }

    left_height = height(root.left)
    right_height = height(root.right)
    current_diff = abs(left_height - right_height)

    left_diff = max_height_diff(root.left)
    right_diff = max_height_diff(root.right)
        
    return max(current_diff, left_diff, right_diff)

# }

# Test samples
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(17)

print(max_height_diff(root)) # Expected output: 1

'''

***** BONEYARD *****



    h = height(root)

    return h

# }

if (root.left) :
        # {
            None
        # }

        else :
        # {
            return -1
        # }

        right_height = height(root.right)

        if (root.right) :
        # {
            None
        # }

        else :
        # {
            return -1
        # }

        # left_height = left_height + 1

        # print

# print('@', h, root)
            
    # right_height = height(root.right, 0)

    # print(left_height, right_height)

# print(h, root)

        
            # print('!', h, root, root.val, root.right, root.left)

if (root) :
    # {
        None
    # }
    
    else :
    # {
        return -1
    # }

    return 1 + max(max_height_diff(root.left), max_height_diff(root.right))

def max_height_diff(root) :
# {
    def height(node) :
    # {
        # implement this
        if (node) :
        # {
            print(node.val)
            return max(height(node.left), height(node.right)) + 1
        # }

        else :
        # {
            return 0
        # }

    # }

    left_height = height(root.left)
    right_height = height(root.right)

    # implement this
    return max(left_height, right_height) - 1

# }

Height Calculation: Your height function is almost there! Remember, the height of a node is the maximum height of its left or right subtree plus one. You're returning -1 for None, but it should be 0 since a None node has a height of 0.

Recursive Traversal: You need to check the height difference for each node, not just the root. Consider how you can recursively call max_height_diff on both the left and right children of the current node.

Tracking Maximum Difference: As you traverse the tree, keep track of the maximum height difference found. You can use a variable to store this value and update it whenever you find a larger difference.

Great! Let's break it down. Your current implementation calculates the height of the left and right subtrees for the root node, but it doesn't yet find the maximum height difference across all nodes in the tree.

Here are a couple of questions to guide you:

How can you modify your function to recursively check each node in the tree for the height difference?
What would be a good way to keep track of the maximum difference found so far as you traverse the tree?

        # left_height = max_height_diff(node.left)
        # right_height = max_height_diff(node.right)
        
    if (root) :
    # {
        None
    # }        

    else :
    # {
        # implement this
        return 0
    # }

'''