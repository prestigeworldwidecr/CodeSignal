'''

Just like how stars in the universe are numbered, we need your skills to arrange some numbers! Here's a list of decimal numbers, think of them as astronomical data. They've come down to us all willy-nilly, which doesn't make sense. You're going to write a function that sorts this cosmic data in ascending order. Use the Python built-in sorting mechanism, don't reinvent the wheel here!

The input format is pretty straightforward: you have a list of randomly generated decimal numbers. The output? A sorted list of those very numbers, in ascending order - smallest to biggest. No exceptions, even for edge cases or guarantees. It's space simple, right?

'''

def sort_list(values) :
# {
    # implement this
    return sorted(values)
# }

print(sort_list([22.7, 14.3, 90.8, 45.3, 77.2]))  # Expected output: [14.3, 22.7, 45.3, 77.2, 90.8]
print(sort_list([1, 5, 0.3, 7.6, 3.1, 100]))      # Expected output: [0.3, 1, 3.1, 5, 7.6, 100]
print(sort_list([45, 85, 33, 90.5, 29]))          # Expected output: [29, 33, 45, 85, 90.5]

'''

**********  BONEYARD  **********

'''