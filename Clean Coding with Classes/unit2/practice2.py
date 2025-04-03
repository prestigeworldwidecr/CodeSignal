'''

In the previous task, we improved encapsulation for a BankAccount class. Now, let’s further explore and apply clean coding principles by addressing poor object design and cohesion.

In this exercise, we have a Rectangle class that exposes its width and height openly, allowing any part of the program to modify these properties arbitrarily, which can potentially lead to inconsistencies.

Your task is to refactor the code so that these properties are properly managed with encapsulation and incorporate methods to provide a cohesive interface for calculating the area and perimeter of the rectangle. Additionally, ensure that the constructor checks for non-negative width and height, raising a ValueError if either is negative.

'''

class Rectangle :
# {
    def __init__(self, width, height) :
    # {
        self._width = width
        self._height = height
        # width(width)
        # height(height)
    # }

    @property
    def width(self) :
    # {
        return self._width
    # }

    @property
    def height(self) :
    # {
        return self._height
    # }

    @width.setter
    def width(self, value) :
    # {
        if (value < 0) :
        # {
            raise ValueError("Width cannot be less than zero")
        # }

        else :
        # {
            self._width = value
        # }

    # }

    @height.setter
    def height(self, value) :
    # {
        if (value < 0) :
        # {
            raise ValueError("Width cannot be less than zero")
        # }

        else :
        # {
            self._height = value
        # }

    # }

    def area(self) :
    # {
        return self._width * self._height
    # }

    def perimeter(self) :
    # {
        return 2 * (self._width + self._height)
    # }

# }

def main() :
# {
    rectangle = Rectangle(5.0, 3.0)
    print("Width:", rectangle.width)
    print("Height:", rectangle.height)
    print("Area:", rectangle.width * rectangle.height)
    print("Perimeter:", 2 * (rectangle.width + rectangle.height))
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