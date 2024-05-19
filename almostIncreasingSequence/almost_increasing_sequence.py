"""

Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
solution(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 10^5,
-105 ≤ sequence[i] ≤ 10^5.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

"""

def solution(sequence) :
# {
    cnt = 0
    cur = sequence[1]
    next = sequence[2]

    for i in range(0, len(sequence) - 1) :
    # {
        cur = sequence[i]
        next = sequence[i + 1]
    
        if (cur >= next) :
        # {
            cnt = cnt + 1
        # }

        else :
        # {
            "do nothing"
        # }

    # }

    print(cnt)

    if (cnt > 1) :
    # {
        return False
    # }
    
    else :
    # {
        return True
    # } 

# }

sequence = [1, 3, 2]
# sequence = [1, 3, 2, 1]
# sequence = [1, 2, 1, 2]
print(solution(sequence))

"""

########
BONEYARD
########

# compare arragned set length to arranged length
    # run through array, if not in order, remove try again, zero tolerance
    # print(len(dict.fromkeys(sequence))) --> 3

    # s1 = sorted(sequence)
    # s2 = dict.fromkeys(sequence)
    # prev = sequence[0]
    # print(i, cur, next)
        print(cnt)

"""