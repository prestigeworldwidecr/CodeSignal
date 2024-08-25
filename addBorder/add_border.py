"""

Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                     "*abc*",
                     "*ded*",
                     "*****"]
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.string picture

A non-empty array of non-empty equal-length strings.

Guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.

[output] array.string

The same matrix of characters, framed with a border of asterisks of width 1

"""

def addBorder(picture) :
# {
    # i = 0
    tmp = ""
    bottomTopBorder = "**"
    result = []
    
    for i in range(len(picture[0])) :
    # {
        bottomTopBorder = bottomTopBorder + "*"
    # }

    result.append(bottomTopBorder)

    for i in range(len(picture)) :
    # {
        tmp = "*" + picture[i] + "*"
        result.append(tmp)
    # }

    result.append(bottomTopBorder)
    
    return result
# }

def solution(picture) :
# {
    return addBorder(picture)
# }

picture = ["abc",
           "ded"] # the output should be

# solution(picture) = ["*****",
#                    "*abc*",
#                    "*ded*",
#                    "*****"]

print(solution(picture))

"""

********
BONEYARD
********

picture = ["abc",
            "ded"]

addBorder(picture)

// solution(picture) = ["*****",
//                      "*abc*",
//                      "*ded*",
//                      "*****"]

// console.log("i: ", picture[i])
    // console.log(result)

"""