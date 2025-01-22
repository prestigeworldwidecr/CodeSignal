'''

Great job, future algorithm master! You've fully explored the depths of "Depth-first Search," and now it's time to dive into a practical application.

Imagine that you are a city planner and need to map different city areas, ranging from the City Center to various suburbs. You will implement this, construct a tree to represent the areas and perform a depth-first search traversal.

Please use the TODO comments as guidance. Your task involves fleshing out the starter code to model the city's areas and conducting a DFS traversal of them. Let's rock it!

'''

class Area :
# {
    def __init__(self, name) :
    # {
        self.name = name
        self.subareas = []
    # }
        
    # TODO: Define the add_subarea method to add a subarea to a given area
    def add_subarea(self, subarea_name) :
    # {
        self.subareas.append(Area(subarea_name))
    # }
        
    # TODO: Define the dfs_traversal method to perform a depth-first search traversal over the areas
    def dfs_traversal(self, visited=None) :
    # {
        if (visited) :
        # {
            None
        # }
        
        else :
        # {
            visited = set()
        # }
        
        print(self.name)
        visited.add(self.name)

        for subarea in self.subareas :
        # {
            if (subarea.name in visited) :
            # {
                None
            # }
            
            else :
            # {
                subarea.dfs_traversal(visited)
            # }
        
        # }

    # }

# }

# TODO: Construct a tree to represent areas of a city
city = Area("San Francisco")
city.add_subarea("City Center")
city.add_subarea("Western Addition")
city.add_subarea("Marina District")

# TODO: Conduct a DFS traversal to print all areas
city.dfs_traversal()

'''

***** BONEYARD *****

'''