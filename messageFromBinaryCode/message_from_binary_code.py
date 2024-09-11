"""

You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.

Example

For code = "010010000110010101101100011011000110111100100001", the output should be
solution(code) = "Hello!".

The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 72 stands for H in the ASCII-table, so the first letter is H.
Other letters can be obtained in the same manner.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string code

A string, the encrypted message consisting of characters '0' and '1'.

Guaranteed constraints:
0 < code.length < 800.

[output] string

The decrypted message.

"""

def convert_8bit(s) :
# {
    tmp = ""
    result = []

    for i in range(len(s)) :
    # {
        tmp = tmp + s[i]

        if ((i + 1) % 8 == 0) :
        # {
            result.append(tmp)
            tmp = ""
        # }

        else :
        # {
            None
        # }

    # }

    return result

# }

def convert_8bit_to_ASCII(a) :
# {
    result = ""

    for i in range(len(a)) :
    # {
        # print(i, a[i], int(a[i], 2), chr(int(a[i], 2)))
        result = result + chr(int(a[i], 2))
    # }

    return result
# }

def solution(code) :
# {
    return convert_8bit_to_ASCII(convert_8bit(code))
# }

code = "010010000110010101101100011011000110111100100001"   # the output should be solution(code) = "Hello!".

print(solution(code))
      
"""

********
BONEYARD
********

"""