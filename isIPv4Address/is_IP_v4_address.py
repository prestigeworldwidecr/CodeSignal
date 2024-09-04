"""

An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A string consisting of digits, full stops and lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 30.

[output] boolean

true if inputString satisfies the IPv4 address naming rules, false otherwise.

"""

def solution(inputString) :
# {
    is_IP_v4_address = False
    tmp = inputString.split('.')

    if (len(tmp) == 4) :
    # {
        None
    # }

    else :
    # {
        return False
    # }

    for i in tmp :
    # {
        if (i.isdigit() and 0 <= int(i) and int(i) < 256) :
        # {
            is_IP_v4_address = True
        # }

        else :
        # {
            return False
        # }

    # }

    return is_IP_v4_address

# }

# For inputString = "172.16.254.1", the output should be solution(inputString) = true;
inputString = "172.16.254.1"
print(solution(inputString))

"""

********
BONEYARD
********

# print(i)
# print(tmp)

# print(inputString)

author: dnl-blkv

def solution(s):
    p = s.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

"""