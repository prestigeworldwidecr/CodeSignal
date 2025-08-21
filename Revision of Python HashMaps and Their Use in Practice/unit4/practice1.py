'''

CosmoRead message aloud
In our library system, ensure that a book's copies are decremented only when copies are available. Modify the code to check if more than 0 copies are available before decreasing. This introduces a practical use of conditional expressions in real-world tasks.

'''

# HashMap to hold the library system
library_system = {}

# Example: Adding a book
library_system["978-3-16-148410-0"] = {
                                        "title": "The Little Prince",
                                        "author": "Antoine de Saint-Exupéry",
                                        "copies": 3
                                        }

# Example: Borrowing a book (decrementing the number of copies)
if (library_system["978-3-16-148410-0"]["copies"] > 0) :
# {
    library_system["978-3-16-148410-0"]["copies"] = library_system["978-3-16-148410-0"]["copies"] - 1  # Assuming the book is available
# }

else :
# {
    None
# }   

'''

***** BONEYARD *****

'''