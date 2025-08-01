'''

Great job diving into multidimensional arrays! Next challenge: let's simulate adding a new feature to our apartment building management system. You'll need to expand our current setup to accommodate more residents in our digital building. Remember, adding a new floor and ensuring we can visit all floors, including the new one, is crucial for the accommodation.

'''

# Initializing a 2D array that represents an apartment building
apartments = [["Apt 101", "Apt 102"], 
              ["Apt 201", "Apt 202"],
              ["Apt 301", "Apt 302"]]

# TODO: Add a new floor with apartments to our apartment building and then make a walk visiting each apartment on every floor.
for floor in apartments :
# {
    for apartment in floor :
    # {
        print(apartment)
    # }
    
# }


'''

***** BONEYARD *****

# print()

print(apartments[0])  # Accessing the first apartment on the first floor

for i in range(len(apartments)) :
# {
    for j in range(len(apartments[0])) :
    # {
        # apartments[i][j] = "Apt " + str(i + 1) + str(j + 1)
        # print(apartments[i][j], end = ' ')
        print(i, j)
    # }

# }



'''