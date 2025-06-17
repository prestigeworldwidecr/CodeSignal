'''

Welcome to the second lesson of the "Clean Code with Multiple Classes" course! In the previous lesson, we explored how to enhance class design and manage code smells effectively. Today, we'll delve into Abstract Base Classes (ABCs) in Python, which play crucial roles in crafting clean, maintainable applications. Abstract Base Classes help define clear structures within your code, promoting organization and scalability by establishing a framework for further development.

In Python, Abstract Base Classes (ABCs) are a way to define a contract for derived classes. They specify which methods a class must implement, providing guidance without enforcing a specific implementation. This approach allows for flexibility while ensuring consistency in behavior across different classes.

Let's consider a simple example using the abc module:

In this example, PaymentProcessor is an abstract base class that defines the process_payment method as abstract. Any class inheriting this ABC must provide its own implementation for this method. This structure allows different payment processors, like a CreditCardProcessor, to be interchangeable within the codebase, adhering to the same contract.

Using ABCs promotes flexibility and scalability, as new types of payment processors can be added with minimal changes to the existing code.

Abstract Base Classes in Python cannot be instantiated directly. They allow for a mix of concrete and abstract methods, providing a common base of functionality while still enforcing certain methods that must be implemented by derived classes.

In this code, Animal is an abstract base class that provides a concrete implementation of the eat method while leaving the make_sound method abstract. The Dog class extends Animal and provides its own implementation of make_sound. This setup allows you to define shared behaviors (e.g., eat) while requiring derived classes to specify others (e.g., make_sound).

Using abstract base classes is advantageous when you want to provide shared functionality among related classes, reducing code duplication while maintaining flexibility.

Improper use of class structures can lead to messy code and poor design decisions. Issues such as rigid structures or excessive duplication often arise.

Let's address a common problem: a tightly coupled class hierarchy that makes it difficult to add new functionality. Here’s a poorly structured example:

In this design, the PaymentProcessor class has separate methods for different payment types, leading to a rigid and inflexible structure. Adding a new payment type would necessitate modifying this class to include an additional method.

By using an abstract base class, you can define a payment contract that enforces a consistent interface across all payment types:

Now, adding new payment options, like MobilePayment, becomes straightforward:

The abstract base class Payment ensures each payment method adheres to the same interface, fostering a readable and maintainable code structure. This approach reduces the complexity and rigidity of the original design, demonstrating clear advantages over a method-based implementation where each payment type has its separate function.

This usage example shows how the process_payment function can handle any object that follows the Payment interface, highlighting the flexibility and power of using abstract base classes alongside duck typing in Python.

Implementing Abstract Base Classes and utilizing Python's dynamic nature comes with best practices:

Keep Classes Focused: Design ABCs with a single responsibility, avoiding the temptation to include too many abstract methods in one class.

Design for Change: Design your class hierarchies to be adaptable and scalable for future changes or additions.
Favor Composition Over Inheritance: Use ABCs to compose behaviors over creating deep inheritance chains.

In this lesson, we explored the importance of Abstract Base Classes and Python's dynamic nature in constructing clean, maintainable code. By understanding when and how to use these, you can design flexible and scalable Python applications. Moving on, you'll encounter practice exercises designed to reinforce these concepts, allowing you to apply them in real-world scenarios and further solidify your skills in clean coding principles. Remember, the effective use of Abstract Base Classes can significantly enhance your ability to write clean, organized code. Happy coding!

'''

from abc import ABC, abstractmethod

# Abstract Base Class defining a contract
class PaymentProcessor(ABC) :
# {
    @abstractmethod
    def process_payment(self, amount):
    # {
        pass
    # }

# }

# Class implementing the abstract method
class CreditCardProcessor(PaymentProcessor) :
# {
    def process_payment(self, amount) :
    # {
        print("Processing credit card payment of $", amount)
    # }

# }

from abc import ABC, abstractmethod

# Abstract Base Class with both abstract and concrete methods
class Animal(ABC) :
# {
    def eat(self) :
    # {
        print("This animal is eating.")
    # }

    @abstractmethod
    def make_sound(self) :
    # {
        pass
    # }

# }

# Class extending the abstract base class
class Dog(Animal) :
# {
    def make_sound(self) :
    # {
        print("Bark!")
    # }

# }

class PaymentProcessor :
# {
    def pay_with_cash(self, amount) :
    # {
        print("Paying $", amount, " with cash")
    # }

    def pay_with_card(self, amount) :
    # {
        print("Paying $", amount, " with credit card")
    # }

# }

from abc import ABC, abstractmethod

class Payment(ABC) :
# {
    @abstractmethod
    def pay(self) :
    # {
        pass
    # }

# }

class CashPayment(Payment) :
# {
    def pay(self):
    # {
        print("Paying with cash")
    # }

# }

class CreditCardPayment(Payment) :
# {
    def pay(self):
    # {
        print("Paying with credit card")
    # }

# }

class MobilePayment(Payment) :
# {
    def pay(self, amount) :
    # {
        print("Paying $", amount, "with mobile payment")
    # }

# }

def process_payment(payment_method, amount):
# {
    payment_method.pay(amount)
# }

# This setup works due to duck typing; each class implements the same method signature.
process_payment(CashPayment(), 100)
process_payment(CreditCardPayment(), 150)
process_payment(MobilePayment(), 200)

'''

***** BONEYARD *****

'''