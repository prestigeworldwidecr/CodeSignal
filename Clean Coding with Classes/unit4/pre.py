'''

Welcome to another lesson in our Clean Code in Python course! In previous lessons, we've delved into foundational concepts like the Single Responsibility Principle, encapsulation, and constructors, which are all crucial for writing clear, maintainable, and efficient code. In this lesson, we'll focus on implementing inheritance wisely in Python. By understanding the role of inheritance in Python's object-oriented programming, we'll learn how to use it effectively to enhance code readability and organization while adhering to the principles of clean code.

Inheritance is a powerful feature in object-oriented programming, including Python, that allows for code reuse and logical organization. It enables developers to create a new class based on an existing class, inheriting its properties and behaviors. When used appropriately, this can lead to more streamlined and easier-to-understand code.

Code Reuse and Reduction of Redundancies: By creating subclasses that inherit from a base class, you can avoid duplicating code, making it easier to maintain and extend your application.
Improved Readability: Logical inheritance hierarchies can improve the clarity of your software. For instance, if you have a base class Vehicle, with subclasses Car and Motorcycle, the structure is intuitive and clarifies the role of each class.
Alignment with Previous Concepts: Inheritance should respect the Single Responsibility Principle and encapsulation. Each class should have a clear purpose and ensure that its data is protected, regardless of its position in the hierarchy.

To leverage inheritance effectively in Python, it's important to adhere to several best practices:

In some cases, favor composition over inheritance.: Sometimes, inheritance can lead to tightly coupled code. In such cases, composition (where a class includes instances of other classes) might be a better choice.
Clear and Stable Base Class Interfaces: Provide consistent and limited interfaces in base classes to prevent subclasses from overly relying on their internal implementations.
Avoid Deep Inheritance Hierarchies: Deep hierarchies can complicate the understanding and maintenance of code, making debugging and modification more challenging.
Common pitfalls include overusing inheritance to model relationships that might not fit an "is-a" relationship well and using inheritance for code sharing without considering logical organization.

The hierarchy is too deep, with Manager extending Employee, which extends Person.
The Person class having a work() method might be inappropriate because not every person works, making the base class less general.
The inheritance might be forced, where a Manager "is-a" Person, but having Employee as an intermediary might not be necessary.

Person no longer has a work() method, making it more general.
Employee now uses composition to include a Person object instead of inheriting from it. This simplifies the hierarchy.
Manager still inherits from Employee, maintaining a logical structure but with reduced complexity.

While we refactored the example to use composition instead of inheritance, it's important to understand both the advantages and potential drawbacks of this approach.

Flexibility: Composition provides greater flexibility by allowing you to modify the behavior of a class at runtime. You can easily switch out components and change behavior without altering class hierarchies.
Encapsulation: It enhances encapsulation by keeping classes focused on specific tasks, thus adhering to the Single Responsibility Principle more closely.
Simpler Hierarchies: Composition helps avoid deep inheritance hierarchies, making your codebase easier to understand and maintain.

Verbosity: Composing objects can lead to more verbose code, as you have to instantiate and manage multiple objects rather than using a straightforward hierarchy.
Complex Interactions: Managing interactions between composed objects can increase complexity. It might require additional mechanisms to ensure the components work together seamlessly.
Cohesion: If not designed carefully, composition can lead to poor cohesion if the responsibilities of the composed objects aren’t well-defined.
In summary, while composition can lead to cleaner and more maintainable code, it does require careful planning and design to avoid verbose or overly complex interactions. As always, the choice between inheritance and composition should be guided by the specific needs of your application and the principles of clean code.

One of the key advantages of inheritance is its ability to minimize code duplication, thereby promoting a DRY (Don't Repeat Yourself) codebase. By defining shared functionalities in a base class, you can significantly enhance the maintainability of your code. Let's explore this concept with examples.

By utilizing a BaseVehicle class, we encapsulate common logic, allowing Car and Motorcycle to inherit shared functionalities. This structure not only eliminates code duplication but also enhances readability and maintainability.

Implementing inheritance thoughtfully simplifies class hierarchies and aligns with clean code principles, making your software more intuitive and efficient.

In this lesson, we explored how to implement inheritance wisely to support clean code practices in Python. By favoring composition over inheritance when appropriate and ensuring clear, stable class designs, you can create more maintainable and understandable code.

Next, you'll have the opportunity to apply and solidify these principles with practice exercises. Remember, clean code principles extend beyond these lessons, and we encourage you to keep practicing and applying them in your Python programming endeavors.

'''

class Person :
# {
    def __init__(self, name, age) :
    # {
        self.name = name
        self.age = age
    # }

    def work(self) :
    # {
        print("Person working")
    # }

# }

class Employee(Person) :
# {
    def __init__(self, name, age, employee_id) :
    # {
        super().__init__(name, age)
        self.employee_id = employee_id
    # }

    def file_taxes(self) :
    # {
        print("Employee filing taxes")
    # }

# }

class Manager(Employee) :
# {
    def hold_meeting(self):
    # {
        print("Manager holding a meeting")
    # }

# }

# The initial deep inheritance hierarchy
manager = Manager(name = "Alice", age = 40, employee_id = 1001)
manager.work()  # Inherits work() method from Person, which might be inappropriate
manager.file_taxes()
manager.hold_meeting()

class Person :
# {
    def __init__(self, name, age) :
    # {
        self.name = name
        self.age = age
    # }

# }

class Employee :
# {
    def __init__(self, person_details, employee_id) :
    # {
        self.person_details = person_details
        self.employee_id = employee_id
    # }

    def file_taxes(self) :
    # {
        print(self.person_details.name, "filing taxes")
    # }

# }

class Manager(Employee) :
# {
    def hold_meeting(self) :
    # {
        print(self.person_details.name, "holding a meeting")
    # }

# }

# The refactored, composition-based structure
person = Person(name = "Alice", age = 40)
employee = Employee(person_details = person, employee_id = 1001)
manager = Manager(person_details = person, employee_id = 1001)
manager.file_taxes()
manager.hold_meeting()

class Car :
# {
    def __init__(self, make, model, year) :
    # {
        self.make = make
        self.model = model
        self.year = year
    # }

    def start_engine(self) :
    # {
        print("Starting the engine of the", self.make, self.model)
    # }

    def open_trunk(self) :
    # {
        print("Opening the trunk of the", self.make, self.model)
    # }

# }

class Motorcycle :
# {
    def __init__(self, make, model, year) :
    # {
        self.make = make
        self.model = model
        self.year = year
    # }

    def start_engine(self) :
    # {
        print("Starting the engine of the", self.make, self.model)
    # }

    def pop_wheelie(self) :
    # {
        print("Popping a wheelie on the", self.make, self.model)
    # }

# }

# Example usage
car = Car(make = "Toyota", model = "Camry", year = 2023)
car.start_engine()
car.open_trunk()

motorcycle = Motorcycle(make = "Harley-Davidson", model = "Iron 883", year = 2023)
motorcycle.start_engine()
motorcycle.pop_wheelie()

class BaseVehicle :
# {
    def __init__(self, make, model, year) :
    # {
        self.make = make
        self.model = model
        self.year = year
    # }

    def start_engine(self) :
    # {
        print("Starting the engine of the", self.make, self.mode)
    # }

# }

class Car(BaseVehicle) :
# {
    def open_trunk(self) :
    # {
        print("Opening the trunk of the self.make", self.model)
    # }

# }

class Motorcycle(BaseVehicle) :
# {
    def pop_wheelie(self) :
    # {
        print("Popping a wheelie on the", self.make, self.model)
    # }

# }

# Example usage
car = Car(make = "Toyota", model = "Camry", year = 2023)
car.start_engine()
car.open_trunk()

motorcycle = Motorcycle(make="Harley-Davidson", model="Iron 883", year=2023)
motorcycle.start_engine()
motorcycle.pop_wheelie()

'''

***** BONEYARD *****

'''