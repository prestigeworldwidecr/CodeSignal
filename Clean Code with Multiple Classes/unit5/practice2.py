'''

In this exercise, you will improve the readability and maintainability of a library system by refactoring its exception handling. The current implementation uses generic exceptions (Exception) for all error scenarios, making it harder to understand and debug.

Your goal is to replace these generic exceptions with meaningful custom exceptions that represent specific error conditions. This will align the code with Python's clean coding principles and make it more robust and easier to debug.

Current Issues

Overuse of Generic Exceptions: Generic exceptions are used for all errors, reducing clarity and debuggability.
Unclear Error Messages: The current error messages do not provide enough context for effective debugging.
Refactor the codebase to implement custom exceptions for the library system. These exceptions should make the error conditions clearer and improve the system's overall maintainability.

Requirements

Create Custom Exceptions:

BookNotAvailableException: Raised when a requested book is unavailable or cannot be updated.
BookNotFoundException: Raised when the specified book ID does not exist.
InvalidUserException: Raised when a user is invalid or unauthorized.
Propagate Exceptions with Context:

Use meaningful error messages to provide sufficient debugging context.
Preserve the original exception context where applicable.

'''

class BookNotAvailableException :
# {
    def __init__(self, book_id) :
    # {
        msg = str("Book:" + book_id + " not available")
        super().__init__(msg)
        self.book_id = book_id
    # }

# }

class BookNotFoundException :
# {
    def __init__(self, book_id) :
    # {
        msg = str("Book:" + book_id + " does not exist")
        super().__init__(msg)
        self.book_id = book_id
    # }
    
# }

class InvalidUserException :
# {
    def __init__(self, user_id) :
    # {
        msg = str("User:" + user_id + " does not exist")
        super().__init__(msg)
        self.user_id = user_id
    # }
    
# }

class BookRepository :
# {
    def is_book_available(self, book_id) :
    # {
        if book_id == "00000" :
        # {
            # raise Exception("Book not found")
            raise BookNotAvailableException(book_id)
        # }

        else :
        # {
            return True
        # }

    # }

    def is_valid_user(self, user_id) :
    # {
        if (user_id == "user1") :
        # {
            return True
        # }

        else :
        # {
            # raise Exception("Invalid user")
            raise InvalidUserException(user_id)
        # }

    # }

    def update_book_status(self, book_id, is_available) :
    # {
        if (book_id == "error") :
        # {
            # raise Exception("Update failed")
            raise BookNotFoundException(book_id)
        # }
        
        else :
        # {
            s = ""
            
            if (is_available) :
            # {
                s = "Available"
            # }

            else :
            # {
                s = "Not available"
            # }

            # print("Book status updated: {'Available' if is_available else 'Not available'}")
            print("Book status updated: " + s)
        # }
    
    # }

# }

class LibraryService :
# {
    def __init__(self) :
    # {
        self.book_repository = BookRepository()
    # }

    def borrow_book(self, book_id, user_id) :
    # {
        if (self.book_repository.is_book_available(book_id)) :
        # {
            None
        # }

        else :
        # {
            # raise Exception("Book is not available")
            raise BookNotAvailableException(book_id)
        # }

        if (self.book_repository.is_valid_user(user_id)) :
        # {
            None
        # }

        else :
        # {
            # raise Exception("User is not valid")
            raise InvalidUserException(user_id)
        # }

        self.book_repository.update_book_status(book_id, False)
        print("Book borrowed successfully!")


def main() :
# {
    library_service = LibraryService()

    try :
    # {
        library_service.borrow_book("12345", "user1")
    # }

    except Exception as e :
    # {
        print("Operation failed:", e)
    # }

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

'''