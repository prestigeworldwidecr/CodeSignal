'''

Alright, ready for the next galaxy-level challenge? Here it is, hot off the spaceship!

Let's imagine you've discovered a list of intergalactic treasures represented by integers in an array arr. Now, you've got a peculiar rule out here in the cosmos: you can only pick up the treasures located at the even indexes in that array! Now, being a smart space explorer, you want to find out the net worth of all these even-indexed treasures.

So, here's your mission: craft a Python function recursiveSumEven that accepts your list-of-integers treasure array as a parameter and returns the sum of all those even-indexed treasures. And since this is the cosmos and peculiar rules rule, you'll need to calculate this sum recursively!

This function will be tested with different-sized lists, including ones with 0 elements, so do consider the edge cases! Sail high, space champion! Remember, the answer is always in the journey.

'''

def recursiveSumEven(arr, idx = 0) :
# {
    # implement this

    if (idx >= len(arr)) :
    # {
        return 0
    # }

    # even
    elif (idx % 2 == 0):
    # {
        if (idx <= len(arr) - 1) :
        # {
            return arr[idx] + recursiveSumEven(arr, idx + 1)
        # }

        else :
        # {
            return 0
        # }
        
    # }

    # odd
    elif (idx % 2 == 1):
    # {
        # return "odd"
        return recursiveSumEven(arr, idx + 1)
    # }

    else :
    # {
        None
    # }

# }

# Testing the function
print(recursiveSumEven([1, 2, 3, 4, 5, 6])) # Expected output: 9
# print(recursiveSumEven([2, 3])) # Expected output: 2
# print(recursiveSumEven([])) # Expected output: 0

'''

********
BONEYARD
********

Base Case: What should the function return when the index idx is beyond the length of the array? This is where you stop the recursion.

Recursive Case:

Check if the current index is even. If it is, add the value at that index to the result of the recursive call.
Move to the next index by calling the function recursively with idx + 1.
How would you implement these steps in your function? 🐾

Let's refine your approach a bit:

Base Case: If idx is greater than or equal to the length of the array, return 0. This means you've processed all elements.

Recursive Case:

Check if idx is even. If it is, add the value at arr[idx] to the result of the recursive call with idx + 1.
If idx is odd, simply call the function recursively with idx + 1 without adding the current element.
Here's a hint: You don't need to check if the array length is even or odd. Focus on the index instead. How can you adjust your code to reflect this logic? 🐾

# print("!", arr, idx)
# print("#", arr, idx, arr[idx])
            # return arr[idx] + recursiveSumEven(arr, idx + 2)
            # return result
# print("@", arr, idx)


    
    elif (len(arr) == 0) :
    # {
        return 0
    # }

'''