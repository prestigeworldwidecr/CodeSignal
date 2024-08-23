"""

Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 10^6.
10 ≤ n < 999999
2, 4 or 6 digits

[output] boolean

true if n is a lucky ticket number, false otherwise.

"""

def solution(n) :
# {
    a = 0
    b = 0
    tmp = str(n)

    for i in range(int(len(tmp) / 2)) :
    # {
        a = a + int(tmp[i])
    # }

    for j in range(int(len(tmp) / 2), int(len(tmp))) :
    # {
        b = b + int(tmp[j])
    # }

    # print(a, b)
    return a == b
    
# }

n = 1230

solution(n)

# For n = 1230, the output should be solution(n) = true;
# For n = 239017, the output should be solution(n) = false.

"""

********
BONEYARD
********

# print(tmp[j])
# print(tmp[i])
i = int((len(tmp) / 2))
# print(i)
tmp = int(str(slice(0, i)))
print(tmp)

"""