'''

Hello and welcome to the lesson on Dependency Management between Classes! In our journey toward writing clean code, we've explored various aspects of class collaboration and the use of abstract base classes. Now, we're going to delve into managing dependencies — a crucial part of ensuring your code remains maintainable and testable. By understanding and effectively managing dependencies, you'll be able to write cleaner and more modular code that stands the test of time.

In the realm of object-oriented programming, dependencies refer to the relationships between classes where one class relies on the functionality of another. When these dependencies are too tightly coupled, any change in one class might necessitate changes in many others. Let's examine a simple example:

In this example, the Car class is directly dependent on the Engine class. Any modification to Engine might require changes in Car, highlighting the issues with tightly coupled code. It's essential to maintain some level of decoupling to allow more flexibility in code maintenance.

Tightly coupled code, like in the example above, leads to several problems:

Reduced Flexibility: Changes in one module require changes in dependent modules.
Difficult Testing: Testing a class in isolation becomes challenging due to its dependencies.
Increased Complexity: The more interdependencies, the harder it is to anticipate the ripple effect of changes.
This Python code snippet illustrates a potential solution using dependency injection:

By decoupling the Car class from directly instantiating the Engine, dependency injection allows the Car to be more adaptable to change. This means that different Engine implementations can easily be injected into the Car, promoting reuse and flexibility without requiring modifications to the Car code. Additionally, in testing scenarios, dependency injection enables the use of mock or dummy Engine objects, facilitating isolated testing of the Car class's functionality without being dependent on the actual Engine behavior.

One key strategy is adhering to the Dependency Inversion Principle (DIP), a core tenet of SOLID principles, which suggests:

High-level modules should not depend on low-level modules: For instance, a Car class should rely on an Engine abstraction rather than a specific engine type like GasEngine, allowing flexibility in engine interchangeability without affecting the Car.
Abstractions should not depend on details: For example, an Engine abstraction should not assume the details of a GasEngine implementation, thereby allowing various engine types to adhere to the same abstraction without constraining them to specific operational details.
This principle can be illustrated in Python using abstract base classes or duck typing:

The Car class can now utilize any implementation of Engine without being tightly coupled to a specific one. This enhances testing and future-proofs your design.

To manage dependencies effectively, consider these best practices:

Use Abstract Base Classes: Design your classes to depend on abstractions rather than concrete implementations.
Apply Design Techniques: Techniques such as factory functions or composition can assist in reducing dependencies. For instance, a factory function can be employed for creating objects, thereby reducing direct dependencies:

Leverage Constructor Injection: Utilizing constructor arguments for dependency injection increases testability and reduces coupling.

Effective dependency management is best demonstrated through practical applications. Consider the shift in a Python application where introducing abstract base classes and using dependency injection reduced testing times by 30% and enhanced code flexibility.

Imagine using the code before and after refactoring for dependency management:

Before Refactoring: Directly creates instances within classes, leading to tightly-coupled code.
After Refactoring: Uses factory functions and achieves loose coupling through dependency injections.

In this lesson, we've tackled the concept of dependency management, a pivotal factor in writing clean, maintainable, and flexible code. You are now equipped with the knowledge to identify and resolve dependency issues using principles and patterns like Dependency Inversion and Dependency Injection. The practice exercises that follow will offer you the chance to apply these concepts hands-on, strengthening your ability to manage class dependencies effectively in your projects. Happy coding!

'''

class Engine :
# {
    def start(self) :
    # {
        print("Engine starting...")
    # }

# }

class Car :
# {
    def __init__(self) :
    # {
        self.engine = Engine()  # Direct dependency
    # }

    def start(self) :
    # {
        self.engine.start()
    # }

# }

class Car :
# {
    def __init__(self, engine) :
    # {
        self.engine = engine  # Dependency injection
    # }

    def start(self) :
    # {
        self.engine.start()
    # }

# }

from abc import ABC, abstractmethod

class Engine(ABC) :
# {
    @abstractmethod
    def start(self) :
    # {
        None
    # }

# }

class GasEngine(Engine) :
# {
    def start(self) :
    # {
        print("Gas engine starting...")
    # }

# }

class Car :
# {
    def __init__(self, engine: Engine) :
    # {
        self.engine = engine  # Dependency injection
    # }

    def start(self) :
    # {
        self.engine.start()
    # }

# }

from abc import ABC, abstractmethod

class Engine(ABC) :
# {
    @abstractmethod
    def start(self) :
    # {
        None
    # }

# }

class GasEngine(Engine) :
# {
    def start(self) :
    # {
        print("Gas engine starting...")
    # }

# }

class ElectricEngine(Engine) :
# {
    def start(self) :
    # {
        print("Electric motor powering up...")
    # }

# }

class EngineFactory :
# {
    @staticmethod
    def create_engine(engine_type: str) -> Engine :
    # {
    
        if (engine_type == "gas") :
        # {
            return GasEngine()
        # }
        
        elif (engine_type == "electric") :
        # {
            return ElectricEngine()
        # }

        else :
        # {
            raise ValueError("Invalid engine type")
        # }

    # }

# }

class Car :
# {
    def __init__(self, engine_type: str) :
    # {
        self.engine = EngineFactory.create_engine(engine_type)
    # }

    def start(self) :
    # {
        self.engine.start()
    # }

# }

# Example usage
gas_car = Car("gas")
electric_car = Car("electric")

gas_car.start()      # Output: Gas engine starting...
electric_car.start() # Output: Electric motor powering up...

'''

***** BONEYARD *****

'''