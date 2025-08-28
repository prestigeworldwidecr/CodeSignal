'''

Ready to put your skills to the test, Space Voyager? Let's enhance your learning adventure with HashMaps. Your mission is to manage a library's inventory by adding code to update the stock of an existing book and to check if a new book is already available. Utilize your understanding of HashMaps to complete this mission!

'''

# Maintain a simple inventory of books in a library using a HashMap

library_inventory = {
                    "BookA": 3,
                    "BookB": 5,
                    "BookC": 2
                    } # Existing books

library_inventory["BookD"] = 4 # Adding a new book with its initial count

# TODO: Update the stock for 'BookA' by adding 2 more to its current count
library_inventory["BookA"] = library_inventory["BookA"] + 2

# TODO: Check if 'BookB' is in the inventory and print its stock count. 
# If it's not available, print "[Book Name] is not in stock."
if ("BookB" in library_inventory) :
# {
    print(library_inventory["BookB"])
# }

else :
# {
    print("BookB is not in stock.")
# }

'''

***** BONEYARD *****

'''