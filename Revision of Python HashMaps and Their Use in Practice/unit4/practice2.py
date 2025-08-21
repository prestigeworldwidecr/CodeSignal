'''

Great work on managing the library system! Now, let's test your skills in spotting a subtle bug. It appears there is an issue when attempting to display book information by its ID. Can you identify and resolve it to ensure the book details are correctly printed? Analyze the code and perform the necessary correction. Remember, the devil is in the details.

'''

# Initializing a library catalog HashMap with book details
library_catalog = {
                    "001": {"title": "Wonder",
                            "author": "R.J. Palacio",
                            "year_published": 2012
                            },

                    "002": {"title": "Charlotte\"s Web",
                            "author": "E.B. White",
                            "year_published": 1952}
                }

# Function to display book information by ID
def show_book_info(book_id) :
# {
    if book_id in library_catalog :
    # {
        print(library_catalog[book_id])
    # }

    else :
    # {
        print("Book not found in the library catalog.")
    # }

# }

# Display the info for book ID '001'
show_book_info("001")

'''

'''