'''

Welcome to the first practical task on the Law of Demeter! In this exercise, you'll work on improving object interactions within a small program. The current code violates the Law of Demeter by allowing methods to access objects indirectly. Your task is to refactor the code so that each method interacts only with its direct components, resulting in a more maintainable and less tightly coupled codebase.

The given program models a library system where a library can check out a book for a user. Your specific tasks include:

Refactoring the Library Class: Ensure that the Library class only interacts with objects it knows directly. Avoid accessing the internal properties of a Book or User object externally. The Library should request the User to handle the borrowing process.

Encapsulating User Behavior: The User class should manage its own state and activities, such as borrowing a book. It should not expose details of its internal state to other classes. Ensure that the User class has a method that allows the Library to instruct it to borrow a book without accessing internal details like the user's name.

Encapsulating Book Details: The Book class should provide its title through a method and not allow direct access to its attributes. This prevents other classes from becoming dependent on its internal structure.

'''

# from abc import ABC, abstractmethod

class Library() :
# {
    def check_out_book(self, user, book_title) :
    # {
        book = Book(book_title)
        user.check_out_book(book)
    # }

# }

class User() :
# {
    def __init__(self, name) :
    # {
        self._name = name
    # }

    def get_username(self) :
    # {
        return self._name
    # }

    def check_out_book(user, book) :
    # {
        print(user.get_username(), "borrowed", book.get_book_title())
    # }

# }

class Book(Library) :
# {
    def __init__(self, title) :
    # {
        self._title = title
    # }

    def get_book_title(self) :
    # {
        return self._title
    # }

# }

def main() :
# {
    user = User("John Doe")
    # book = Book("Python Programming")
    library = Library()
    library.check_out_book(user, "Python Programming")
# }

if (__name__ == "__main__") :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

def get_name(self) :
    # {
        return self._name
    # }

def check_out_book(self, user, book_title) :
    # {
        book = Book(book_title)
        # print(user.get_name(), "borrowed", book.title)
    # }    

    
    def get_title() :
    # {
        return title
    # }

def __init__(self) :
    # {
        # self._book = book
        None
    # }

    def check_out_book(self, user, book) :
    # {
        print('!')
        None
    # }    

'''