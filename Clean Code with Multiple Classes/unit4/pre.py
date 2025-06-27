'''

Welcome to the next lesson of the Clean Code with Multiple Classes course! This lesson is all about putting polymorphism into practice, building on the foundations laid in previous lessons, such as class collaboration, abstract base classes, and dependency management. Polymorphism is a cornerstone concept in object-oriented programming (OOP) that allows us to write more dynamic and flexible code. Today, we will explore its practical applications and how it can enhance code quality. Let's dive in!

Polymorphism in Python empowers developers to write flexible and scalable code. Rather than relying on explicit type declarations, Python embraces dynamic typing and duck typing, which allow objects to be treated according to their behavior.

Consider a scenario where you have multiple classes representing different types of payments: CreditCardPayment, PayPalPayment. By using polymorphism, you can treat these different payment types in a unified way:

By using a common method like pay, different payment methods can be handled through the concept of duck typing:

This example demonstrates the core benefit of polymorphism: the ability to write code that can work with objects of different classes in a unified manner. This flexibility reduces code duplication and makes it easy to add new payment types by simply ensuring they implement the required method without altering existing logic.

One of the recurring issues in software development is rigid code that's difficult to modify or extend. Polymorphism offers a way out by enabling more abstract and adaptive design patterns. Let's revisit a problem you might have seen before: a program littered with lengthy conditional logic to handle different behaviors based on object types.

For example, consider the following code without polymorphism:

In Python, duck typing helps eliminate such cumbersome conditional structures. Here's how the same functionality could be achieved using polymorphism:

By designing your classes to use polymorphism, you avoid lengthy conditional checks that can be error-prone and hard to maintain.

To effectively implement polymorphism in Python, leverage subclassing and duck typing. Let's revisit the payment example:

Python's flexibility allows you to add new payment methods with minimal changes, aligning with the Open/Closed Principle — modules are open for extension but closed for modification.

Understanding Python's method resolution order and dynamic typing will enhance your ability to create clean and adaptable code structures, promoting reuse and extension without rigid inheritance.

When implementing polymorphism, consider these practices to ensure effective and maintainable designs in Python:

Embrace Duck Typing: Trust that objects will correctly implement the necessary methods, without enforcing explicit type checks.

Favor Composition Over Inheritance: Although polymorphism often uses inheritance, prefer composition to share behavior across classes without rigid inheritance chains.

Keep Methods Consistent: Ensure methods that will be invoked polymorphically have consistent signatures and behaviors across classes.

By adhering to these practices, your code will be more adaptable and modular, allowing for easier modifications and additions.

While polymorphism provides significant advantages, improper use can lead to pitfalls. Here are common mistakes to avoid in Python:

Overusing Type Hints: Over-reliance on type hints can restrict the flexibility of dynamic typing. Use them judiciously to enhance readability without constraining polymorphism.

Ignoring Proper Abstractions: Failing to correctly abstract common behavior can result in bloated or redundant methods. Carefully design your methods to support polymorphic use.

Confusion Between Interface and Implementation: Make sure that method names and expected behaviors are consistently understood between different classes.

To sidestep these issues, ensure your classes have clear responsibilities, and test your code extensively to catch design flaws early.

Today, we've navigated the practical facets of polymorphism, linking back to concepts like subclassing and flexible design principles that you've learned throughout this course. The key takeaway is the power of polymorphic design in making your code flexible, maintainable, and adaptable. Now, it's time to put theory into action. Dive into the exercises ahead, where you will reinforce these concepts through hands-on coding. Remember, successful application of polymorphism requires experimentation and continuous refinement. Happy coding, and enjoy the challenge!

'''

from abc import ABC, abstractmethod

class Payment(ABC) :
# {
    @abstractmethod
    def pay(self) :
    # {
        None
    # }

# }

class CreditCardPayment(Payment) :
# {
    def pay(self) :
    # {
        print("Processing credit card payment.")
    # }

# }

class PayPalPayment(Payment) :
# {
    def pay(self):
    # {
        print("Processing PayPal payment.")
    # }

# }

def process_payment(payment):
# {
    payment.pay()
# }

# You can pass any object that has a pay method to process_payment.
payment = CreditCardPayment()
process_payment(payment)

def process_payment_details(payment_method) :
# {
    if (isinstance(payment_method, CreditCardPayment)) :
    # {
        # Process credit card payment
        None
    # }

    elif (isinstance(payment_method, PayPalPayment)) :
    # {
        # Process PayPal payment
        None
    # }
    
    else : 
    # {
        # More conditions...
        None
    # }

# }

def process_payment(payment) :
# {
    payment.pay()
# }

class BankTransferPayment(Payment) :
# {
    def pay(self) :
    # {
        print("Processing bank transfer payment.")
    # }

# }

'''

***** BONEYARD *****

'''