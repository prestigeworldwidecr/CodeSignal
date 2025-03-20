'''

Hello and welcome! In today's lesson, we will delve into the practical application of the Breadth-First Search (BFS) algorithm to solve intriguing algorithmic problems. We'll focus on a popular problem - finding the shortest path from the given source to the given destination in an unweighted, connected, and undirected graph. This problem frequently surfaces in various domains, such as spatial networks, social networks, computing, and logistics.

Our problem involves developing a minimum-cost route planner by using the BFS algorithm for a logistics company. The company operates in a bustling urban environment where there are multiple pickup and drop-off points, represented as nodes in a graph. The paths between these points, represented as edges in the graph, are bidirectional. Therefore, you can traverse them both ways. In other words, the graph is undirected.

Your task is to find the shortest path from a source node to a destination node in this graph.

One possible approach to this problem is to use the so-called brute-force approach, where you calculate all the possible paths from the source to the destination and then determine the shortest path among them. While this strategy might sound like it solves the problem, in reality, it can be very inefficient, especially when the number of nodes and edges is large. Storing all possible paths could lead to overflowing memory and sluggish time complexity. In fact, the time complexity for this algorithm is exponential, meaning it wouldn't perform well for even medium-sized graphs.

A much more efficient way to address this problem is by using the Breadth-First Search (BFS) algorithm. BFS is perfect for finding the shortest path in an unweighted graph because it explores all nodes at the current 'depth' before moving on to nodes at the next 'depth level'.

So, the starting vertex lies at depth 0, and the minimal distance to it is also 0. All starting vertex's neighbors will be processed at depth 1, and the minimal distance to them is also 1. Continuing the pattern, when BFS processes the vertex at depth d, we can be sure the minimal distance to this vertex is d. As BFS doesn't visit the same vertex twice, we will eventually visit all vertices and set a minimal distance for each of them.

This Python solution uses the Breadth First Search algorithm to find the shortest path between two nodes in a bidirectional unweighted graph. It initializes a queue and visited set with the start node and then explores all its neighboring nodes. For each neighboring node, if it's not visited yet, the solution adds it to the visited set and enqueues a new distance and path. The solution ensures that the first path found to reach the end node is the shortest due to the structure of BFS.

By utilizing the optimized properties of the Breadth-First Search algorithm and fine-tuning the Python language, we have learned to solve a common real-world problem of finding the shortest path between two vertices in the graph. We used BFS to find the shortest path from a source to a desired destination and to determine if a path exists between two nodes in a graph. We discovered how BFS traverses the target graph level by level. The BFS property ensured that as soon as we found our destination, we had uncovered the shortest path.

Now that we have seen BFS in action on two real-world problems, it's time to practice! And guess what? You are almost done with this course too. Very proud of you!

'''

from collections import deque

def shortestPath(n, graph, start, end) :
# {
    # The queue stores tuples `(distance, path)`
    # where `distance` is the minimal distance to the current vertex
    # and `path` is the shortest path from the starting vertex to the current vertex
    queue = deque([(0, [start])])
    visited = set([start])
    min_distances = {start: 0}
    
    while (queue) :
    # {
        distance, path = queue.popleft()
        node = path[-1]
        min_distances[node] = distance

        if (node == end) :
        # {
            return distance, path
        # }

        else :
        # {
            None
        # }
        
        for neighbor in graph[node] :
        # {
            if (neighbor in visited) :
            # {
                None
            # }

            else :
            # {
                visited.add(neighbor)
                queue.append((distance + 1, path + [neighbor]))
            # }

        # }

    # }

    return float('inf'), []

# }

'''

***** BONEYARD *****

'''