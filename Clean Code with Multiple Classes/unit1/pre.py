'''

Welcome to the very first lesson of the "Clean Code with Multiple Classes" course! 🎉 This course aims to guide you in writing code that's easy to understand, maintain, and enhance. Within the broader scope of clean coding, effective class collaboration is crucial for building well-structured applications. In this lesson, we will delve into the intricacies of class collaboration and coupling — key factors that can make or break the maintainability of your software. Specifically, we'll address some common "code smells" that indicate problems in class interactions and explore ways to resolve them.

Let's dive into the challenges of class collaboration by focusing on four common code smells:

Feature Envy: Occurs when a method in one class is overly interested in methods or data in another class.
Inappropriate Intimacy: Describes a situation where two classes are too closely interconnected, sharing private details.
Message Chains: Refers to sequences of method calls across several objects, indicating a lack of clear abstraction.
Middle Man: Exists when a class mainly delegates its behavior to another class without adding functionality.
Understanding these code smells will enable you to improve your class designs, resulting in cleaner and more maintainable code.

These code smells can significantly impact system design and maintainability. Let's consider their implications:

They can lead to tightly coupled classes, making them difficult to modify or extend. 🔧
Code readability decreases, as it becomes unclear which class is responsible for which functionality.
Addressing these issues often results in code that's not only easier to read but also more flexible and scalable. Tackling these problems can markedly enhance software architecture, making it more robust and adaptable.

In this scenario, calculate_total_price() in ShoppingCart overly accesses data from Item, indicating feature envy.

To refactor, consider moving the logic to the Item class:

Now, each Item calculates its own total, reducing dependency and distributing responsibility appropriately. ✔️

Inappropriate Intimacy occurs when a class is overly dependent on the internal details of another class. Here's an example:

In this scenario, the Library class relies too heavily on the details of the Book class, demonstrating inappropriate intimacy. The key distinction between Inappropriate Intimacy and Feature Envy is that inappropriate intimacy involves a significant intertwining between two classes, while feature envy is about a method's excessive interest in another class's data or behavior instead of its own.

To refactor, allow the Book class to handle its own representation:

This adjustment enables Book to encapsulate its own details, encouraging better encapsulation and separation of concerns. 🛡️

Message Chains occur when classes need to traverse multiple objects to access the methods they require. Here's a demonstration:

The chain user.get_address().get_zip_code().get_postal_code() illustrates this problem.

To simplify, encapsulate the access within methods:

This adjustment makes the User class responsible for retrieving its postal code, creating a clearer and more direct interface. 📬

A Middle Man problem occurs when a class primarily exists to delegate its functionalities. Here's an example:

The Controller doesn't do much beyond delegating to Service.

To refactor, simplify delegation or reassign responsibilities:

By removing the unnecessary middle man, the design becomes more streamlined and efficient. 🔥

In this lesson, you've explored several code smells associated with suboptimal class collaboration and coupling, including Feature Envy, Inappropriate Intimacy, Message Chains, and Middle Man. By identifying and refactoring these smells, you can elevate your code's clarity and maintainability.

Get ready to put these concepts into practice with upcoming exercises, where you'll identify and refactor code smells, strengthening your skills. Keep striving for cleaner, more effective code! 🌟

'''

class ShoppingCart :
# {
    def __init__(self) :
    # {
        self.items = []
    # }

    def calculate_total_price(self) :
    # {
        total = 0

        for item in self.items :
        # {
            total = total + item.get_price() * item.get_quantity()
        # }

        return total
    # }

# }

class Item :
# {
    def __init__(self, price, quantity) :
    # {
        self.price = price
        self.quantity = quantity
    # }

    def get_price(self) :
    # {
        return self.price
    # }

    def get_quantity(self) :
    # {
        return self.quantity
    # }

# }

class ShoppingCart :
# {
    def __init__(self) :
    # {
        self.items = []
    # }

    def calculate_total_price(self) :
    # {
        total = 0

        for item in self.items :
        # {
            total = total + item.calculate_total()
        # }

        return total
    # }

# }

class Item :
# {
    def __init__(self, price, quantity) :
    # {
        self.price = price
        self.quantity = quantity
    # }

    def calculate_total(self) :
    # {
        return self.price * self.quantity
    # }

# }

class Library :
# {
    def __init__(self, book) :
    # {
        self.book = book
    # }

    def print_book_details(self) :
    # {
        print("Title:", self.book.get_title())
        print("Author:", self.book.get_author())
    # }

# }

class Book :
# {
    def __init__(self, title, author) :
    # {
        self.title = title
        self.author = author
    # }

    def get_title(self) :
    # {
        return self.title
    # }

    def get_author(self) :
    # {
        return self.author
    # }

# }

class Library :
# {
    def __init__(self, book) :
    # {
        self.book = book
    # }

    def print_book_details(self) :
    # {
        print(self.book.get_details())
    # }

class Book :
# {
    def __init__(self, title, author) :
    # {
        self.title = title
        self.author = author
    # }

    def get_details(self) :
    # {
        s = "Title:", self.title,
        "\nAuthor:", self.author

        return s
    # }

# }

class User :
# {
    def __init__(self, address):
    # {
        self.address = address
    # }

    def get_address(self) :
    # {
        return self.address
    # }

# }

class Address :
# {
    def __init__(self, zip_code) :
    # {
        self.zip_code = zip_code
    # }

    def get_zip_code(self) :
    # {
        return self.zip_code
    # }

# }

class ZipCode :
# {
    def __init__(self, postal_code) :
    # {
        self.postal_code = postal_code
    # }

    def get_postal_code(self) :
    # {
        return self.postal_code
    # }

# }

# Usage
user = User(Address(ZipCode("90210")))
postal_code = user.get_address().get_zip_code().get_postal_code()

class User :
# {
    def __init__(self, address) :
    # {
        self.address = address
    # }

    def get_user_postal_code(self) :
    # {
        return self.address.get_postal_code()
    # }

# }

class Address :
# {
    def __init__(self, zip_code) :
    # {
        self.zip_code = zip_code
    # }

    def get_postal_code(self) :
    # {
        return self.zip_code.get_postal_code()
    # }

# }

class ZipCode :
# {
    def __init__(self, postal_code) :
    # {
        self.postal_code = postal_code
    # }

    def get_postal_code(self) :
    # {
        return self.postal_code
    # }

# }

# Usage
user = User(Address(ZipCode("90210")))
postal_code = user.get_user_postal_code()

class Controller :
# {
    def __init__(self, service) :
    # {
        self.service = service
    # }

    def execute(self) :
    # {
        self.service.perform_action()
    # }

# }

class Service :
# {
    def perform_action(self) :
    # {
        # Action performed
        pass
    # }

# }

class Service :
# {
    def perform_action(self) :
    # {
        # Action performed
        pass
    # }

# }

# Usage
service = Service()
service.perform_action()

'''

***** BONEYARD *****

'''