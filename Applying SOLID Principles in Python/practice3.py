'''

In this task, we will focus on implementing the Interface Segregation Principle. The existing code involves a Vehicle interface that combines functionalities needed by different types of vehicles, leading to unused and unnecessary method implementations. Your job is to refactor the code by breaking down this interface into smaller, more specific interfaces that cater to the needs of different types of vehicles.

The current setup complicates the class design by forcing unrelated functionalities onto different vehicle types. Let's streamline the interfaces and ensure that each vehicle implements only the methods relevant to its functionality

'''

# from abc import ABC, abstractmethod

class Car :
# {
    def drive(self) :
    # {
        print("Car is driving")
    # }

    def open_door(self) :
    # {
        print("Car door is opening")
    # }

# }

class Bicycle :
# {
    def pedal(self) :
    # {
        print("Bicycle is pedaling")
    # }

# }

def main() :
# {
    car = Car()
    car.drive()
    car.open_door()

    bicycle = Bicycle()
    bicycle.pedal()
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

    def pedal(self) :
    # {
        # Not applicable for Car
        pass
    # }

def drive(self) :
    # {
        # Bicycle doesn't drive like a car
        pass
    # }

    def open_door(self) :
    # {
        # Not applicable for Bicycle
        pass
    # }

    class Vehicle :
# {
    def drive(self) :
    # {
        None
    # }

    def open_door(self) :
    # {
        None
    # }

    def pedal(self) :
    # {
        None
    # }

# }

'''