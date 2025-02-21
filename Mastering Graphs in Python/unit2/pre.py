'''

Greetings! Welcome to the next stage of our journey in the "Mastering Graphs in Python" course! Up to this point, we've explored graph structures and adjacency matrices in great detail, uncovering the mechanics behind these critical data structures. In today's session, we'll delve into another essential graph representation: the adjacency list.

Consider your friends list on a social networking site like Facebook; this can be viewed as a classic example of an adjacency list. Each person on Facebook has a list of connections (or friends), and you can discover mutual connections by examining the overlap in your friends lists. That's precisely how adjacency lists function!

The adjacency list representation is generally more space-efficient for storing sparse graphs compared to adjacency matrices. We'll begin by theoretically understanding adjacency lists and then illustrate how to implement them in Python. We'll then learn how to perform basic operations. To put theory into practice, we'll simulate a real scenario: building a social network graph using an adjacency list. So, let's get started!

Before we dive into the implementation, let's familiarize ourselves with the concept of adjacency lists. An adjacency list simplifies a graph into its most essential and straightforward form. It's similar to creating a contacts list on your phone, where you have a compendium of everyone you can call. Likewise, in a graph, every node keeps a list, akin to a contacts list, of the nodes it's connected to.

Let's further refine our understanding with a simple example:

Suppose we have four interconnected cities shown below.

San Diego: San Francisco, Los Angeles, Las Vegas
San Francisco: San Diego, Los Angeles
Los Angeles: San Diego, San Francisco, Las Vegas
Las Vegas: San Diego, Los Angeles

When it comes to Python, the built-in dictionaries and lists are invaluable for representing adjacency lists.

In an adjacency list representation, dictionaries function exceptionally well. The keys represent the nodes of the graph, and the corresponding values are lists containing the adjacent nodes.

You can translate the city roadmap mentioned above into a Python dictionary as follows:

Once we have an adjacency list, performing basic operations becomes a breeze. Since our adjacency list is essentially a dictionary of lists, adding a vertex is as simple as adding a new key-value pair to our dictionary. In the same vein, adding an edge entails merely adding a new element to the pertinent list. Ascertaining the existence of an edge is just as straightforward; all we need to do is check if a vertex exists in another vertex’s list.

Here's how these operations translate into Python code:

If we want to add a new city (let's say 'Seattle') to our roadmap, we write:

To add a new road (refer to edge in graph theory) from San Diego to Seattle, we simply need to add 'Seattle' to San Diego's list:

Adjacency lists find myriad practical applications. One notable example is social networks like Facebook or LinkedIn. In such networks, each individual represents a node in the graph. When two people become friends or connections, an edge forms between their corresponding nodes.

Consider three friends: 'John', 'Emma', and 'Sam'. We can model their friendships using an adjacency list as follows:

This adjacency list tells us that John, Emma, and Sam are all friends with each other - a classic 'Friends List'!

Congratulations on your progress! You've just expanded your knowledge of graph structures by mastering adjacency lists. An adjacency list is a straightforward, no-frills method of representing a graph's structure, explicitly listing all neighbors for each vertex. It also offers the added benefit of being more space-efficient compared to adjacency matrices, especially for sparse graphs.

In summary, you've understood what adjacency lists are and how to create one for a graph using Python. You've become proficient in performing basic operations like adding a vertex, adding an edge, and checking if an edge exists. Last but certainly not least, you've delved into real-world scenarios of adjacency lists by building a social network graph.

'''

roadmap = {
            'San Diego': ['San Francisco', 'Los Angeles', 'Las Vegas'],
            'San Francisco': ['San Diego', 'Los Angeles'],
            'Los Angeles': ['San Diego', 'San Francisco', 'Las Vegas'],
            'Las Vegas': ['San Diego', 'Los Angeles']
        }

roadmap['Seattle'] = []

roadmap['San Diego'].append('Seattle')    # Adds an edge between San Diego and Seattle.

exists = 'Seattle' in roadmap['San Diego']  # Returns True.

friends_network = {
                    'John': ['Emma', 'Sam'],
                    'Emma': ['John', 'Sam'],
                    'Sam': ['John', 'Emma']
                }


'''

***** BONEYARD *****

'''