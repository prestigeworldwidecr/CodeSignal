"""

Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

Example

For a = [50, 60, 60, 45, 70], the output should be
solution(a) = [180, 105].

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 105,
45 ≤ a[i] ≤ 100.

[output] array.integer

"""

def alternatingSums(a) :
# {
    i = 0
    is_even = False
    even_sum = 0
    odd_sum = 0
    result = [0, 0]

    for i in range(len(a)) :
    # {
        is_even = (i + 1) % 2

        if (is_even) :
        # {
            even_sum = even_sum + a[i]
        # }

        else :
        # {
            odd_sum = odd_sum + a[i]
        # }
    # }

    result [0] = even_sum
    result [1] = odd_sum

    return result
# }

def solution(a) :
# {
    return alternatingSums(a)
# }

a = [50, 60, 60, 45, 70]
print(solution(a))
# For a = [50, 60, 60, 45, 70], the output should be solution(a) = [180, 105].

"""

********
BONEYARD
********

a = [50, 60, 60, 45, 70]   # solution(a) = [180, 105]

alternatingSums(a)

    # console.log("i: ", i, " even? ", is_even)
    # console.log("even_sum: ", even_sum, " odd_sum: ", odd_sum)
    # console.log(result)

"""