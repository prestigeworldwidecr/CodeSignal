'''

Great job handling book counts! Now, let's make a slight tweak to the scenario. Imagine that a few new books have been added to the library, and your task is to update their counts. You need to fill in the missing code to accurately count these new additions. Ensure the output reflects the updated counts for a small set of new returns.

'''

# Create a dictionary to track the count of books in the library
book_counts = {}

# List of books returned to the library
returned_books = ["Mystery at the Mansion", "Space Odyssey", "Mystery at the Mansion", "Python Programming"]

# Loop through the returned_books list
for book in returned_books :
# {
    # TODO: Update book_counts with the right counts for each book
    book_counts[book] = book_counts.get(book, 0) + 1
# }

#     
# Output the dictionary with the count of books
print(book_counts)
# What changes do you see in the output?

'''

***** BONEYARD *****

'''