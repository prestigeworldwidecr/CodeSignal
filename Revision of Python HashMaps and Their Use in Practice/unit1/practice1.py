'''

You've mastered updating titles in our library catalog! For your next mini-challenge, switch things up by changing the library catalog: update the title for 'book3' to 'Little Women', instead of altering 'book1'. Keep the librarian spirit alive and let's refine our catalog!

'''

# Scenario: Library and book cataloging.

# Create a dictionary representing a small library catalog
library_catalog = {
                    "book1": "The Hobbit",
                    "book2": "The Catcher in the Rye",
                    "book3": "Pride and Prejudice"
                    }

# Update the title for "book1"
library_catalog["book1"] = "The Lord of the Rings"
library_catalog["book3"] = "Little Women"

# Print the updated library catalog
for book, title in library_catalog.items():
# {
    print(book, ':', title)
# }

'''

***** BONEYARD ***** 

'''