'''

Deep within the kingdom of Million Numbers, a challenge was set before the esteemed Pythonista. This kingdom was a land of diversity, filled with n elements, each an integer between -100 and 100. The count of these elements was no small number either - ranging anywhere from 1 to a whopping 1000000.

The Pythonista was handed a scroll that represented these elements as a list of integers. The Pythonista's task? To delve deep into this pool of numbers and find the smallest absolute difference between any pair of elements.

In the kingdom of Million Numbers, the absolute difference was measured as |a - b|, where a and b signified any two elements from the list.

The Pythonista was asked to weave a magical function named solution(nums). This Python function would take in the list of integers 'nums', representative of all elements in the kingdom; it would parse through the sea of numbers and elegantly return the smallest absolute difference among all possible pairs.

Although the kingdom was grand in scale, efficiency was revered. The Pythonista's magic had to be potent and swift - an optimized spell capable of working at a time complexity of 
O
(
n
l
o
g
n
)
O(nlogn) or better, to ensure the quickest resolution to the kingdom's interesting challenge.

Notes:

If n = 1, the minimum absolute difference is 0, since there is only one number, leaving no other number to pair it with.
It is guaranteed that the list nums contains no duplicate numbers.

Thanks for your feedback! Here’s a straightforward summary:

You get a list of integers (size n, no duplicates).
Find the smallest absolute difference 
∣
a
−
b
∣
∣a−b∣ between any two numbers in the list.
If there’s only one number, return 0.
Your solution should be efficient: 
O
(
n
log
⁡
n
)
O(nlogn) or better.
Does this help clarify the task? If you have any specific questions about the requirements, let me know!

Absolutely! Here’s a simple example:

Suppose nums = [4, 9, 1, 32].

The absolute differences between all pairs are:
∣
4
−
9
∣
=
5
∣4−9∣=5
∣
4
−
1
∣
=
3
∣4−1∣=3
∣
4
−
32
∣
=
28
∣4−32∣=28
∣
9
−
1
∣
=
8
∣9−1∣=8
∣
9
−
32
∣
=
23
∣9−32∣=23
∣
1
−
32
∣
=
31
∣1−32∣=31
The smallest absolute difference is 3 (between 4 and 1).



'''

import sys

def solution(nums) :
# {
    # TODO: implement the function to find minimum absolute difference among all pairs.
    min_diff = sys.maxsize
    nums.sort()

    if (len(nums) < 2) :
    # {
        return 0
    # }

    else :
    # {
        for i in range(len(nums) - 1) :
        # {
            cur_diff = nums[i + 1] - nums[i]
            
            if (cur_diff < min_diff) :
            # {
                min_diff = cur_diff
            # }

            else :
            # {
                None
            # }

        # }

    # }

    return min_diff
# }

nums = [4, 9, 1, 32]

print(solution(nums))

'''

***** BONEYARD *****

# print(nums)

'''