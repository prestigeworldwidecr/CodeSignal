"""

Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

Example

For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = false.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer yourLeft

A non-negative integer representing the heaviest weight you can lift with your left arm.

Guaranteed constraints:
0 ≤ yourLeft ≤ 20.

[input] integer yourRight

A non-negative integer representing the heaviest weight you can lift with your right arm.

Guaranteed constraints:
0 ≤ yourRight ≤ 20.

[input] integer friendsLeft

A non-negative integer representing the heaviest weight your friend can lift with his or her left arm.

Guaranteed constraints:
0 ≤ friendsLeft ≤ 20.

[input] integer friendsRight

A non-negative integer representing the heaviest weight your friend can lift with his or her right arm.

Guaranteed constraints:
0 ≤ friendsRight ≤ 20.

[output] boolean

true if you and your friend are equally strong, false otherwise.

"""

def solution(yourLeft, yourRight, friendsLeft, friendsRight) :
# {
    you = [yourLeft, yourRight]
    friend = [friendsLeft, friendsRight]

    if (max(you) == max(friend) and min(you) == min(friend)) :
    # {
        return True
    # }

    else :
    # {
        return False
    # }

# }


yourLeft = 10
yourRight = 15
friendsLeft = 15
friendsRight = 10
# For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be solution(yourLeft, yourRight, friendsLeft, friendsRight) = true

print(solution(yourLeft, yourRight, friendsLeft, friendsRight))

"""

********
BONEYARD
********

# max(yourLeft, yourRight)
# print(max(you), max(friend))
# if (True) :

"""