'''

In this task, we’re going to improve the way Book objects are created by refactoring the constructor to handle a cleaner, more flexible initialization process.

Currently, the constructor for the Book class requires a large number of parameters, which can be difficult to manage. You will need to refactor this by grouping related data into separate classes (such as Author and Publisher) to simplify the constructor and improve maintainability.

'''

class Book :
# {
    def __init__(self, title, year, genre, price, aut, pbl) :
    # {
        self.title = title
        self.year = year
        self.genre = genre
        self.price = price
        self.publisher = pbl
        self.author = aut
    # }

# }

class Author :
# {
    def __init__(self, author_name, author_email) :
    # {
        self.author_name = author_name
        self.author_email = author_email
    # }

# }

class Publisher :
# {
    def __init__(self, publisher_name, publisher_address) :
    # {
        self.publisher_name = publisher_name
        self.publisher_address = publisher_address
    # }

# }

def main() :
# {
    # TODO: Replace direct instantiation with a builder pattern or refactor constructor
    # None
    aut1 = Author("J.K. Rowling", "jk.rowling@example.com")
    pub1 = Publisher("Bloomsbury Publishing", "50 Bedford Square, London")
    book1 = Book("Harry Potter and the Philosopher's Stone", 1997, "Fantasy", 39.99, aut1, pub1)

    print("Book Title:", book1.title)
    print("Year:", book1.year)
    print("Genre:", book1.genre)
    print("Price:", book1.price)
    print("Author:", book1.author.author_name)
    print("Author Email:", book1.author.author_email)
    print("Publisher:", book1.publisher.publisher_name)
    print("Publisher Address:", book1.publisher.publisher_address)
# }

if (__name__ == "__main__") :
# 
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

class Builder :
    # {
        def __init__(self, title, year, genre, price) :
        # {
            self.title = title
            self.year = year
            self.genre = genre
            self.price = price
            self.author = None
            self.publisher = None
        # }
        

def __init__(self, title, author_name, author_email, publisher_name, publisher_address, year, genre, price):
    # {
        # TODO: Consider grouping author and publisher details into separate classes to simplify the constructor
        self.title = title
        self.author_name = author_name
        self.author_email = author_email
        self.publisher_name = publisher_name
        self.publisher_address = publisher_address
        self.year = year
        self.genre = genre
        self.price = price
    # }

def __str__(self) :
    # {
        print(self)
        
        return ("Book Title:", self.title, "Author:", self.author_name +
                "Publisher:", self.publisher_name, "Year:", str(self.year) +
                "Genre:", self.genre, "Price: ", str(self.price))
    # }

book = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "jk.rowling@example.com",
                "Bloomsbury Publishing", "50 Bedford Square, London", 1997, "Fantasy", 39.99)
    
    print(book)

'''