'''

Welcome to the second lesson of the "Clean Coding with Classes" course! Previously, we focused on creating single-responsibility classes, highlighting how a singular focus improves readability and maintainability. Today, we'll delve into an essential concept in object-oriented design — encapsulation. Encapsulation plays a crucial role in creating clean, organized, and manageable code. Mastering it in Python will elevate your ability to write robust and maintainable software.

Here’s why encapsulation is beneficial:

Simplified Maintenance: By hiding implementation details, you can change an object's internal workings without affecting the external code, as long as the public interface remains stable.
Preventing Misuse: Encapsulation allows for control over data access and modification through defined interfaces (e.g., methods), reducing the likelihood of improper use of data.
Enhanced Security: By managing access to an object's data through defined interfaces, encapsulation helps prevent unauthorized data manipulation or access.
Without proper encapsulation, an object's internal state might be directly accessible and modifiable, leading to several issues:

Inconsistent States: Directly accessible attributes can be modified unexpectedly, leading to invalid states.
Reduced Maintainability: Lack of control over attribute access can cause unintended side effects throughout the codebase.
Difficult Debugging: Problems caused by shared mutable states can be tricky to diagnose and fix.
Understanding encapsulation in Python will empower you to design classes that are resilient, reliable, and aligned with clean coding principles.




'''

# Let’s examine a poor example of Python encapsulation:
class Book :
# {
    def __init__(self) :
    # {
        self.title = None
        self.author = None
        self.price = None
    # }

# }

# Usage
book = Book()
book.title = "Clean Code"
book.author = "Robert C. Martin"
book.price = -10.0  # This doesn't make sense for a price

'''
The attributes title, author, and price are publicly accessible and can be modified directly from outside the class. This allows invalid data states, such as a negative price, which should be avoided.
This lack of control over the object's data highlights encapsulation issues that can lead to larger problems in complex systems.
'''

'''

Prefix with Underscore: Attributes such as _title, _author, and _price are now intended for internal use only. This is a convention that signals these attributes are "protected" and should not be accessed directly from outside the class.

Getter and Setter Using @property: The @property decorator is used to define getter methods for attributes like title, author, and price. These methods allow controlled access to the internal state of the object.

The @price.setter Decorator: The @price.setter decorator ensures that whenever the price attribute is modified, it is checked for validity. If the value is negative, an error is raised.

Constructor: The constructor now accepts valid values, and it is more robust due to the controlled access provided by the getter and setter methods.

In many programming languages, it's common to use explicit getter and setter methods (e.g., get_price(), set_price()). However, Python offers a more elegant and idiomatic solution through the use of properties. Here’s why properties are preferable:

Cleaner Syntax: Properties allow you to access attributes as if they were regular attributes, not methods. This makes the syntax cleaner and more intuitive. Instead of writing book.get_price(), you can simply access book.price. This reduces boilerplate code and makes the interface simpler and more Pythonic.

Encapsulation: Properties allow you to hide the implementation details (like how the data is stored) while still exposing a clean, simple interface. The @property decorator lets you define methods for attribute access while maintaining the appearance of regular attribute access.

Readability: When using properties, the code reads more naturally, as attributes are accessed directly without the need for additional method calls. This enhances code readability and aligns with Python's philosophy of simplicity.

Flexibility: With properties, you can easily modify how an attribute is accessed in the future (e.g., add validation or computation) without changing the external interface of the class. This makes your code more flexible and future-proof.

Follow Naming Conventions: Use underscores to signal the intended access level of attributes and methods.
Utilize Properties: Use properties to control access to class attributes and maintain data integrity.
Minimize Public Interface: Only expose necessary methods and attributes to maintain a clean and minimal interface.
By following these practices, your Python code will be clean, maintainable, and robust.



'''

class Book :
# {
    def __init__(self, title, author, price) :
    # {
        self._title = title
        self._author = author
        self._price = price
    # }

    @property
    def title(self) :
    # {
        return self._title
    # }

    @property
    def author(self) :
    # {
        return self._author
    # }

    @property
    def price(self) :
    # {
        return self._price
    # }

    @price.setter
    def price(self, price) :
    # {
        if (price >= 0) :
        # {
            self._price = price
        # }

        else :
        # {
            raise ValueError("Price cannot be negative")
        # }

    # }

# }

# Usage
book = Book("Clean Code", "Robert C. Martin", 10.0)

class Book :
# {
    def get_price(self) :
    # {
        return self._price
    # }

    def set_price(self, value) :
    # {
        if (value >= 0) :
        # {
            self._price = value
        # }

        else :
        # {
            raise ValueError("Price cannot be negative")
        # }

    # }

# }

book = Book("Clean Code", "Robert C. Martin", 10.0)
price = book.get_price()
book.set_price(20.0)

class Book :
# {
    @property
    def price(self) :
    # {
        return self._price
    # }

    @price.setter
    def price(self, value) :
    # {
        if (value >= 0) :
        # {
            self._price = value
        # }

        else :
        # {
            raise ValueError("Price cannot be negative")
        # }

    # }

# }

book = Book("Clean Code", "Robert C. Martin", 10.0)
price = book.price  # No need to call a method
book.price = 20.0  # No need to call a setter method explicitly

'''

***** BONEYARD *****

'''