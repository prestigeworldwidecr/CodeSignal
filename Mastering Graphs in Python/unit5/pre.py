'''

Welcome back to our continuing journey through the realm of advanced algorithms. Today, we'll spotlight the Breadth-First Search (BFS) algorithm for Graphs, extending our understanding from previous lessons on graph structures and the Depth-First Search (DFS) algorithm.

In our daily life, we often encounter situations modeled by BFS. For instance, imagine organizing a party and deciding whom to invite. You'd probably start with close friends (depth 1), then consider not-so-close friends (depth 2), and continue this way until you've exhausted your social graph. This eventual guest list could very well mirror a BFS traversal of your friend graph, starting with you.

The BFS algorithm, like a symbolic torch, sheds light on a graph from a starting vertex, traversing nodes breadthwise before going deeper. It explores all the neighbor vertices before moving on to vertices at the next depth level.

In this lesson, we seek to understand the BFS algorithm deeply, learn how to implement a step-by-step BFS traversal and a whole-graph BFS exploration in Python, as well as to apply BFS to solve complex problems.

So, put on your explorer hats, and let's delve deeper into this appealing world of BFS!

The Breadth-First Search (BFS) algorithm provides a systematic method for visiting every vertex in a graph. BFS begins at a chosen vertex and systematically visits all the vertices at the current depth before moving to the next depth level.

One can envision BFS as a deliberate explorer. For instance, if you are in a maze, unlike DFS, that could lead you to branch out into unknown directions recklessly, BFS carefully maps out the options at the current level before bravely forgoing one step ahead. BFS explores all reachable paths one step away from you before advancing to paths two steps away, and so on until it either finds the destination or exhausts all paths.

This layer-by-layer approach distinguishes BFS from DFS. While DFS extends as deeply as possible before retracting, BFS covers as much ground as possible at the current depth before advancing into deeper parts.

To better understand this concept, consider a simple graph composed of Nodes labeled A, B, C, D, E, and F, arranged as follows: A — B — C, A — D — E, and B — F:

The Breadth-First Search (BFS) algorithm provides a systematic method for visiting every vertex in a graph. BFS begins at a chosen vertex and systematically visits all the vertices at the current depth before moving to the next depth level.

One can envision BFS as a deliberate explorer. For instance, if you are in a maze, unlike DFS, that could lead you to branch out into unknown directions recklessly, BFS carefully maps out the options at the current level before bravely forgoing one step ahead. BFS explores all reachable paths one step away from you before advancing to paths two steps away, and so on until it either finds the destination or exhausts all paths.

This layer-by-layer approach distinguishes BFS from DFS. While DFS extends as deeply as possible before retracting, BFS covers as much ground as possible at the current depth before advancing into deeper parts.

To better understand this concept, consider a simple graph composed of Nodes labeled A, B, C, D, E, and F, arranged as follows: A — B — C, A — D — E, and B — F:

While understanding BFS, we naturally ask, "How does BFS differ from DFS?" DFS and BFS are essential graph traversal algorithms, but their methodologies differ significantly.

DFS is often relatable to exploring a dense forest or a complex network of tunnels. It selects a path and ventures deep in that direction within the graph before reverting to explore other paths. In contrast, BFS adopts a dissimilar strategy as it examines the entire breadth of a level within the graph before moving forward. This breadth-wise approach of BFS explores all nodes closest to or at the same distance from the start node before advancing to nodes at a farther level. If we relate this back to a video game analogy, BFS will explore all the rooms on one level of the map before moving to the next level.

Having understood BFS conceptually, let's now break down the mechanism of the BFS algorithm. At its core, it uses a queue data structure to administer its operations, providing an orderly and systematic method for node traversal.

Here's the pseudocode for the BFS algorithm:

initialize an empty Queue Q

Mark the starting vertex as visited and enqueue it into Q

WHILE Q is not empty DO
    Dequeue a vertex (say V) from Q
    FOR each neighbor (say N) of V DO
        IF N is not visited
            Mark N as visited and enqueue it into Q
        END IF
    END FOR
END WHILE

Implementing this BFS algorithm in Python requires the deque library for queue operations:

This Python code demonstrates a BFS() function that accepts a graph (presented as an adjacency list) and a starting point for the BFS traversal. It uses a deque to handle BFS operations and a set visited to track visited nodes.

By applying BFS, we can explore all reachable nodes from a chosen starting point. As shown in our previous example, if we start our BFS from Node A, we reach all the nodes (A -> B -> D -> C -> F -> E) in the graph.

Moreover, BFS proves useful in finding the shortest path between two nodes in an unweighted graph. This property is invaluable across a wide range of applications, from GPS navigation's shortest path issue to the issue of website ranking in internet hyperlink structure.

How about seeing our BFS algorithm in action? Consider a grid or a maze where each cell represents a unique node. If a cell is accessible from its neighbor cell, these two cells share an edge. BFS excels in such scenarios as it effectively computes the minimum number of steps required to move from a starting point to a goal point within a maze.

For instance, you may be familiar with puzzles involving moving a chess knight from one corner to another in the fewest possible moves. Such puzzles dictate a minimum movement constraint, which, in our BFS context, translates as the shortest path. BFS adeptly computes the optimum solution and is, therefore, a valuable tool in complex problem-solving.

This image presents a chess knight at its starting position, and the number in each cell corresponds to the minimal number of knight moves required to reach this cell. BFS can easily calculate this matrix!

That concludes our exploration of the Breadth-First Search (BFS) algorithm's intricacies! We've deepened our understanding of BFS, learned about its Python-based implementation, participated in a step-by-step walkthrough of a BFS traversal, and discovered how to conduct a whole-graph BFS exploration. Furthermore, we applied BFS to solve complex problems and unearthed its practicality in real-world applications.

BFS is a cornerstone in graph theory. Understanding its operations is an essential step towards comprehending real-world network structures, planning routes in GPS navigation, and acing coding interviews. Now, let's add some excitement with hands-on practice exercises! These exercises provide a great opportunity to apply the BFS traversal skills you learned today to navigate various graph data structures.

'''

from collections import deque

def BFS(graph, start) :
# {
    visited = set([start])   # a set to keep track of visited nodes
    queue = deque([start])  # a deque (double-ended queue) to manage BFS operations
    
    while (queue) :
    # {
        node = queue.popleft()  # dequeue a node
        print(node, end=" ")  # Output the visited node
        
        for neighbor in graph[node] :  # visit all the neighbors
        # {
            if (neighbor in visited) :  # enqueue unvisited neighbors
            # {
                None
            # }                

            else :
            # {
                queue.append(neighbor)
                visited.add(neighbor)  # mark the neighbor as visited
            # }

        # }

    # }

# }

# Use an adjacency list to represent the graph
graph = {'A': ['B', 'D'],
            'B': ['A', 'C', 'F'],
            'C': ['B'],
            'D': ['A', 'E'],
            'E': ['D'],
            'F': ['B']
        }

BFS(graph, 'A')  # Call the BFS function
# Output: A B D C F E

'''

***** BONEYARD *****

'''