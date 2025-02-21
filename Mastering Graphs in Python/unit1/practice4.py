'''

Well done, explorer! You are navigating through the complexities of graph structures impressively. Let's delve further into this fascinating world of adjacency matrices.

Imagine that you're managing multiple projects and want to keep track of overlaps in team members across projects. To depict this relationship more clearly, you decide to use an adjacency matrix.

The starter code, unfortunately, is missing some crucial pieces. Could you implement these missing parts to construct the adjacency matrix, thereby providing a clear picture of the projects with shared team members?

'''

# Number of projects
n = 7

# Initialize the adjacency matrix
# M = [[0] * n for _ in range(n)]
M = []
for _ in range(n) :
# {    
    M.append([0] * n)
# }

# TODO: Map the overlapping project teams in the adjacency matrix. Consider that projects that have overlapping team members are: 
# 1) projects at indices 0 and 1
# 2) projects at indices 2 and 6 
M[0][1] = M[1][0] = 1
M[2][6] = M[6][2] = 1


'''

***** BONEYARD *****


# Print the adjacency matrix
for row in M :
# {
    print(row)
# }

for i in range(n) :
# {
    for j in range(n) :
    # {
        if (i != j) :
        # {
            if (M[i][j] == 0) :
            # {
                for k in range(n) :
                # {
                    # if ((M[i][k] == None and M[k][j] == None) or M[i][k] != M[k][j]) :
                    if (M[i][k] == None and M[k][j] == None) :
                    # {
                        None
                    # }
                    
                    else :
                    # {
                        print("Based on mutual friends,")
                        print("User,", M[i], "and User", M[j], "might know each other.")
                    # }
            
                # }
            
            # }

            else :
            # {
                None
            # }
        
        #}

    # }

# }

'''