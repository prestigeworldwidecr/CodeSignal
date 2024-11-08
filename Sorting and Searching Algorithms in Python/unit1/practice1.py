'''

You are whooshing in with a brain-bender, spacetrooper! Have you ever heard about the Fibonacci sequence, starting with 0 and 1, each number being the sum of the preceding two? Now, imagine blasting off from 2 and 3 instead, isn't that galactic? In this task, I want you to construct a function that takes an integer n and parachutes back with the n-th number in our ship-shaped Fibonacci sequence. Just a tiny reminder: your indexing starts at 0, and the function must return the n-th element in the sequence.

Watch out for the black holes, Galactic Pioneer! The input n can be any integer from 0 and onwards, and the output should be a single integer, the n-th element in our turbocharged Fibonacci sequence. Remember, no fear! I believe in you, Voyager! Keep reaching for the stars!

'''

def fib (n, computed = {0: 0, 1: 1}) :
# {
    if n not in computed :
    # {
        computed[n] = fib(n - 1, computed) + fib(n - 2, computed)
    # }

    else :
    # {
        None
    # }

    return computed[n]

# }

def alt_fib(n) :
# {
    # implement this
    result = fib (n + 3, computed = {0: 0, 1: 1})
    
    return result
# }

# Test the function with some values
print(alt_fib(0))  # Expected output: 2
print(alt_fib(1))  # Expected output: 3
print(alt_fib(2))  # Expected output: 5
print(alt_fib(3))  # Expected output: 8
print(alt_fib(4))  # Expected output: 13
print(alt_fib(5))  # Expected output: 21

'''

********
BONEYARD
********

'''