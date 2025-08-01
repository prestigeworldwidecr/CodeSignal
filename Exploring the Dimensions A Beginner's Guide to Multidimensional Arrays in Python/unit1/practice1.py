'''

You've done a fantastic job learning how to update elements in a multidimensional array! For this challenge, you'll apply what you've learned to the apartmentBuilding array. Please update the name of "Apt 202" to "Renovated Apt 202" in the provided multidimensional array. Do not change the array definition, update the element after creating the array.

This simple task will help reinforce your ability to reference and update elements within nested lists. Let's enhance our apartment building!

'''

apartmentBuilding = [
                        ["Apt 101", "Apt 102", "Apt 103"], 
                        ["Apt 201", "Apt 202", "Apt 203"], 
                        ["Apt 301", "Apt 302", "Apt 303"]
                    ]

# TODO: Update "Apt 202" to "Renovated Apt 202" in `apartmentBuilding`
apartmentBuilding[1][1] = "Renovated Apt 202"

# Print all the apartments after the renovation update
for floor in apartmentBuilding :
# {
    for unit in floor:
    # {
        print(unit + ", ", end='')
    # }

    print()  # Move to the next floor

# }

'''

***** BONEYARD *****

'''