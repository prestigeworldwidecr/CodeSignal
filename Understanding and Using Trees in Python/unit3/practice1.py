'''

Great job on your space journey thus far, Voyager! You've recently ventured into the exciting realm of the Breadth-First Search (BFS) algorithm, which is applied to non-binary trees. It's now time to apply this knowledge to a real-life scenario.

Suppose you're an explorer charting a course through the world's major rainforests. Starting from the Amazon rainforest, your objective is to explore every neighboring forest. Your task involves using the Breadth-First Search algorithm to plan your route.

'''

from collections import deque

# Represents the forest as a dictionary
forest = {
            "Amazon_Rainforest": ["Congo_Basin", "Southeast_Asian_Rainforests"],
            "Congo_Basin": ["Guinea_Rainforests", "New_Guinea_Rainforests"],
            "Southeast_Asian_Rainforests": ["Sundaland_Rainforests", "Wallacea_Rainforests"],
            "Guinea_Rainforests": [],
            "New_Guinea_Rainforests": ["Papua_New_Guinea_Rainforests"],
            "Sundaland_Rainforests": [],
            "Wallacea_Rainforests": ["Celebes_Rainforests"],
            "Papua_New_Guinea_Rainforests": [],
            "Celebes_Rainforests": []
        }

def BFS(forest, root='Amazon_Rainforest'):
# {
    # BFS algorithm to visit all forests
    queue = deque()  # Queue to hold forest regions
    queue.append(root)  # Starting search from root
    visited = []  # List to hold visited forests

    while (queue) :
    # {
        current_forest = queue.popleft()
        visited.append(current_forest)  # Mark current forest as visited

        # Queuing the forests not yet visited
        if (current_forest in forest) :
        # {
            for neighbouring_forest in forest[current_forest] :
            # {
                if neighbouring_forest in visited :
                # {
                    None
                # }

                else :
                # {
                    queue.append(neighbouring_forest)
                # }

            # }

        # }

    # }
    
    return visited

# }

print(" -> ".join(BFS(forest, root="Amazon_Rainforest")))  # Using Amazon Rainforest as root

'''

***** BONEYARD *****

'''