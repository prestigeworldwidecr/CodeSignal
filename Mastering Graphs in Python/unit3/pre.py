'''

Welcome back! Today, we are continuing our exploratory journey through the intricate world of graph data structures. We have already navigated the meandering paths of adjacency matrices and adjacency lists. Today, we're stepping into another mesmerizing aspect of this data structures journey - the Depth-First Search (DFS) algorithm. Also known as the 'maze explorer', DFS is a master key to various graph-related challenges in fields ranging from computer networking to genetic genealogy.

One of the hallmarks of DFS is its penchant for penetrating as far as possible into a graph along a route before retracing its steps (or backtracking) when it reaches an endpoint. Then it delves into the next available route. It can be visualized as exploration within a network of caves, where each cave has multiple tunnels. You choose a tunnel, traverse as far as you can until you reach a dead end, return, choose another unexplored tunnel, and continue this process until no path is left unexplored.

Depth-First Search or DFS is an algorithmic solution for traversing or searching through tree data structures or graph nodes. Its strategy of diving as deep as possible into a graph's branch before backtracking inspired its nomenclature.

Let’s visualize a familiar scenario for a moment. Suppose we're playing a video game situated in a complex map, loaded with winding paths and hidden rooms. You opt for a path and continue walking until you encounter a dead end. What's the next move? You revert, select another available path, and persist with this procedure until all possible paths are traversed — that’s DFS for you!

To better understand DFS within a graph context, consider this graph:

Here's how DFS explores the graph: A > B > D > E > C. DFS proceeds from A to B, then advances from B to D. As D has no unvisited adjacent nodes, DFS backtracks to B and resumes the traversal towards E. When all adjoining nodes from E are visited, DFS backtracks to B once again and finally advances towards C.

Now, let's discover the DFS algorithm! It primarily initiates at the root or the start node of a graph plunges as far as feasible down a branch, and then backtracks when it cannot delve further (i.e., it arrives at a node with no unvisited adjacent nodes).

Here's a high-level pseudocode illustration of the DFS algorithm to ease our discussion:

1. Mark the current node as 'visited' and print the node.
2. For every adjacent unvisited node of the current node:
    2.1. Invoke the recursive DFS function.

Discussing DFS's time and space complexity is pivotal to understanding an algorithm's efficiency. The time complexity of DFS is 
O
(
V
+
E
)
O(V+E), where 
V
V indicates the number of vertices, and 
E
E represents the number of edges (connections between vertices) in the graph. The space complexity is 
O
(
V
)
O(V), considering the storage of the visited nodes

In this Python code, we define a recursive function DFS(), taking three parameters — graph, start, and visited. The set visited keeps track of all visited nodes. We commence from the start node and add it to visited. For any next_node in the adjacency list of start that is not yet visited, we recursively invoke DFS().

DFS's versatility makes it a powerful tool with a broad spectrum of applications. On a higher level, DFS excels in problems related to the establishment of connections within graphs and the discovery of pathways between two nodes. In terms of time efficiency, DFS thrives on densely connected graphs where the probability of finding the target quickly exceeds that of BFS.

However, all tools have their limitations and nuances. DFS does not perform optimally in problems necessitating the shortest path, such as GPS routing problems, where BFS is a superior choice. Además, DFS requires careful management when dealing with cycles within the graph, as it could end up in an infinite loop without effective control over the visited nodes.

Having mastered the DFS algorithm, let's delve into its real-world applications. One significant application of DFS is in the domain of computer games. Envision a scenario where you are an explorer venturing through a mythical jungle in search of sacred artifacts scattered across a complex network of trails filled with obstacles and rewards. To ensure a unique route is chosen each time, the game could employ DFS to steer your game character through the virtual jungle.

Another intriguing application of DFS lies within the social network domain. DFS algorithms could navigate a connection web from a known user to an unknown user. Using DFS, developers can innovate a feature showcasing how two users are connected through mutual connections on the platform, similar to LinkedIn's feature that displays how a user is connected to another user through mutual connections.

One practical use of DFS is determining whether a graph contains a cycle. If we encounter a previously visited node while executing DFS, then a cycle exists in the graph.

Exploring the graph starting at A using DFS, our path would be A > B > D > E > C. On arriving at node C and checking its neighbors, we find that A and E have already been visited, which suggests a cycle in the graph.

DFS can also be deployed for pathfinding. Suppose we have a maze represented as a graph, and the goal is to find a path from one corner to another. The DFS algorithm would enable exploration of paths, selecting a path, and following it to the farthest point until a dead-end is reached before reverting and attempting the next available path until the destination is reached. Each move marks the node as visited and the path taken is retained.

However, while DFS can help locate a path, it does not guarantee the most efficient or shortest path. In scenarios requiring the shortest path, we would utilize another algorithm, like BFS or Dijkstra's algorithm.

Congratulations on cementing your understanding of a foundational algorithm in computer science — Depth-First Search! You've delved into the inner workings of DFS, differentiated between DFS and BFS, and implemented DFS in Python. Moreover, you have recognized the applicability of DFS through several uses in real-world scenarios such as social networking or game algorithms.

'''

def DFS(graph, start, visited) :
# {
    visited.add(start)
    print(start, end=' ')
    
    for next_node in graph[start] :
    # {
        if(next_node in visited) :
        # {
            None
        # }

        else :
        # {
            DFS(graph, next_node, visited)
        # }

    # }

# }

graph = {
            'A': set(['B', 'C']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A']),
            'D': set(['B']),
            'E': set(['B']),
        }

visited = set()
DFS(graph, 'A', visited)  # Output: A B D E C

'''

***** BONEYARD *****

'''