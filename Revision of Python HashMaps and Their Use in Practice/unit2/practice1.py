'''

You've learned how to efficiently count occurrences of each book genre in a library using Python dictionaries. Now, let's practice finding a more concise method for counting books. The goal is to make your code more concise and efficient by utilizing the skills you've learned and possibly discovering something new along the way!

Good effort, but this isn't the most efficient way. The goal is to count each genre in a single pass using a dictionary, as shown in the lesson.

Want to give it another shot, or need a hint?

c
4:27 AM
my solution runs faster
Cosmo
4:27 AM
Read message aloud
Interesting observation! What makes you think your solution is faster?
Can you compare the number of operations each approach performs for every book in the list?


c
4:28 AM
because yours checks each item in books. mine only runs for each book, not duplicated
Cosmo
4:28 AM
Read message aloud
Great thinking! Both solutions actually loop through every book in the list exactly once—so both have 
O
(
n
)
O(n) time complexity.

The difference is in how the dictionary is updated:

Your original code checks if the book is in the dictionary, then updates or adds it.
The more concise version uses get() to fetch the current count (or 0 if not present), then adds 1.
Both approaches do a dictionary lookup and update for each book. Can you spot any other differences between them?


c
7:18 AM
firstly, books_no_dups = set(books)
secondly, books_dict[book] = books.count(book)
Cosmo
7:18 AM
Read message aloud
Nice! That’s a creative approach.
But let’s think about efficiency:

What is the time complexity of books.count(book) inside a loop?
How many times will books.count(book) run if you do it for every unique book?
Try to estimate the total number of operations for your method compared to the single-pass dictionary approach.


c
1:12 PM
books.count(book) has time complecity O(1)
books.count(book) will run once for every book, not every instance of the book within books[]
Cosmo
1:12 PM
Read message aloud
Actually, books.count(book) is not 
O
(
1
)
O(1)—it’s 
O
(
n
)
O(n) because it scans the entire list each time to count occurrences.

So, if you run books.count(book) for every unique book (let’s say 
k
k unique genres), the total time complexity becomes 
O
(
k
⋅
n
)
O(k⋅n).
The single-pass dictionary approach is 
O
(
n
)
O(n), which is more efficient, especially as the list grows.

Does that make sense? Want to try rewriting your code using the more efficient method

'''

# Python program based on the scenario of counting books in a library
books = ["mystery", "sci-fi", "mystery", "fantasy", "sci-fi", "romance"]
books_dict = {}
# books_no_dups = set(books)

for book in books :
# {
    # books_dict[book] = books.count(book)
    books_dict[book] = books_dict.get(book, 0) + 1
# }

# color_dict[color] = color_dict.get(color, 0) + 1

print(books_dict)

'''

***** BONEYARD *****

# print()


    if (book in books_count) :
    # {
        books_count[book] = books_count[book] + 1
    # }

    else:
    # {
        books_count[book] = 1
    # }

'''