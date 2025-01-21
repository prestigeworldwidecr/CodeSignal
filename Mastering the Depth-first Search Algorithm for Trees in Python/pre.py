'''

Introduction to Depth-first Search (DFS)
In today's lesson, we examine the specifics of a crucial tree traversal algorithm: Depth-first Search (DFS). So far in this course, we have emphasized the importance of tree structures in computer science and analyzed the underlying complexities of both binary and non-binary trees. We are now ready to explore an essential tree traversal strategy — the DFS algorithm on trees.

Before moving forward, let's set a clear roadmap for our journey. By the end of this lesson, you will have a thorough understanding of the mechanics of DFS and its application to trees. We will guide you through vivid examples and step-by-step Python code, transforming your theoretical knowledge of DFS into practical skills. Eventually, in our hands-on section, you will put your skills to the test on the CodeSignal IDE, solidifying your growing mastery over the DFS algorithm.

Let's delve into this exciting realm of algorithmic exploration!

How would you explore an uncharted forest? Where would you begin? Would you inspect each pathway at ground level before climbing a tree, or would you ascend the first tree you encounter, climbing as high as possible before descending? The latter approach mirrors the strategy that the Depth-first Search (DFS) algorithm uses when exploring trees or graphs.

Essentially, DFS is a tree traversal technique that seeks to explore as far down a pathway (or to as great a depth) as possible before returning (or backtracking). Instead of splitting its focus over multiple pathways concurrently, DFS concentrates on exploring one pathway as thoroughly as possible before retreating to explore other pathways. Here's another real-world analogy for DFS: consider how you might navigate a labyrinth; you'd follow a twisting, turning path to its end before backtracking to explore another path. This principle lies at the heart of DFS — explore the depth before the breadth!

The DFS Algorithm at a Glance
A journey of a thousand miles begins with a single step. For DFS, that first step is the root node of the tree (or an arbitrary node chosen as the root when dealing with a graph). Let's closely examine the stages involved in conducting a DFS:

The DFS algorithm starts at the root node, marking it as visited.
For every child node of the starter node:
If the child hasn't been visited, the algorithm recursively executes from the child node.
If the child has already been visited, the algorithm skips this node and proceeds to the next child.
The algorithm automatically finishes when all achievable nodes have been visited.

Understanding an algorithm's efficiency is a crucial aspect of comprehending any algorithm. Efficiency includes time and space complexity, both of which consider how running time or memory space used by an algorithm increases with the input size.

For DFS, the time complexity is 
O
(
V
+
E
)
O(V+E), where 
V
V represents the number of vertices (or nodes), and 
E
E represents the number of edges. DFS needs to visit every edge and vertex at least once, which dictates its time complexity. For trees specifically, as 
E
=
V
−
1
E=V−1, the dfs time complexity is 
O
(
V
)
O(V).

The space complexity of DFS is 
O
(
V
)
O(V).

Practical application solidifies theoretical understanding. DFS is used extensively to solve complex problems related to connected components, topological sorting, and detecting cycles, among other issues. For example, if we need to find a path from node 'A' to 'J' in our tree above, DFS can identify such a path.

The find_path function leverages DFS to identify a path from start to end. It iterates through tree nodes until it locates the desired node, providing an example of how DFS assists in addressing tree-related problems.

And there you have it! We've taken a deep dive into the Depth-first Search for trees, emerging with a wealth of knowledge about its workings, advantages, and Python implementation. Now, with a more comprehensive understanding of tree data structures, you're better prepared to tackle complex coding problems involving DFS algorithms. We've explained how DFS works, walked you through its Python implementation, and explored its efficiency by analyzing time and space complexity. By applying DFS principles to a real-world problem, you've glimpsed how DFS can lead to efficient solutions.

'''

def dfs(tree, root, visited, traversal) :
# {
    traversal.append(root)
    visited.add(root)

    for child in tree[root] :
    # {
        if (child in visited) :
        # {
            None
        # }

        else :
        # {
            dfs(tree, child, visited, traversal)
        # }

    # }

# }

tree = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A'],
    'D': ['A', 'G', 'H'],
    'E': ['B'],
    'F': ['B', 'I', 'J'],
    'G': ['D'],
    'H': ['D'],
    'I': ['F'],
    'J': ['F'],
    }

visited = set()
traversal = []
dfs(tree, 'A', visited, traversal)

print(' -> '.join(traversal)) # A -> B -> E -> F -> I -> J -> C -> D -> G -> H

def find_path(tree, start, end, visited, path=[]) :
# {
    path = path + [start]
    visited.add(start)

    if (start == end) :
    # {
        return path
    # }

    else :
    # {
        None
    # }
    
    for node in tree[start] :
    # {
        if node in visited :
        # {
            None
        # }           
            
        else :
        # {
            new_path = find_path(tree, node, end, visited, path)

            if (new_path) :
            # {
                return new_path
            # }

            else :
            # {
                None
            # }

        # }

    # }

    return None

# }

visited = set()
print(find_path(tree, 'A', 'J', visited)) # Output: ['A', 'B', 'F', 'J']

'''

***** BONEYARD *****

'''