'''

Welcome to the first practical exercise on meaningful naming! In this task, we’ll focus on improving the clarity of method and variable names. The current code includes names that do not clearly reveal their purpose, making the code difficult to understand. Your task is to refactor the given code by renaming methods and variables to better represent their roles. The functionality should remain the same, but the code will become easier to read and maintain.

This simple code checks if a number is even or odd. Let's enhance the code by making the names more descriptive!

'''

def isEven(num) :
# {
    return num % 2 == 0
# }


def main() :
# {
    num = 4
    parity_str = isEven(num)

    if (parity_str) :
    # {
        parity_str = "Even"
    # }

    else :
    # {
        parity_str = "Odd"
    # }

    print("The number is:", parity_str)
# }

if __name__ == "__main__" :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD*****

# res = "Even" if e(n) else "Odd"

'''