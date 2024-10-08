"""

In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. The message contains several numbers that, when typed into a supercomputer, will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.

You figured out that some numbers have a modified single digit in their binary representation. More specifically, in the given number n the kth bit from the right was initially set to 0, but its current value might be different. It's now up to you to write a function that will change the kth bit of n back to 0.

Example

For n = 37 and k = 3, the output should be
solution(n, k) = 33.

3710 = 1001012 ~> 1000012 = 3310.

For n = 37 and k = 4, the output should be
solution(n, k) = 37.

The 4th bit is 0 already (looks like the Mad Coder forgot to encrypt this number), so the answer is still 37.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
0 ≤ n ≤ 2^31 - 1.

[input] integer k

The 1-based index of the changed bit (counting from the right).

Guaranteed constraints:
1 ≤ k ≤ 31.

[output] integer

"""

def solution(n, k) :
# {
    tmp = list("{0:b}".format(n))
    
    if (k >= len(tmp)) :
    # {
        return n
    # }

    else :
    # { 
        tmp[len(tmp) - k] = 0
        result = ""
        
        for i in range(len(tmp)) :
        # {
            result = result + str(tmp[i])
        # }

        return int(result, 2)
    # }

    return ...

# }

# For n = 37 and k = 3, the output should be solution(n, k) = 33.
n = 37
k = 3
n = 0
k = 4

print(solution(n, k))


"""

********
BONEYARD
********

# tmp = str(bin(n)).format(int_value)
# tmp = str(tmp)
    # print(' '.join(str(tmp)))

    # return int(str(tmp), 2)

"""