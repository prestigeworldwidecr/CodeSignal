'''

You've learned how to count book copies in a library using a Python dictionary. Now it's your turn to efficiently track a collection of your favorite books. Remember, each book title in your collection can appear multiple times, and you want to know the total count for each.

'''

# Create and initialize a list 'books' with some duplicated book titles of your choice
# TODO: YOUR CODE HERE
books = ["book1", "book2", "book3", "book2", "book1"]

# Create an empty dictionary 'book_count' to store the count of each book
# TODO: YOUR CODE HERE
book_count = {}

# Loop through each book in the 'books' list
# TODO: Check if the book is already in dictionary, if so increment its count, otherwise add it with count 1
for book in books :
# {
    book_count[book] = book_count.get(book, 0) + 1
# }

# Finally, print the 'book_count' dictionary
# TODO: YOUR CODE HERE
print(book_count)

'''

***** BONEYARD *****

'''