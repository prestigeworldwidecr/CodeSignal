'''

Perfect work! You have reached the final stage of an intense journey unraveling binary search with continuous functions. Now, it's time to apply your acquired skills in the real world!

Your mission is as follows: Implement binary search on the function 
f
(
x
)
=
x
3
−
5
x
2
+
5
f(x)=x 
3
 −5x 
2
 +5 to find the value of 
x
x in the interval 
[
2
,
5
]
[2,5] such that 
f
(
x
)
=
0
f(x)=0. Please ensure you use a precision of 
1
0
−
6
10 
−6
  when defining your binary search.

Remember, binary search can help us find an approximate root of a continuous function within a given interval. Therefore, you should implement the necessary function and perform the base setup of the binary search. Your mission begins when the actual binary search starts. Good luck, Space Voyager!

'''

# Python program to find the value of 'x' when f(x) = 0 using Binary Search on Continuous Space
import math
import numpy as np

# Define a continuous function 'f'
def f(x) :
# {
    return x ** 3 - 5 * x ** 2 + 5
# }

# TODO: Write the Binary Search Function that performs the search on the continuous function in the interval [2, 5]
def binary_search(func, target, left, right, epsilon) :
# {
    # middle = (left + right) / 2
    
    while right - left > epsilon :
    # while np.abs(func(left)) > epsilon and np.abs(func(right)) > epsilon and np.abs(func(middle) - target) > epsilon:
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

# TODO: Define precision, target value, and interval bounds
precision = 1e-6
target = 0
interval = [2, 5]

# TODO: Implement the binary search function and print out the value of 'x' for which f(x) is approximately 0.
result = binary_search(f, target, interval[0], interval[1], precision)
print(result)

'''

********
BONEYARD
********

'''