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
        # implement this
        if (node) :
        # {
            # print(node.val)
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

# Test samples
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(17)

print(max_height_diff(root)) # Expected output: 1

'''

***** BONEYARD *****


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