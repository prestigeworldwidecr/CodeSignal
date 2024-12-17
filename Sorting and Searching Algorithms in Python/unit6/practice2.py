'''

Great work! You have just sorted a list of random strings using Merge Sort. However, what if you find yourself in a scenario where you are only concerned about the first three characters? A slight tweak to the code could modify this behavior.

Could you adjust the merge operation to compare sub-strings of length 3 instead of comparing entire strings? This modification would enable us to sort the list according to the first three characters of each string.

'''

import random
import string

def merge_sort(data) :
# {
    if (len(data) <= 1):
    # {
        return data
    # }

    else :
    # {
        None
    # }

    mid = len(data) // 2

    left = merge_sort(data[0: mid: ])
    right = merge_sort(data[mid: len(data): ])

    return merge(left, right)

# }

def merge(left, right) :
# {
    res = []
    left_index = 0
    right_index = 0

    while (left_index < len(left) and right_index < len(right)) :
    # {
        if (left[left_index][0: 3: ] < right[right_index][0: 3: ]) :
        # {
            res.append(left[left_index])
            # left_index += 1
            left_index = left_index + 1
        # }

        else:
        # {
            res.append(right[right_index])
            # right_index += 1
            right_index = right_index + 1
        # }

    # }

    res.extend(left[left_index: : ])
    res.extend(right[right_index: : ])

    return res

# }

# Generate random strings
# data = [''.join(random.choices(string.ascii_letters + string.digits, k=6)) for _ in range(20)]
data = []

for i in range(20) :
# {
    data.append(''.join(random.choices(string.ascii_letters + string.digits, k=6)))
# }


print("\nOriginal list of random strings:")
print(data)

sorted_data = merge_sort(data)

print("\nSorted list of random strings:")
print(sorted_data)

'''

********
BONEYARD
********

# print('!', right_index)
# left = data[0: mid: ]
    # right = data[mid: len(data): ]
    # left_index = right_index = 0
    # tmp = 0    

    No worries! Let's break it down. In the merge function, where you compare elements from the left and right lists, think about how you can focus on just the first three characters of each string.

Here's a hint: Instead of comparing the entire strings, try using slicing to compare only the first three characters. How might you modify the comparison line to achieve this?

# while (left_index < 3 and right_index < 3) :
    i = 0
    # while (i <= 3) :

    # i = i + 1

    # print(i, left_index, right_index)

    # if (left[left_index][:3] < right[right_index][:3]) :

'''