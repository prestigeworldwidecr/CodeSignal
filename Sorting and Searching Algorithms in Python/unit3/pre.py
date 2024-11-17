'''

Introduction
Hello everyone, and welcome back to another exciting lesson! Today, we embark on an intriguing journey of applying the binary search algorithm, which we have thoroughly covered in previous lessons, to continuous functions. This lesson aims to spark your curiosity and expand your understanding of the binary search algorithm. It will provide new insight on how to determine a specific function value within a continuous interval. This approach broadens the application of binary search from discrete space to continuous functions. So, let's unravel this exciting topic together!

Understanding Continuous Functions
Before we dive into binary search and continuous functions, let's refresh our understanding of what exactly continuous functions are. In the simplest terms, a function is a mapping from an input (or set of inputs) to an output. For instance, if we think about a Python function, it takes one or more arguments and returns an output based on the logic embedded within the function.

Continuous functions are those that produce a smooth, unbroken output for a continuous range of inputs without any abrupt changes or gaps. In mathematical terms, a function 
f
(
x
)
f(x) is continuous at a point 
x
=
a
x=a if the limit of 
f
(
x
)
f(x) as 
x
x approaches 
a
a from the left is equal to the limit of 
f
(
x
)
f(x) as 
x
x approaches 
a
a from the right, and these values are equal to 
f
(
a
)
f(a). That means that:

lim
⁡
x
→
a
−
f
(
x
)
=
lim
⁡
x
→
a
+
f
(
x
)
=
f
(
a
)
x→a 
−
 
lim
​
 f(x)= 
x→a 
+
 
lim
​
 f(x)=f(a)
​
  
​
 
Where 
lim
⁡
x
→
a
−
f
(
x
)
lim 
x→a 
−
 
​
 f(x) and 
lim
⁡
x
→
a
+
f
(
x
)
lim 
x→a 
+
 
​
 f(x) represent the limit of 
f
(
x
)
f(x) as 
x
x approaches 
a
a from the left and the right, respectively.

For example, in real life, the function that relates the time of day to the temperature outside is continuous (although it may go up and down). It's a natural phenomenon that temperature doesn't make abrupt jumps.

Why is this property important to us? Well, remember that for binary search, the elements must be sorted, i.e., arranged in some order. Although continuous functions might not be sorted in the traditional sense (like a list of integers), they still maintain order due to their 'continuity'. This property allows us to apply the binary search algorithm to them.

Binary Search Recap
You might recall from previous lessons that binary search is a powerful search algorithm with a logarithmic running time. It searches a sorted list by repeatedly dividing the search interval in half. In each step, it compares the middle element with the target item. If the middle element matches the target item, its position in the list is returned. However, if the target item is greater than the middle element, the search continues on the right half of the list and vice versa.

But how does all this apply to a continuous function? Well, the mechanism of binary search remains much the same, but instead of comparing the middle element to the target, we compare the middle point 
x
x's function value 
f
(
x
)
f(x) to the target. We continuously narrow down an interval until we reach an interval small enough that the function value within it is as close to the target as we demand.

Finding the Function Value with Binary Search
Now, let's lay out the steps for finding a specific function value using binary search. The spirit of the methodology is similar to that of searching a discrete list, but there are some key differences:

We define the left and right bounds of the binary search. These should be an interval [left, right) within which the function takes on our target value.
We define a loop that runs until the difference between left and right is smaller than a very small number 
ϵ
ϵ (called the precision of our search).
Within that loop, we compute the midpoint: m = (left + right) / 2.
We then compute the function value at m, f(m). If f(m) is less than the target value, we update left to m. Otherwise, we update right to m.
The loop continues until we achieve the required precision, and the function value within the final interval [left, right) is close enough to the target that we accept it as the sought value.
Let's stress-test our understanding with a hands-on example. Consider the continuous function 
f
(
x
)
=
x
2
−
2
f(x)=x 
2
 −2, and let's try to find 
x
x for which 
f
(
x
)
=
0
f(x)=0, within the interval [1, 2].

Implications of Precision
Throughout our binary search function, we mentioned a precision value 
ϵ
ϵ, which we set as a very small number (
1
0
−
6
10 
−6
  in our case). It's introduced to achieve the desired accuracy in our result. The smaller the 
ϵ
ϵ, the higher the precision of our target value since we are narrowing down the interval width to a smaller range. However, this comes with a trade-off. A smaller 
ϵ
ϵ means that our while loop will run more times, and thus, the algorithm will take longer to reach the desired precision level. This challenge presents an exciting optimization problem but is beyond the scope of this lesson.

Applying the Technique to a Complex Problem
With this newly acquired knowledge, we open up a vast range of possibilities to solve complex problems. For example, suppose we need to solve a problem in physics where we need to determine at which time 
t
t, the velocity function 
V
(
t
)
=
9.81
∗
t
−
0.65
∗
t
2
V(t)=9.81∗t−0.65∗t 
2
  of an object equals a certain target value within a given time range. We can discretize the time and check every second, but a more efficient solution could be derived using a binary search, where the left bound is 0, the right bound is t, and the target is the target velocity. Such use cases show that with a sound understanding of binary search and continuous functions, we are equipped to solve a whole new array of complex problems.

Wrapping up
That brings us to the end of this exciting lesson. We leaned into binary search, expanding our understanding by seeing its application to continuous functions for determining a specific function value within an interval. We revisited the unique nature of continuous functions, figured out how binary search can be adapted to work with them, and discussed the significance of precision and its implications on binary search. Finally, we decoded a Python implementation of binary search on continuous functions and discussed how to extend this technique to solve more complex real-life problems.

'''

# Define the function
def f(x) :
# {
    return x * x - 2
# }

# Define the binary search function 
def binary_search(target, left, right, precision) :
# {
    while right - left > precision :
    # {
        mid = (left + right) / 2

        # If the midpoint value is less than the target...
        if f(mid) < target :
        # {
            # ...update the left boundary to be the midpoint.
            left = mid  
        # }

        else:
        # {
            # Otherwise, update the right boundary.
            right = mid 
        # }

    # }

    return left # Return the left boundary of our final, narrow interval.
# }

epsilon = 1e-6
result = binary_search(0, 1, 2, epsilon)

print("x for which f(x) is approximately 0:", result)

# Outputs:
# x for which f(x) is approximately 0: 1.4142131805419922
# This code prints an 
# x
# ≈
# 2
# x≈ 
# 2
# ​
#  , demonstrating how binary search can find function values in continuous space.

'''

********
BONEYARD
********

'''