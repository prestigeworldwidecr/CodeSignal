'''

Welcome to the final task of this unit! Let's put everything together and tackle a slightly more complex challenge. We have a Library class managing a list of books, but it currently exposes its internal book list directly to users. This is a significant encapsulation issue that makes the system prone to data integrity problems.

Your task is to refactor this code and solve these encapsulation violations by hiding the implementation details and providing a well-defined public interface for managing books. Let's ensure that the library only allows valid operations and robustly manages its collection of books!

Good try, but there's room for improvement. Your solution needs to encapsulate the book list by providing methods to add, remove, and list books, with checks for duplicates or invalid operations. Would you like some guidance on how to proceed? 

'''

class Library :
# {
    def __init__(self) :
    # {
        self._books = []
    # }

    @property
    def books(self) :
    # {
        return list(self._books)
    # }

    def add_book(self, value) :
    # {
        if (value == None) :
        # {
            raise ValueError("Title invalid")
        # }

        elif (value in self._books) :
        # {
            raise ValueError(value, "already in Library")
        # 

        else :
        # {
            self._books.append(value)
            # print(value, "added to Library")
        # }

    # }

    def remove_book(self, value) :
    # {
        if (value in self._books) :
        # {
            self._books.remove(value)
            # print(value, "removed from Library")
        # }

        else :
        # {
            raise ValueError(value, "not in library")
        # }

    # }

    def print_books(self) :
    # {
        print("Library Books:")

        for book in self.books :
        # {
            print(book)
        # }

    # }

# }

def main() :
# {
    library = Library()
    library.add_book("Design Patterns")
    library.add_book("Refactoring")
    library.remove_book("Design Patterns")

    # print(len(library.books))

    library.print_books()
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


    @books.setter
    def books(self, value) :
    # {
        self._books.append(value)
    # }

    @books.deleter
    def books(self) :
    # {
        self._books.remove(self.value)
    # }


# print_books

library.books.append("Clean Code")
    library.books.append("Design Patterns")
    library.books.append("Refactoring")
    library.books.remove("Design Patterns")

    print("Library Books:")

    for book_title in library.books :
    # {
        print(book_title)
    # }

'''