'''

Alright, partner, let's strap on our rocket boots and leap into the gravity field of recursion! Ever wonder how to make a big math problem into tiny bite-sized pieces? That's what we're fixing to do!

Imagine you have a list of positive integers, like [1, 2, 3]. Now, instead of wrestling with just one number, you're up against a whole squadron! I need you to whip up a function that uses recursion to calculate the factorial of each integer in the list.

Remember, the factorial function is defined by 
n
!
=
n
⋅
(
n
−
1
)
⋅
(
n
−
2
)
⋅
.
.
.
⋅
1
n!=n⋅(n−1)⋅(n−2)⋅...⋅1. And don't forget that 
0
!
=
1
0!=1.

Your function should take this list as input and return a new list with the factorials in the same order as the original numbers. For example, given [2, 3, 4] as input, your function should spit out [2, 6, 24] since 2! equals 2, 3! equals 6, and 4! equals 24.

Note, that the input can include any numbers, even negative, and your code should correctly handle them.

Start up your thrusters, and let's see what you can do!

Bonus points: Try to think about how to apply the memorization technique here to avoid recursive calculations for the same inputs.

'''

def factorial(num) :
# {
    # implement this

    if (num < 0) :
    # {
        return None
    # }

    elif (num == 0 or num == 1) :
    # {
        return 1
    # }

    else :
    # {
        return num * factorial(num - 1)
    # }

# }

def factorials(nums) :
# {    
    result = []

    for num in nums :
    # {
        if (factorial(num) is not None) :
        # {
            result.append(factorial(num))
        # }

        else :
        # {
            result.append("Error")
        # }

    # }

    return result
    
    # return [factorial(num) if factorial(num) is not None else 'Error' for num in nums]
# }

# print(factorials([2, 3, 4])) # should print: [2, 6, 24]
# print(factorials([1, 5, 6])) # should print: [1, 120, 720]
print(factorials([0, -3, 10])) # should print: [1, 'Error', 3628800]

'''

********
BONEYARD
********

# print('!', num)

'''