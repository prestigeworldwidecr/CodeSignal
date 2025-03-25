'''

In this task, we will focus on utilizing Python's duck typing philosophy to create a flexible and adaptable design for shape objects. Duck typing allows us to write code that operates on objects regardless of their specific types as long as they implement the required behavior. You will be tasked with creating multiple shape classes that don't inherit from a common base class but still work together seamlessly through duck typing principles. Implement functions that can operate on any shape object to calculate the area and display information about the shape, outputting the shape class name and its area. This exercise emphasizes the use of duck typing to improve code adaptability and reduce dependencies on class hierarchies.

'''

from math import pi

class Circle :
# {
    def __init__(self, radius) :
    # {
        self.radius = radius
    # }

    def calculate_area(self) :
    # {
        return pi * self.radius * self.radius
    # }

# }


class Rectangle :
# {
    def __init__(self, width, height) :
    # {
        self.width = width
        self.height = height
    # }

    def calculate_area(self) :
    # {
        return self.width * self.height
    # }


    # TODO: Implement calculate_area to return the area if 'calculate_area' method exists.
    # Otherwise, raise an AttributeError.

    # TODO: Implement print_shape_info to print shape type and area if 'calculate_area' method exists.
    # Otherwise, raise an AttributeError.

# }

def print_shape_info(self) :
# {
    area = self.calculate_area()
    print(f"{self.__class__.__name__} - Area: {area}")    
# }

def main() :
# {
    c = Circle(7)
    r = Rectangle(5, 3)

    # TODO: Use print_shape_info for Circle to display class name and area
    if (hasattr(c, 'calculate_area')) :
    # {
        print_shape_info(c)
    # }

    else :
    # {
        raise AttributeError
    # }

    # TODO: Use print_shape_info for Rectangle to display class name and area
    if (hasattr(r, 'calculate_area')) :
    # {
        print_shape_info(r)
    # }
    
    else :
    # {
        raise AttributeError   
    # }

# }

if __name__ == "__main__" :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

try :
    # {
        area = self.calculate_area()
        print(f"{self.__class__.__name__} - Area: {area}")
    # }

    except AttributeError :
    # {
        raise AttributeError
    # }

    def print_shape_info(self) :
    # {
        try :
        # {
            area = self.calculate_area()
            print(f"{self.__class__.__name__} - Area: {area}")
        # }

        except AttributeError :
        # {
            raise AttributeError
        # }
        
    # }

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

'''