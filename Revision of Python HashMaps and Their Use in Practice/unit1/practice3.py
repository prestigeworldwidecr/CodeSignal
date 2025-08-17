'''

Bravo for learning about dictionaries in Python! Now, let's test your knowledge. Your task is to check if a certain book exists in our library catalog. If it does, simply print "Book is available". If not, notify us that it's not in the catalog. Remember to use dictionary operations to accomplish this.

'''

# Library Catalog
library_catalog = {
                    "Moby Dick" : "Herman Melville",
                    "The Great Gatsby" : "F. Scott Fitzgerald"
                }

# TODO: Check if '1984' is in the library_catalog. If yes, print "Book is available". If no, print it's not in the catalog.

available = False

for title, author in library_catalog.items() :
# {
    if (title == "1984") :
    # {
        available = True
    # }

    else :
    # {
        None
    # }

# }

if (available) :
# {
    print("Book is available")
# }

else :
# {
    print("it's not in the catalog")
# }

'''

***** BONEYARD *****

# print(title)
        # print("Book is available")
        

'''