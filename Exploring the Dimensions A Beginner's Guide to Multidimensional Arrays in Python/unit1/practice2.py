'''

You've been tasked with managing an apartment building's occupancy records. The provided code is supposed to print all unoccupied apartments on each floor. Unfortunately, it is currently not working as intended. Can you identify and fix the issue

'''

# Let's create a building with 2 floors and 3 apartments on each floor
# For each apartment - first element is the apartment number, second is the occupancy status (True - Occupied, False - Unoccupied)
building = [
                [("101", True), ("102", False), ("103", False)],
                [("201", True), ("202", True), ("203", False)]
            ]

for floor in building :
# {
    for apt in floor :
    # {
        # print(apt[1])
        
        if (apt[1] == True) : # current apartment is occupied
        # {
            None
        # }

        else :
        # {
            print("Apartment:", apt[0], "is not occupied.")
            # break
            # None
        # }

    # }

# }

'''

***** BONEYARD *****

  # Checking occupancy status

'''