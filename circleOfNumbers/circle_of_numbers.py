"""

Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
solution(n, firstNumber) = 7.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

A positive even integer.

Guaranteed constraints:
4 ≤ n ≤ 20.

[input] integer firstNumber

Guaranteed constraints:
0 ≤ firstNumber ≤ n - 1.

[output] integer

"""

def circle_of_numbers(n, first_number) :
# {
    diameter = n / 2
    result = None

    if (first_number < diameter):
    # {
        result = first_number + diameter
    # }

    elif (first_number >= diameter) :
    # {
        result = first_number - diameter
    # }

    else :
    # {
        None
    # }

    return result

# }

def solution(n, first_number) :
# {
    return circle_of_numbers(n, first_number)
# }

# For n = 10 and firstNumber = 2, the output should be solution(n, firstNumber) = 7.
n = 10
first_number = 2

# print(solution(n, first_number))

"""

********
BONEYARD
********


"""