'''

Alright, cosmic coder! Here's a brain-tickling challenge for you! You're given a peculiar list of unique integers - it's sorted in a decreasing order and then rotated at a random pivot. So, while you and I know that it's still sorted, it kicks off from an unpredictable point. Your mission, if you choose to accept it, is to hunt down a specific target number in this array and report its index. If the target turns up missing, return -1.

How is the input scheduled to arrive, you ask? Well, the format is a list with positive integer elements, with possible edge cases being an array of size 1 or the target number not being present in the array! You are guaranteed that the array will always consist of unique numbers.

You need to whip up a solution that takes this list and target number as inputs and returns the index of our target, or -1 if it's on the lam. Now, go give it whatever you've got!

'''

def search_dec_rotated(nums, target):
# {
    left = 0
    right = len(nums) - 1

    while left <= right:
    # {
        mid = (left + right) // 2

        if (nums[mid] == target) :
        # {
            return mid
        # }

        elif (nums[left] >= nums[mid]) :
        # {
            if (nums[mid] < target <= nums[left]) :
            # {
                right = mid - 1
            # }

            else :
            # {
                left = mid + 1
            # }

        # }

        elif (nums[mid] >= nums[right]) :
        # {
            if (nums[right] <= target < nums[mid]) :
            # {
                left = mid + 1
            # }

            else :
            # {
                right = mid - 1
            # }

        # }

        else :
        # {
            None
        # }

    # }

    return -1

# }

print(search_dec_rotated([4, 3, 2, 1, 8, 7, 6, 5], 1))  # Expected output: 3
print(search_dec_rotated([9, 8, 7, 6, 5, 4, 3, 2, 1], 4))  # Expected output: 5
print(search_dec_rotated([5, 4, 3, 2, 1], 8))  # Expected output: -1

'''

********
BONEYARD
********

It looks like you're trying to implement a binary search on a rotated, decreasing array. Let's focus on a few key points to guide you:

Midpoint Check: You need to check if the mid element is equal to the target. If it is, return mid.

Determine the Sorted Half: Since the array is rotated, one half will always be sorted. Check if the left half is sorted by comparing nums[left] and nums[mid].

Target Location:

If the left half is sorted and the target is within this range, adjust the right pointer.
If the right half is sorted and the target is within this range, adjust the left pointer.
Adjust Pointers: Based on the checks, adjust left or right to narrow down the search.

Good try, but that's not exactly right. Your solution doesn't effectively handle the properties of a rotated, decreasing array.

nums.append(float('inf'))  # append an infinite element to handle edge case

Target Location:

If the left half is sorted and the target is within this range (nums[left] >= target > nums[mid]), adjust the right pointer.
If the right half is sorted and the target is within this range (nums[mid] > target >= nums[right]), adjust the left pointer.
Adjust Pointers: Based on the checks, adjust left or right to narrow down the search.

X (nums[left] >= target > nums[mid])
(nums[mid] < target <= nums[left])

X (nums[mid] > target >= nums[right])
(nums[right] <= target < nums[mid])

if (nums[left] <= nums[mid] and nums[left] <= target < nums[mid]) :
        # {
            right = mid - 1
        # }

        elif (nums[mid] <= nums[right] and nums[mid] < target <= nums[right]) :
        # {
            left = mid + 1
        # }

        elif (nums[right] < nums[mid]) :
        # {
            left = mid + 1
        # }

        else :
        # {
            right = mid - 1
        # }


'''