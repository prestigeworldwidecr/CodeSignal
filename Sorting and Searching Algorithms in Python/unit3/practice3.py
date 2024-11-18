'''

Excellent work, Galactic Pioneer coder! You have been doing an amazing job exploring binary search with continuous functions. However, there seems to be an issue that requires your attention.

Your fellow cosmonauts onboard a different spaceship are attempting to find the root of the function 
f
(
x
)
=
x
6
−
3
x
4
+
4
x
3
−
1
f(x)=x 
6
 −3x 
4
 +4x 
3
 −1 using binary search. It appears there is an issue with the code, and they're seeking your help to debug it.

The current output doesn't observe the constraints and goals that were set for calculations. Are you prepared to aid them and debug the issue?

'''

# Python program to find the value of 'x' when f(x) = 0 using Binary Search
import math
import numpy as np

# Define a continuous function 'f' where f(x) = x^6 - 3x^4 + 4x^3 - 1
def f(x) :
# {
    return x**6 - 3 * x**4 + 4 * x**3 - 1
# }

# Binary Search Function
def binary_search(func, target, left, right, epsilon) :
# {
    middle = (left + right) / 2
    
    # while right - left > epsilon :
    while np.abs(func(left)) > epsilon and np.abs(func(right)) > epsilon and np.abs(func(middle) - target) > epsilon:
    # {
        middle = (left + right) / 2

        if (func(middle) < target) :
        # {
            left = middle
        # }

        else :
        # {
            right = middle  
        # }

    # }
           
    return middle

# }

epsilon = 1e-6  # to make sure the solution is within an acceptable range
target = 0  # target f(x) value
start = -5  # starting point of the interval
end = 5  # ending point of the interval

result = binary_search(f, target, start, end, epsilon)
print("The value of x for which f(x) is approximately 0 is:", result)

'''

********
BONEYARD
********

'''