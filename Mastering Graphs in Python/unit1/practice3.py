'''

Congratulations! Having completed the first few exercises by running pre-written code and making small modifications, it's now time to delve deeper and confront a real-world debugging challenge.

In our social network, let's assume that we have an updated set of relationships at our disposal. We have Python code that constructs an adjacency matrix and employs it to recommend potential friends based on their shared connections.

However, as can occasionally occur, there might be a bug causing unforeseen results. Can you identify and resolve the problem? Please remember that in the realm of real-world coding, debugging plays a crucial role!

'''

# Number of friends
n = 5
users = ['Alice', 'Bob', 'Carol', 'David', 'Emma']

# Initialize the adjacency matrix
# M = [[0] * n for _ in range(n)]
M = []
for _ in range(n) :
# {
    M.append([0] * n)
# }

# Add relationships in the adjacency matrix
# Alice
M[0][1] = M[0][3] = M[0][4] = 1
# Bob
M[1][0] = M[1][2] = M[1][3] = 1
# Carol
# M[1][2] = 1
M[2][1] = 1
# David
M[3][0] = M[3][1] = M[3][4] = 1
# Emma
M[4][0] = M[4][3] = 1

# Print the adjacency matrix
for row in M :
# {
    print(row)
# }

# Suggest friends for each user, avoiding cases where users are suggested to be friends with themselves
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
                        print("User,", users[i], "and User", users[j], "might know each other.")
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

***** BONEYARD *****

Good try, but there's a small issue. The original bug was in the adjacency matrix setup for Carol. Instead of M[1][2] = 1, it should be M[2][1] = 1. Would you like some help fixing this?

'''