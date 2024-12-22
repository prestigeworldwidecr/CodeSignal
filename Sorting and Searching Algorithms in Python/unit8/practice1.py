'''

Alright, Stellar Navigator, here's a scenario for you. Suppose you've got a list of integers, and you're hunting for the 
k
k-th largest cosmic gem — I mean integer — in that list. Now, remember, we're space-trotters, so when we say 
k
=
1
k=1, we're looking for the largest gem. For 
k
=
2
k=2, we're after the second largest, and so forth.

Your mission, should you choose to accept it, is to accept two parameters: the list of integers and the index 
k
k. The list may contain duplicates, and 
k
k will always be between 1 and the size of the list.

Your output should be the 
k
k-th largest value, just like I taught you. And if two numbers are identical? Hey, remember, in this galaxy, they're considered the same no matter their position on the list!

'''

import random

def find_kth_largest(numbers, k) :
# {
    if (numbers) :
    # {
        pos = partition(numbers, 0, len(numbers) - 1)
    
        if (k - 1 == pos) :
        # {
            # The pivot is the k-th element after partitioning
            return numbers[pos]
        # }

        elif (k - 1 > pos) :
        # {
            # The pivot index after partitioning is larger than k
            # We'll keep searching in the left part
            return find_kth_largest(numbers[ : pos: ], k)
        # }

        else :
        # {
            # The pivot index after partitioning is smaller than k
            # We'll keep searching in the right part
            return find_kth_largest(numbers[pos + 1: : ], k - pos - 1)
        # }

    else :
    # {
        return None
    # }

# }
        
def partition(nums, l, r) :
# {
    # Choosing a random index to make the algorithm less deterministic
    rand_index = random.randint(l, r)

    # nums[l], nums[rand_index] = nums[rand_index], nums[l]
    tmp = nums[l]
    nums[l] = nums[rand_index]
    nums[rand_index] = tmp
    pivot_index = l

    for i in range(l + 1, r + 1) :
    # {
        if (nums[i] <= nums[l]) :
        # {
            # pivot_index += 1
            pivot_index = pivot_index + 1
            # nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
            tmp = nums[i]
            nums[i] = nums[pivot_index]
            nums[pivot_index] = tmp
        # }

        else :
        # {
            None
        # }

    # }

    # nums[pivot_index], nums[l] = nums[l], nums[pivot_index]
    tmp = nums[pivot_index]
    nums[pivot_index] = nums[l]
    nums[l] = tmp

    return pivot_index

# }

print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # Expected output: 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Expected output: 4

'''

***** BONEYARD *****

'''