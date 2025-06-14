'''

Welcome to the third lesson of the "Clean Coding with Classes" course! 🎓 As we continue our journey, we've already covered key concepts like the Single Responsibility Principle and Encapsulation. In this lesson, we'll focus on Constructors and Object Initialization, which are essential for creating clean and efficient Python applications. By the end of this lesson, you'll understand how to write __init__ methods that contribute to clean, maintainable code.

The __init__ method in Python is fundamental for initializing objects in a known state, thereby enhancing code maintainability and readability. This method encapsulates the logic of object creation, ensuring that each object starts its life correctly. A well-written __init__ method can significantly reduce complexity, making the code easier to understand and manage. By clearly stating what an object's dependencies are, it aids in maintaining flexibility and facilitating easier testing.

Common problems with the __init__ method include excessive parameters, hidden dependencies, and complex initialization logic. These issues can lead to convoluted, hard-to-maintain code. To tackle these problems, consider the following Python-specific solutions:

Use @classmethod: This decorator allows for alternative constructors, managing complex initialization scenarios.
Helper Functions: Create functions that encapsulate complex object creation logic, providing clear entry points for instantiation.
Dependency Declaration: Ensure dependencies are clearly stated when initializing objects, reducing hidden dependencies.
Each of these strategies contributes to cleaner, more understandable code by simplifying the initialization process and clarifying object dependencies.

Adopting best practices for the __init__ method can vastly improve your code quality:

Keep Initialization Simple: The __init__ method should only set up the object, avoiding complex logic.
Use Descriptive Parameter Names: This aids in understanding what each parameter represents.
Limit the Number of Parameters: Too many parameters can complicate the __init__ method's use. Consider using keyword arguments or data classes if you have more than three or four parameters.
Ensure Valid Initialization: Make sure that objects are initialized in a valid state, avoiding the need for further configuration or checks.
These practices lead to cleaner, more focused initialization methods that are easy to understand and maintain.

Complex Initialization Logic: The __init__ method does too much by parsing a string and initializing multiple fields, making it hard to follow and maintain.
Assumes Input Format: Relies on a specific data format, leading to potential errors if the input structure changes.
Lacks Clarity: It's not immediately clear what data format data_string should be in, leading to confusion.

Simplified Initialization: The __init__ method now simply assigns values without complex logic, making it easier to understand.
Class Method Factory: from_string provides a clear, separate method for parsing, preserving __init__ simplicity. The @classmethod decorator signifies that from_string is associated with the class itself, using cls to refer to the class for creating instances.
Flexibility: Allows for easier changes if data parsing needs updating without altering the __init__ method.

Having too many arguments in a constructor is a red flag. If a constructor requires a long list of parameters, it's often a sign that the class is trying to do too much or that it lacks a clear responsibility. This can make the code harder to read, understand, and maintain.

This constructor has seven parameters, which can become difficult to manage. In this case, it may be beneficial to refactor the class by grouping related data into objects.

Grouped Arguments: We have now reduced the number of parameters by grouping related data (e.g., customer information, payment details) into separate classes. This reduces complexity and makes the code easier to manage.

Improved Readability and Maintainability: The Order class is now cleaner, and each class has a clear responsibility. If we need to modify payment methods or customer details, we can do so independently without affecting the Order class.

Best Practice: A constructor should not require too many arguments. If a class needs many parameters, consider grouping related data into objects, dictionaries, or data classes. This will make your code more readable and easier to maintain.

When a class has too many constructor parameters, it can make object creation cumbersome and error-prone. The Builder Pattern offers a solution by allowing complex objects to be created step by step, with more control over the process.

In the following example, we demonstrate how the Builder Pattern simplifies the creation of a Pizza object that requires multiple attributes, such as size, toppings, and crust type.

Too Many Parameters: The constructor takes multiple parameters, which makes it harder to understand and use correctly.
Order of Arguments: It's easy to pass the parameters in the wrong order, leading to potential bugs.
Lack of Flexibility: Adding new attributes, like sauces or extras, would require changing the constructor directly.

To address these issues, we can refactor the Pizza class by using the Builder Pattern. The builder class will handle the creation of the Pizza object step by step, making the code more flexible and readable.

Improved Readability: The builder provides a clear, step-by-step way to configure the Pizza object.
Fluent Interface: The add_topping method allows for toppings to be added in a readable and intuitive manner.
Flexibility and Maintainability: New attributes like sauces or extras can be added without changing the constructor, making the code easier to extend and maintain.
Error Prevention: The builder pattern prevents errors related to the order of arguments in the constructor.
Optional Parameters Handling: The builder pattern allows you to set only the necessary parameters for a Pizza object, like size and crust type, while toppings can be added as optional attributes using methods like add_topping, enhancing flexibility and customization.

In this lesson, we explored the importance of the __init__ method and object initialization in writing clean, maintainable Python code. Key takeaways include simplifying initialization methods, clearly defining dependencies, and avoiding complex logic inside __init__. We also discussed handling too many constructor arguments and how the Builder Pattern can offer a solution for complex object creation. As you move on to the practice exercises, apply these principles to solidify your understanding and improve your ability to write clean, efficient Python code. Good luck! 🚀

'''

class UserProfile :
# {
    def __init__(self, data_string) :
    # {
        data = data_string.split(',')
        self.name = data[0]
        self.email = data[1]
        # Assumes age can be parsed and address is in a specific position
        self.age = int(data[2])
        self.address = data[3]
    # }

# }

data_string = "John Doe,john.doe@example.com,30,1234 Elm Street"
user_profile = UserProfile(data_string)

# Accessing attributes of the created object
print(user_profile.name)  # Output: John Doe
print(user_profile.email)  # Output: john.doe@example.com
print(user_profile.age)  # Output: 30
print(user_profile.address)  # Output: 1234 Elm Street

class UserProfile :
# {
    def __init__(self, name, email, age, address) :
    # {
        self.name = name
        self.email = email
        self.age = age
        self.address = address
    # }

    @classmethod
    def from_string(cls, data_string) :
    # {
        data = data_string.split(',')
        return cls(data[0], data[1], int(data[2]), data[3])
    # }

# }

# Example of using the from_string class method to create a UserProfile object
data_string = "John Doe,john.doe@example.com,30,1234 Elm Street"
user_profile = UserProfile.from_string(data_string)

# Accessing attributes of the created object
print(user_profile.name)  # Output: John Doe
print(user_profile.email)  # Output: john.doe@example.com
print(user_profile.age)  # Output: 30
print(user_profile.address)  # Output: 1234 Elm Street

class Order :
# {
    def __init__(self, order_id, customer_name, items, shipping_address, payment_method, discount, total_price):
    # {
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.shipping_address = shipping_address
        self.payment_method = payment_method
        self.discount = discount
        self.total_price = total_price
    # }

# }

class Order :
# {
    def __init__(self, order_id, customer, items, payment_details) :
    # {
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.payment_details = payment_details
    # }

# }

class Customer :
# {
    def __init__(self, name, address, email) :
    # {
        self.name = name
        self.address = address
        self.email = email
    # }

# }

class PaymentDetails :
# {
    def __init__(self, method, discount) :
    # {
        self.method = method
        self.discount = discount
    # }

# }

customer = Customer(name = "Alice Smith", address = "1234 Maple Drive", email = "alice.smith@example.com")

# List of items in the order
items = ["Notebook", "Pen", "Calculator"]

# Create PaymentDetails object
payment_details = PaymentDetails(method = "Credit Card", discount = 10)

# Create Order object using the customer, items, and payment details
order = Order(order_id = 123456, customer = customer, items = items, payment_details = payment_details)

# Accessing and printing the Order object's attributes
print("Order ID:", order.order_id)
print("Customer Name:", order.customer.name)
print("Customer Address:", order.customer.address)
print("Customer Email:", order.customer.email)
print("Items: ", ', '.join(order.items))
print("Payment Method:", order.payment_details.method)
print("Discount:", order.payment_details.discount, '%')

class Pizza :
# {
    def __init__(self, size, crust_type, toppings) :
    # {
        self.size = size
        self.crust_type = crust_type
        self.toppings = toppings
    # }

# }

# Creating a pizza object
pizza = Pizza("Large", "Thin Crust", ["Cheese", "Pepperoni", "Olives"])

class Pizza :
# {
    def __init__(self, builder) :
    # {
        self.size = builder.size
        self.crust_type = builder.crust_type
        self.toppings = builder.toppings
    # }

    class Builder :
    # {
        def __init__(self, size, crust_type) :
        # {
            self.size = size
            self.crust_type = crust_type
            self.toppings = []  # Default: No toppings
        # }

        def add_topping(self, topping) :
        # {
            self.toppings.append(topping)
            return self
        # }

        def build(self) :
        # {
            return Pizza(self)
        # }

    # }

# }

# Using the builder to create a pizza object
pizza = (Pizza.Builder("Large", "Thin Crust")
         .add_topping("Cheese")
         .add_topping("Pepperoni")
         .add_topping("Olives")
         .build())

# Accessing the pizza object attributes
print("Pizza Size:", pizza.size)  # Output: Large
print("Crust Type:", pizza.crust_type)  # Output: Thin Crust
print("Toppings:", ', '.join(pizza.toppings))  # Output: Cheese, Pepperoni, Olives

'''

***** BONEYARD *****

'''