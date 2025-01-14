'''

Hello, fellow explorer! Are you ready to dig deeper into the fascinating world of trees?

Imagine this: You've had a busy day browsing the web, and your screen is cluttered with numerous tabs. Trying to recall all the websites you visited could be a tedious task!

Fear not! In this hands-on experience, we're going to visualize your browsing history as a tree. This will create a fun, understandable, and efficient record of your browsing activity.

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
        for child in self.children :
        # {
            if (child) :
            # {
                None
            # }

            else :
            # {
                self.children = child
            # }

        # }

    # }

# Create a Browser History as a Non-Binary Tree
browser_history_root = TreeNode("HomePage")

google = TreeNode("Google.com")
youtube = TreeNode("Youtube.com")
codesignal = TreeNode("CodeSignal.com")

browser_history_root.add_child(google)
browser_history_root.add_child(youtube)
browser_history_root.add_child(codesignal)

# Let's add some more
gmail = TreeNode("Gmail.com")
google.add_child(gmail)

codesignal_tour = TreeNode("CodeSignal.com/Tour")
codesignal_blog = TreeNode("CodeSignal.com/Blog")
codesignal.add_child(codesignal_tour)
codesignal.add_child(codesignal_blog)

# Function to print the Browser History Tree (i.e., Pre-order traversal)
def print_history(node):
# {
    if (node) :
    # {
        print("Visited -> ", node.value)

        for child in node.children :
        # {
            print_history(child)
        # }

    # }

    else :
    # {
        return None
    # }

# }

print_history(browser_history_root)

'''

***** BONEYARD *****

'''