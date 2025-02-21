'''

Congratulations! You're doing great. Up to this point, you've been building friendship networks. Now, let's add a little twist.

Suppose you find yourself in a new city and are attempting to map all of the bus routes that connect various spots throughout the city such as libraries, malls, and parks. Each bus route goes both ways: if you can travel from the mall to the park, you are supposed to always be able to return back to the mall using the same route.

The provided code aims to represent different bus routes in the city of Boston as a graph. However, it seems a minor bug is impeding the correct identification of connectivity between the spots.

'''

# Defining an empty dictionary to represent the Adjacency List of our graph
city_connections = {}

# Adding vertices to graph by adding keys to dictionary
city_connections["Boston Library"] = [] 
city_connections["Fenway Park"] = []  
city_connections["Quincy Market"] = []

# Adding an edge between two vertices
city_connections["Fenway Park"].append("Boston Library")

# Adding more edges
city_connections["Fenway Park"].append("Quincy Market")
city_connections["Boston Library"].append("Quincy Market")

# return trips
city_connections["Boston Library"].append("Fenway Park")
city_connections["Quincy Market"].append("Fenway Park")
city_connections["Quincy Market"].append("Boston Library")

print("Bus routes in Boston after adding edges:", city_connections)

'''

***** BONEYARD *****

'''