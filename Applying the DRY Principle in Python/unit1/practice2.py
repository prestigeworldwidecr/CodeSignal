'''

In this engaging task, we will further reinforce our understanding of the DRY principle by focusing on variable extraction. We'll enhance the maintainability of the code by extracting the hardcoded PI values into a single global constant.

The current code involves calculations related to a circle, where the value of PI is hardcoded multiple times with varying precision. Your task is to refactor the code by introducing a constant for PI, thereby eliminating redundant code and making the logic clear and consistent.

This exercise will help you understand how centralizing a common constant value can significantly enhance the clarity and maintainability of your code.

'''

import math # math.pi

def main() :
# {
    radius = 5.0

    print("Circumference:", calculate_circumference(radius))
    print("Area:", calculate_area(radius))
# }

def calculate_circumference(radius) :
# {
    # return 2 * 3.14159 * radius
    return 2 * math.pi * radius
# }

def calculate_area(radius) :
# {
    # return 3.1415926535 * radius * radius
    return math.pi * math.pow(radius, 2)
# }

if __name__ == "__main__":
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