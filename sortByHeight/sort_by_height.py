"""

Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer a

If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

Guaranteed constraints:
1 ≤ a.length ≤ 1000,
-1 ≤ a[i] ≤ 1000.

[output] array.integer

Sorted array a with all the trees untouched.

"""

def solution(a) :
# {
    j = 0
    b = a.copy()
    b = sorted(b)

    while (len(b) > 0) :
    # {
        if (b[0] == -1) :
        # {
            b.pop(0)
        # }

        else :
        # {
            break
        # }

    # }

    for i in range(len(a)) :
    # {

        if (a[i] == -1) :
        # {
            None
        # }

        else :
        # {
            a[i] = b[j]
            j = j + 1
        # }

    # }

    return a

# }

a = [-1, 150, 190, 170, -1, -1, 160, 180] # [-1, 150, 160, 170, -1, -1, 180, 190]
a1 = [4, 2, 9, 11, 2, 16]
a2 = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
# a = [-1, -1, -1, -1, -1]

solution(a)

"""

********
BONEYARD
********

print(i, len(b), b[j], b)

import sys

start_ppl = -1

# for i in range(len(b)) :
    # {
        # print(i, len(b), b[i], b)
        
        # if (b[i] == -1) :
        # {
            # print("hi")
            # b.pop(i)
        # }

        # else :
        # {
            # None
        # }

    # }

# start_ppl = i
# break

# i = sys.maxsize # exit
# print(i)

https://www.geeksforgeeks.org/enumerate-in-python/

# print("hi")
# print(b[i], i)
        

# copy 1 remove trees, sort
    # original array, replace non-minus 1s w/None
    # place copy 1 in order into None's

    # print(str(a).replace("-1", "None"))
    # can use list functions
    # https://www.w3schools.com/python/python_lists_remove.asp
    # b.remove(-1)
    # b[0] = 99

// stringToIntArray(tmp);
    // tmp[i] = parseInt(a[i]);
    // tmp = tmp.sort();
    // tmp.push(i);
    // console.log(tmp);
    // console.log(a[i]);
    // return tmp;

// tmp[k] = -1;
// tmp[k] = a[i];
// console.log("b[j]: ", b[j], " a[i]: ", a[i]);


    // var tmp = new Float64Array(a);
    // var numArray = new Float64Array([140000, 104, 99]);
    // tmp = Array.from(a, Number);

    // console.log(tmp);

// console.log(a, b);
// for (i; i < (a.length + b.length); i++)

"""