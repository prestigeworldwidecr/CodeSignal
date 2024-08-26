"""

Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = True.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = True.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = False.

Any swap of any two elements either in a or in b won't make a and b equal.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer a

Array of integers.

Guaranteed constraints:
3 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.

[input] array.integer b

Array of integers of the same length as a.

Guaranteed constraints:
b.length = a.length,
1 ≤ b[i] ≤ 1000.

[output] boolean

True if a and b are similar, False otherwise.

"""

"""


"""

def onePairSwap(a, b) :
# {
    i = 0
    cnt = 0

    for i in range(len(a)) :
    # {

        if (cnt > 2) :
        # {
            return False
        # }

        else :
        # {

            if (a[i] != b[i]) :
            # {
                cnt = cnt + 1
            # }

            else :
            # {
                None
            # }

        # }

    # }

    return True
# }

def removeDuplicates(s) :
# {
    # tmp = [...new Set(s)].join("")
    tmp = list(set(s))

    return tmp
# }

def isArrayEqual(a, b) :
# {
    i = 0
    
    for i in range(len(a)) :
    # {

        if (a[i] != b[i]) :
        # {
            return False
        # }

        else :
        # {
            None
        # }

    # }

    return True
# }

def areSimilar(a, b) :
# {
    aCopy =  a.copy()
    bCopy =  b.copy()
    
    if (len(a) != len(b)) :
    # {
        return False
    # }

    elif (not(isArrayEqual(sorted(aCopy), sorted(bCopy)))) :
    # {
        return False
    # }

    elif (not(isArrayEqual(removeDuplicates(aCopy), removeDuplicates(bCopy)))) :
    # {
        return False
    # }

    else :
    # {
        return onePairSwap(a, b)
    # }

# }

def solution(a, b) :
# {
    return areSimilar(a, b)
# }

a = [1, 2, 3]
b = [1, 2, 3]
print(solution(a, b)) # For a = [1, 2, 3] and b = [1, 2, 3], the output should be solution(a, b) = True.

"""

********
BONEYARD
********
*****
    STRAT
    *****

    immediate no if length not equal    x
    immediate no if sorted elements arent equal x
    immediate no if elements removed arent equal    x
    check if elements are in same position
    first strike, let pass
    2nd reject

    console.log("a: ", a, " b: ", b)
    console.log("i: ", i, " a[i]: ", a [i], " b[i]", b[i], " cnt: ", cnt)

a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]

# aCopy.sort()
    # bCopy.sort()

console.log(areSimilar(a, b))

# a = [1, 2, 3] and b = [1, 2, 3] solution(a, b) = True.
# a = [1, 2, 3] and b = [2, 1, 3] solution(a, b) = True.
# a = [1, 2, 2] and b = [2, 1, 1] solution(a, b) = False.

# a = [1, 2, 3]
# b = [1, 2, 3]
# a = [1, 2, 3]
# b = [2, 1, 3]
# a = [1, 2, 2]
# b = [2, 1, 1]

# console.log(a == b)
# console.log(a.eq)

# console.log("*4")
        # console.log("*3")
        # else if (a.sort() != )
        # console.log("i: ", i, " cnt: ", cnt, "a[i]: ", a[i], " b[i]: ", b[i])
        # console.log("*1")
        # console.log("*2", " a sorted: ", a.sort(), " b sorted: ", b.sort())
        # console.log("*2: ", a.sort() == b.sort())



"""