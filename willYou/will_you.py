"""

Once Mary heard a famous song, and a line from it stuck in her head. That line was "Will you still love me when I'm no longer young and beautiful?". Mary believes that a person is loved if and only if he/she is both young and beautiful, but this is quite a depressing thought, so she wants to put her belief to the test.

Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.

A person contradicts Mary's belief if one of the following statements is True:

they are young and beautiful but not loved;
they are loved but not young or not beautiful.
Example

For young = True, beautiful = True, and loved = True, the output should be
solution(young, beautiful, loved) = False.

Young and beautiful people are loved according to Mary's belief.

For young = True, beautiful = False, and loved = True, the output should be
solution(young, beautiful, loved) = True.

Mary doesn't believe that not beautiful people can be loved.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] boolean young

[input] boolean beautiful

[input] boolean loved

[output] boolean

True if the person contradicts Mary's belief, False otherwise.

"""

def boolean_to_binary(b) :
# {
    if (b == 0) :
    # {
        return 0
    # }

    else :
    # {
        return 1
    # }

# }

def will_you(young, beautiful, loved) :
# {
    binary = "" + str(boolean_to_binary(young)) + str(boolean_to_binary(beautiful)) + str(boolean_to_binary(loved))
    digit = int(binary, 2)

    match digit :
    # {
        case 0 :
            return False
        case 1 :
            return True
        case 2 :
            return False
        case 3 :
            return True
        case 4 :
            return False
        case 5 :
            return True
        case 6 :
            return True
        case 7 :
            return False
    # }

#}

def solution(young, beautiful, loved) :
# {
    return will_you(young, beautiful, loved)
# }

young = False
beautiful = False
loved = True

print(solution(young, beautiful, loved))

"""

********
BONEYARD
********

"""