'''

Welcome to the first task on managing class dependencies in Python! In this exercise, you'll explore decoupling by refactoring code that suffers from issues of tight coupling. The current code ties a Car class directly to a specific GasEngine, making future changes hard to implement. Your task is to refactor the code to allow the Car class to utilize any engine type through an abstract base class. This will significantly enhance the code's flexibility and testability.

'''

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

def main() :
# {
    car = Car(GasEngine())
    car.start()
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