'''

Hey, Space Ace! Ready for a fun task? Imagine we're cruisin' the galaxy and bump into an array of integers, sorted but with some stowaway duplicates. Your mission, oh brainy one, is to craft an algorithm, using a modified binary search, to find where a given integer, our target, should dock. If the target is already in the array, return the index of its leftmost occurrence. If it's lost in space, provide the index where it should join while keeping the array sorted.

You'll be coding a function that takes two inputs. First, the array of integers, such as [1, 2, 3, 3, 5] and second, the target integer, say 3. But remember, it could be that the target is not on the list, for example, 4.

The function should return an integer representing an index. For the target 3, our solution should be 2, the index of the leftmost 3. In the case of the target 4, the answer is 3, the would-be location of 4 if we need to maintain the sorted order.

Do note the input array will always be sorted in ascending order and will always contain at least one number.

'''

def insert_position(nums, target) :
# {
    # implement this
    left = 0
    right = len(nums)
    
    while right - left > 1 :
    # {
        mid = (left + right) // 2

        if (nums[mid] <= target) :
        # {
            left = mid
        # }
        
        else:
        # {
            right = mid
        # }
        
    # }

    return left
# }

print(insert_position([1, 2, 3, 3, 5], 3))  # Expected output: 2
print(insert_position([1, 2, 3, 3, 5], 4))  # Expected output: 4
print(insert_position([1, 3, 5, 7, 9], 10)) # Expected output: 5

'''

********
BONEYARD
********

    # nums.append(float('inf'))  # append an infinite element to handle edge case
    # left, right = 0, len(nums)

'''