"""

CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
solution(inputString) = 14.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

Guaranteed constraints:
0 ≤ inputString.length ≤ 105.

[output] integer


"""

import string

def solution(inputString) :
# {
    inputString = inputString.replace(' ', '_')
    tmp = list(inputString)
    result = ""
    
    for i in range(len(inputString)) :
    # {
        if (tmp[i].isdigit() or tmp[i] == '+' or tmp[i] == '-' or tmp[i] == '*' or tmp[i] == '/') :
        # {
            None
        # }

        else :
        # {
            tmp[i] = '_'
        # }

    # }

    # tmp = tmp.split('*')

    return tmp
# }

# For inputString = "2 apples, 12 oranges", the output should be solution(inputString) = 14.
# inputString: "there are some (12) digits 5566 in this 770 string 239"
# inputString: "abcdefghijklmnopqrstuvwxyz1AbCdEfGhIjKlMnOpqrstuvwxyz23,74 -"
inputString = "2 apples, 12 oranges"
inputString = "there are some (12) digits 5566 in this 770 string 239"
inputString = "abcdefghijklmnopqrstuvwxyz1AbCdEfGhIjKlMnOpqrstuvwxyz23,74 -"

print(solution(inputString))

"""

********
BONEYARD
********

 tmp = inputString.replace('(', '')
    tmp = tmp.replace(')', '')
    print(tmp)
    tmp = tmp.split(' ')
    sum = 0

    for i in range(len(inputString)) :
    # {
        if (inputString[i].isalpha()) :
        # {
            inputString[i] = ''
            print(inputString[i])
        # }

        else :
        # {
            print(inputString[i])
            None
        # }

    # }

    print('!', inputString)

"!"#$%&'(),.:;<=>?@[\]^_`{|}~"


    for i in tmp :
    # {
        if (i.isdigit()) :
        # {
            # print(i)
            sum = sum + int(i)
        # }

        else :
        # {
            None
        # }

    # }

"""