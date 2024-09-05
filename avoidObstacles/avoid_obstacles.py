"""

You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.

Check out the image below for better understanding:


"""

def solution(inputArray) :
# {
    tmp = -1
    
    for i in range(len(inputArray)) :
    # {
        if (i > 0 and inputArray[i] % i == 1) :
        # {
            print(i, inputArray[i], inputArray[i] % i)
            tmp = i
        # }

        else :
        # {
            None
        # }

    # }

    return tmp

# }

# For inputArray = [5, 3, 6, 7, 9], the output should be solution(inputArray) = 4.

inputArray = [5, 3, 6, 7, 9]
# inputArray = [2, 3]
print(solution(inputArray))

"""

########
BONEYARD
########

# return inputArray

"""