"""

A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
solution(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
solution(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
solution(inputString) = false.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

Guaranteed constraints:
15 ≤ inputString.length ≤ 20.

[output] boolean

true if inputString corresponds to MAC-48 address naming rules, false otherwise

"""

def is_MAC_letter(c) :
# {
    return (c == 'A' or c == 'B' or c == 'C' or c == 'D' or c == 'E' or c == 'F')
# }

def all_MAC_compliant(inputString) :
# {
    tmp = "".join(inputString.split('-'))
    result = False

    # print('!', tmp)
    
    for i in range(len(tmp)) :
    # {
        # print(tmp, i, tmp[i], len(tmp))
        
        if (is_MAC_letter(tmp[i]) or tmp[i].isdigit()) :
        # {
            result = True
        # }
        
        else :
        # {
            return False
        # }
    # }

    return result

# }

def solution(inputString) :
# {
    
    # print(tmp)
    if (len(inputString) == 17) :
    # {
        return all_MAC_compliant(inputString)
    # }

    else :
    # { 
        return False
    # }
    
# }

# For inputString = "00-1B-63-84-45-E6", the output should be solution(inputString) = true;
# For inputString = "Z1-1B-63-84-45-E6", the output should be solution(inputString) = false;
# For inputString = "not a MAC-48 address", the output should be solution(inputString) = false.
# inputString = "00-1B-63-84-45-E6"
# inputString = "Z1-1B-63-84-45-E6"
inputString = "not a MAC-48 address"
inputString = "02-03-04-05-06-07-"
print(solution(inputString))
# print(is_MAC_letter('D'))
# print(is_MAC_letter('a'))


"""

********
BONEYARD
********

"""