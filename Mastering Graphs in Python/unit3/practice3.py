"""

Fantastic! You"re doing a great job implementing depth-first searches in a graph. Now, let"s try a more challenging task!

Imagine you"ve been given the responsibility of analyzing a business offers network. A particular piece of code should identify the companies that have been visited, but it appears to be malfunctioning. Could you locate and rectify the issue to reveal the correct DFS traversal order?

"""

# Define the graph using a dictionary
offer_network = {
                    "Company_A": set(["Company_B", "Company_D"]),
                    "Company_B": set(["Company_A", "Company_C"]),
                    "Company_C": set(["Company_B", "Company_D"]),
                    "Company_D": set(["Company_A", "Company_C"])
                }

def DFS(offer_network, start_company, visited_offers) :
# {
    """
    Function implementing the DFS algorithm to traverse the graph.
    """
    if (start_company in visited_offers) :
    # {
        return
    # }

    else :
    # {
        visited_offers.add(start_company)
        print(start_company, end=" --> ")
        
        for partner in offer_network[start_company] :
        # {
            if (partner in visited_offers) :
            # {
                None
            # }

            else :
            # {
                DFS(offer_network, partner, visited_offers)
            # }
            
        # }

    # }

# }

visited_companies = set()
# Invoke DFS function, starting with "Company_A"
DFS(offer_network, "Company_A", visited_companies) 
print("\nVisited companies:", visited_companies) 

"""

***** BONEYARD *****

"""