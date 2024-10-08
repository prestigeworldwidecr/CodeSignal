"""

Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer inputArray

Guaranteed constraints:
0 ≤ inputArray.length ≤ 104,
0 ≤ inputArray[i] ≤ 109.

[input] integer elemToReplace

Guaranteed constraints:
0 ≤ elemToReplace ≤ 109.

[input] integer substitutionElem

Guaranteed constraints:
0 ≤ substitutionElem ≤ 109.

[output] array.integer

"""

def solution(inputArray, elemToReplace, substitutionElem) :
# {
    return inputArray.replace(elemToReplace, substitutionElem)
# }

# For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

inputArray = [1, 2, 1]
inputArray = [1, 2, 0, 4, 5]
elemToReplace = 1
substitutionElem = 3
elemToReplace = 3
substitutionElem = 0

print(solution(inputArray, elemToReplace, substitutionElem))

"""

********
BONEYARD
********

# tmp = inputArray.index(elemToReplace)
    for i in range(inputArray.count(elemToReplace)) :
    # {
        print(i, inputArray)
        inputArray[inputArray.index(elemToReplace)] = substitutionElem
    # }

"""