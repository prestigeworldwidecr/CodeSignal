'''

Time to show off your new skills, star-traveler! Imagine this - you are surveying a list of whole numbers (it could be any integer between 
−
1
0
9
−10 
9
  and 
1
0
9
10 
9
 ).

Here's the twist: your task is to count anti-inversion pairs. More specifically, the anti-inversion is a pair of indices 
(
i
,
j
)
(i,j) that fulfill the specific condition: 
i
<
j
i<j and 
n
u
m
s
[
i
]
<
n
u
m
s
[
j
]
nums[i]<nums[j].

Consider both the positive and negative numbers as well as repetitions, and keep in mind: your list could be as small as 1 number or as large as 
1
0
5
10 
5
  numbers!

'''

def count_anti_inversions(arr) :
# {
    # implement this
    if (len(arr) <= 1) :
    # {
        return arr, 0
    # }

    else :
    # {
        middle = int(len(arr) / 2)
        left, a = count_anti_inversions(arr[0 : middle: ])
        right, b = count_anti_inversions(arr[middle: : ])
        result, c = merge_count_anti_inversions(left, right)
        # return result, (a + b + c)
        
        # middle = int(len(arr) / 2)
        # left, a = count_anti_inversions(arr[0 : middle: ])
        # right, b = count_anti_inversions(arr[middle: : ])
        # result, c = merge_count_anti_inversions(left, right)

        # left = count_anti_inversions(arr[0 : middle: ])
        # right = count_anti_inversions(arr[middle: : ])
        # result = merge_count_anti_inversions(left, right)

        return result, (a + b + c)
    # }

# }

def merge_count_anti_inversions(x, y) :
# {
    # implement this
    count = 0
    i = 0
    j = 0

    merged = []

    while (i < len(x) and j < len(y)) :
    # {
        if (x[i] <= y[j]) :
        # {
            merged.append(x[i])
            i = i + 1
        # }

        else :
        # {
            merged.append(y[j])
            j = j + 1
            count = count + len(x) - i
        # }

    merged.extend(x[i: : ])
    merged.extend(y[j: : ])

    return merged, count
# }

# Testing the function
test_array = [2, 4, 1, 3, 5]
_, inv_count = count_anti_inversions(test_array)

print("Number of anti-inversions in", test_array, "is", inv_count)  # Expected Output: 7

'''

***** BONEYARD *****

# inv_count = count_anti_inversions(test_array)
# print('!', _, inv_count)

'''