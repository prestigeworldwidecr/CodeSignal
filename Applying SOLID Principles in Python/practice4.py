'''

In this task, let's explore the Dependency Inversion Principle from the SOLID principles!

The current code involves a printer system that directly interacts with specific printer implementations, leading to tight coupling. Your task is to refactor the code by introducing an abstraction that allows the printer system to depend not on concrete printer implementations but on an abstraction. This change will make the codebase more flexible and easier to extend or modify by promoting loose coupling.

The goal is to implement the Dependency Inversion Principle by refactoring the code to utilize interfaces where necessary, allowing different printer implementations to be swapped out without altering the printer system's code. Let's create a more modular design

'''

from abc import ABC, abstractmethod

class Printer(ABC) :
# {
    @abstractmethod
    def print(self, document) :
    # {
        None
    # }

# }

class InkjetPrinter(Printer) :
# {
    def print(self, document) :
    # {
        print(document)
    # }

# }

class LaserPrinter(Printer) :
# {
    def print(self, document) :
    # {
        print(document)
    # }

# }

class PrintManager :
# {
    def __init__(self, printer) :
    # {
        self.printer = printer
    # }

    def print(self, document) :
    # {
        self.printer.print(document)
    # }

# }

def main() :
# {
    manager = PrintManager(InkjetPrinter())
    manager.print("Inkjet Printing: Hello World!")
    manager = PrintManager(LaserPrinter())  
    manager.print("Laser Printing: Hello SOLID Principles!")
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

def __init__(self) :
    # {
        # self.inkjet_printer = InkjetPrinter()
        # self.laser_printer = LaserPrinter()
    # }

    def print_using_inkjet(self, document) :
    # {
        self.inkjet_printer.print(document)
    # }

    def print_using_laser(self, document) :
    # {
        self.laser_printer.print(document)
    # }

manager = PrintManager()
    manager.print_using_inkjet("Inkjet Printing: Hello World!")
    manager.print_using_laser("Laser Printing: Hello SOLID Principles!")    
    .

    print1 = InkjetPrinter()
    print2 = LaserPrinter()
    manager.print("Inkjet Printing: Hello World!")
    manager.print("Laser Printing: Hello SOLID Principles!")

'''