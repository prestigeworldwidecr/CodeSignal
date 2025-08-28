'''

You've practiced with examples; now, it's time to test your skills in managing a library catalog using HashMaps. Let's create a Library Management System where you check if a specific book is available. Remember how HashMaps can greatly simplify such tasks? Use your knowledge to complete this challenge!

'''

# Suppose you're tasked with checking the availability of a book by its ID in a library

# TODO: Define a 'library_catalog' dictionary with a few books. Each book should have id as key and details like title, author, and year_published as values
library_catalog = {
                    "book1" : {
                                "title" : "title1",
                                "author" : "author1",
                                "year_published" : 2001
                                }, 

                    "book2" : {
                                "title" : "title2",
                                "author" : "author2",
                                "year_published" : 2002
                                }, 

                    "book3" : {
                                "title" : "title3",
                                "author" : "author3",
                                "year_published" : 2003   
                                }
                }

# TODO: Assign a variable 'book_id' with an id you want to check
book_id = "book3"

# TODO: Write an if-else statement to check if the book_id exists in the library_catalog and print the book details or a message saying "Book not found in the library catalog."
if (book_id in library_catalog) :
# {
    print(library_catalog[book_id])
# }

else :
# {
    print("Book not found in the library catalog.")
# }

'''

***** BONEYARD *****

'''