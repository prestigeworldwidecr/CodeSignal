'''

Great job, Cosmic Coder! You've been effectively utilizing binary search on continuous functions — an interstellar effort indeed. Now, it's time to apply this proficiency to an intriguing real-world challenge. Let's imagine that you're an astronaut who brewed coffee at a temperature of 90 degrees, which transpires to be too hot to drink. Over time, as your coffee cools, its taste begins to change. At around 70 degrees, you notice your brew tastes optimal, yet you strive for precision. Recently, you had thought that the optimal temperature would be obtained when the value of the coffee function is 30, so now you're trying to understand which temperature maps to this coffee function value.

Should you choose to accept your mission, you will need to modify the starter code to pinpoint the exact temperature T at which your coffee tastes superior, i.e., coffee_function(T) = 30. At the point where the taste of the coffee peaks, you will find the optimal temperature.

Your objective: tweak the binary search function to identify this temperature. Good luck!

'''

# Python program to find the temperature at which a specific coffee type is approximated to be best
import math

# Define the continuous function for the specific coffee type  
def coffee_function(T) :
# {
    return - ((T - 85) ** 2) + 60
# }

# Define the binary search function 
def binary_search(func, target, left, right, precision) :
# {
    mid = (left + right) / 2

    while right - left > precision:
    # {
        mid = (left + right) / 2

        # TODO: Update `left` and `right` bounds based on the `func(mid)` value
        if func(mid) < target :
        # {
            right = mid
        # }

        else :
        # {
            left = mid
        # }
        
    # }

    return (left + right) / 2 
# }

# Requested precision
epsilon = 1e-6

# Identify the temperature range in which the coffee tastes the best 
temperature_range = [30, 100]

target = 30

# TODO: Find the exact temperature at which your coffee tastes best.
result = binary_search(coffee_function, target, temperature_range[0], temperature_range[1], epsilon) 

print("At the point where the taste of the coffee peaks, you will find the optimal temperature:", result)

'''

********
BONEYARD
********

'''