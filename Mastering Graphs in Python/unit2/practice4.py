'''

Congratulations! With adjacency lists, you can represent not only the bus routes, but also tour routes!

As our journey with graph structures continues to unfold, we encounter a new question: Who wouldn't want to visit the Pyramid complex from the Sphinx?

Let's extend the current tour_route and create a direct route from the Sphinx to the Pyramid complex. Are you ready for action?

'''

# Defining an empty dictionary to represent the Adjacency List of our graph
tour_route = {}

# TODO: Add vertices "Pyramids of Giza", "Sphinx", "Ancient Memphis" and "Egyptian Museum" to our graph by adding keys to our dictionary 
tour_route["Pyramids of Giza"] = []
tour_route["Sphinx"] = []
tour_route["Ancient Memphis"] = []
tour_route["Egyptian Museum"] = []

# TODO: Add a direct edge (2-way route) from the Sphinx to the Pyramids of Giza.
tour_route["Sphinx"].append("Pyramids of Giza")
tour_route["Pyramids of Giza"].append("Sphinx")

# Adding more edges
tour_route["Sphinx"].append("Ancient Memphis")
tour_route["Ancient Memphis"].append("Sphinx")  # It's a two-way route
tour_route["Sphinx"].append("Egyptian Museum")
tour_route["Egyptian Museum"].append("Sphinx")  # It's a two-way route

print("Tour route graph:", tour_route)

'''

***** BONEYARD *****

'''