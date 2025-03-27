'''

In this exercise, we'll focus on enriching our code with comments for better clarity and understanding. The current code consists of a small class that contains a public function without any documentation. Your task is to add meaningful comments to provide clear guidance on how the function should be used.

The class represents a simple solver for quadratic equations of the form ax^2 + bx + c = 0. Let's enhance its usability by documenting its functionality with comments!

'''

import math

class SquareEquationSolver :
# {

    '''
    TODO: Add a docstring to this class
    Class returns the roots of a quadratic equation
    '''
    
    def solve_quadratic(self, a, b, c) :
    # {
        ''' 
        TODO: Add comments to this method
        method solves the quadratic equation ax^2 + bx + c = 0
        and returns the roots as a list
        '''

        roots = [None, None]
        discriminant = b * b - 4 * a * c    # b^2 - 4ac
        roots[0] = (-b + math.sqrt(discriminant)) / (2 * a) # +/- sqrt(b^2 - 4ac) / 2a
        roots[1] = (-b - math.sqrt(discriminant)) / (2 * a)
        return roots
    # }

# }

if (__name__ == "__main__") :
# {
    solver = SquareEquationSolver()
    roots = solver.solve_quadratic(1, -3, 2)
    print("Roots:", roots[0], roots[1])
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

# root2 = (-b - math.sqrt(discriminant)) / (2 * a)
# def solve_quadratic(self, a: float, b: float, c: float) -> list :

'''