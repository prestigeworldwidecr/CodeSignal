'''

Welcome back, scholars! In today's session, we're diving deeply into the Breadth-first Search (BFS) Algorithm, specifically focusing on its application to trees. This potent search algorithm explores nodes level-by-level, examining all siblings before moving on to the children. By the end of our session, you'll have mastered the key aspects of BFS and its intricacies and will have become comfortable implementing BFS for traversing trees using Python.

To put this into context, imagine that you're navigating your way through a network of interconnected destinations, with each destination being a node in a tree. BFS is like taking a comprehensive sightseeing tour that starts at a landmark and visits all the destinations within the immediate vicinity before moving on to the next layer of destinations. With BFS, you ensure you've explored all the sights at each depth before venturing further.

Breadth-first Search (BFS) is a traversal algorithm used in graphs or tree structures — it's a specific way in which we can visit nodes. When we talk about 'visiting' nodes in BFS, we aim to visit nodes closest to the root node first before moving deeper into the tree. BFS, compared to Depth-first Search (DFS), is like exploring your neighborhood before moving on to the next town, while DFS would be like driving straight across the country, visiting towns en route, before coming back to your neighboring town.

BFS is an intuitive method that can form the basis for many algorithms in graph theory. For example, it is leveraged in algorithms for finding the shortest path in unweighted graphs, network broadcasting, and games and puzzles such as the Rubik's cube.

Let's create a visualization to illustrate the BFS technique. Imagine a tree structure representing a family lineage — a root node representing an ancestor and subsequent layers representing descendant generations. Starting from the ancestor, a BFS traversal visits all his immediate offspring before moving on to the grandchildren, then the great-grandchildren, and so on in cascading circles. This visualization helps illustrate how BFS explores nodes — it's like taking a layered tour of a genealogical tree!

A crucial aspect to consider in BFS is the usage of a queue. The queue is a data structure that holds the nodes still to be visited, and it follows a First In, First Out (FIFO) protocol — think of it as standing in line; the first one to get in is the first one to get out.

Conceptually, the BFS algorithm isn't overly complicated. It starts at the root and visits all direct children before moving deeper into the tree. The algorithm can be summed up as follows:

Start with the root node.
Visit the root node and add all its direct children to the queue.
Visit each node in the queue, adding all its unvisited children to the queue. Repeat this exercise until the queue is empty.
This algorithm guarantees that every node on level L (on distance L from the root node) will be processed (i.e., taken from the queue) earlier than any node on level L + 1 or further, which is what we are looking for.

This begs the question: what about the complexity of BFS? If all edges are unweighted, BFS guarantees finding the shortest path from the source to all reachable vertices. In terms of time complexity, performing BFS requires inspecting all vertices and edges, resulting in a time complexity of 
O
(
V
+
E
)
O(V+E) (where 
V
V stands for vertices or nodes, and 
E
E stands for edges or connections). As for trees 
E
=
V
−
1
E=V−1, the time complexity is 
O
(
V
)
O(V).

The space complexity would be 
O
(
V
)
O(V), as all vertices end up in the queue.

Before we roll up our sleeves and dive into coding, let's understand some underlying tools. To implement BFS in Python, we'll take advantage of Python's inbuilt collection deque to create a FIFO queue. The main advantage of using deque from the collections module as a queue instead of a list is that deque provides an 
O
(
1
)
O(1) complexity for append and pop operations compared to a list that provides 
O
(
n
)
O(n) complexity.

Here's a chunk of BFS code on a tree created using a dictionary where each key-value pair denotes a node and its children.

This code outputs an array, giving us the order in which the nodes were visited. Consider these nodes to represent hosts in a network. BFS finds high application in computer networks to broadcast packets, check live hosts, etc., assuming the network graph to be a tree.

To demonstrate an advanced real-life application of BFS on trees, consider it as a solution to find the shortest path in a network of interconnected systems, whether they be cities, computer systems, or web pages. BFS can traverse the network in such a way that it leads to the desired destination in the shortest possible way. This algorithm can be a lifesaver when dealing with large networks as it avoids unnecessary dives into unreachable paths.

The practical versatility of BFS on trees can handle many complex problems, thereby providing optimized solutions in coding interviews and industry projects.



'''

from collections import deque

def BFS(tree, root) :
# {
    visited = set() # Set to keep track of visited nodes
    visit_order = [] # List to keep visited nodes in order they are visited
    queue = deque() # A queue to add nodes for visiting

    queue.append(root) # We'll start at the root

    while (queue) : # While there are nodes to visit.
    # {
        node = queue.popleft() # Visit the first node in the queue
        visit_order.append(node) # Add it to the list of visited nodes
        visited.add(node) # And mark the node as visited

        # Now add all unvisited children to the queue
        for child in tree[node] :
        # {
            if (child in visited) :
            # {
                None
            # }

            else :
            # {
                queue.append(child)
            # }

        # }

    # }

    return visit_order # Return the order of visited nodes

# }

# Tree definition
tree = {
  'A' : ['B', 'C', 'D'],
  'B' : ['A', 'E'],
  'C' : ['A', 'F','G'],
  'D' : ['A', 'H'],
  'E' : ['B', 'I'],
  'F' : ['C'],
  'G' : ['C', 'J'],
  'H' : ['D'],
  'I' : ['E'],
  'J' : ['G']
    }

print(BFS(tree, 'A'))
# Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

'''

***** BONEYARD *****

'''