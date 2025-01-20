'''

Good job, champ! Now, let's tweak the provided starter code a bit.

Imagine that you are tasked with exploring the company structure in a new department. You notice that recently hired "Senior Engineer" and "Product Manager" are not reflected in the current company structure. Add them to the structure, both reporting to "VP Engineering". The existing "Engineer" should now report to a recently hired "Senior Engineer" instead of VP.

Could you please modify the code to help visualize this new hierarchy? It's time to prove your mettle!

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

# }

# Define a Company Hierarchy as a Non-Binary Tree
company_hierarchy_root = TreeNode("CEO")

vp_marketing = TreeNode("VP Marketing")
vp_finance = TreeNode("VP Finance")
vp_engineering = TreeNode("VP Engineering")
# senior_engineer = TreeNode("Senior_Engineer")

company_hierarchy_root.add_child(vp_marketing)
company_hierarchy_root.add_child(vp_finance)
company_hierarchy_root.add_child(vp_engineering)

# Let's add some more
director_marketing = TreeNode("Director Marketing")
vp_marketing.add_child(director_marketing)

senior_engineer = TreeNode("Senior Engineer")
vp_engineering.add_child(senior_engineer)

engineer = TreeNode("Engineer")
senior_engineer.add_child(engineer)

director_marketing = TreeNode("Product Manager")
vp_engineering.add_child(director_marketing)

# Function to print the Company Hierarchy Tree (i.e., Pre-order traversal)
def print_company_hierarchy(node) :
# {    
    if (node) :
    # {
        print("Position -> ", node.value)

        for child in node.children :
        # {
            print_company_hierarchy(child)
        # }

    # }

    else :
    # {
        return None
    # }

# }

# Print the company hierarchy
print_company_hierarchy(company_hierarchy_root)

'''

***** BONEYARD *****

'''