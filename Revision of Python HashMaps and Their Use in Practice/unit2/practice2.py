'''

You're tasked with creating a system to keep track of book copies in the library. However, after implementing your code, you notice the output is not what you expected. Can you determine what went wrong and fix it? Ensure the program accurately counts each book's copies.

'''

# Create a dictionary to count the copies of books in a library
book_dict = {}

# List of books to count
books = ["The Hobbit", "The Hobbit", "The Lion King", "The Hobbit", "Cinderella"]

# Counting the number of each book in the list
for book in books :
# {
    book_dict[book] = book_dict.get(book, 0) + 1
# } 

# Print the dictionary to see how many copies of each book we have
print(book_dict)

'''

***** BONEYARD *****

'''