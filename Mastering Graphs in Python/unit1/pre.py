'''

Introduction to Building a Graph with the Adjacency Matrix
In today's session, we move to the fascinating realm of graph structures. We'll dive deeper into examining one distinctive way of representing graphs - using an Adjacency Matrix. Our specific objective is to unravel how to construct an Adjacency Matrix to depict a given graph using Python, comprehend its underlying structure, and ascertain when this particular representation becomes most advantageous.

To help understand the role of an Adjacency Matrix, let's consider a practical scenario. Suppose you're using social media. Every time you connect with someone — by accepting their friend request, adding them back to your circle, or linking profiles — you're building a real-life graph where nodes represent users’ profiles and edges signify their connections. Now, how would you represent this social network graph so that you can quickly identify who's connected to whom? This is a perfect use case for an Adjacency Matrix representation.

So, what is an Adjacency Matrix? In essence, it is a square matrix, a two-dimensional array, where each cell (i, j) signifies the weight of the edge between vertices i and j in the graph. Distinct from other matrix-like representations, the most striking aspect of an Adjacency Matrix is its ability to provide a concise, easy-to-understand form of visualizing and depicting the vertex connections in any given graph.

To illustrate, let's consider a simple scenario of a small group of friends: Alice, Bob, and Carol. Let's say Alice is friends with both Bob and Carol, but Bob and Carol don't know each other. In social media terms, Alice would have connections with both Bob and Carol. However, Bob's profile would not show Carol as a connection, and the converse holds true as well. Let's look at this graph:

This is precisely the relation we aim to depict using an Adjacency Matrix. Let's create a table that shows the relationships between Alice, Bob, and Carol. A backtick on the intersection of a row and a column represents corresponding users are friends:

We can build the same table in Python, representing backtick as 1 and its absence as 0:

Building an Adjacency Matrix
So, how do we go about building an Adjacency Matrix more generally? In the simplest terms, we begin by setting the size of the matrix equal to the number of vertices in the graph. Each cell in the matrix translates into a possible edge in the graph. By traversing the graph and identifying each edge, we can capture this data in the matrix.

Using Python, we can represent this as follows:

Initialize a list of lists (to replicate a 2D array or a matrix) where each cell M[i][j] equals 0. This implies that there are no edges to start with.
As we find an edge between vertices i and j, we set both M[i][j] and M[j][i] to 1.
Below is a sample Python code that depicts the simple friend group we considered earlier:

'''

M = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0],
    ]

# Mapping friends to numbers for simplicity: Alice: 0, Bob: 1, Carol: 2
n = 3  # number of friends
M = [[0] * n for _ in range(n)]  # Adjacency Matrix

# Alice is friends with Bob and Carol
M[0][1] = M[0][2] = 1
M[1][0] = M[2][0] = 1

# Print the matrix
for row in M:
    print(row)

# Output:
# [0, 1, 1]
# [1, 0, 0]
# [1, 0, 0]

'''

***** BONEYARD *****

'''