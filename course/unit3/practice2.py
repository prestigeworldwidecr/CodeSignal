'''

Alright, Voyager, here's your next mission. Your objective is to identify all the elements in a list of integers that are repeating their ugly mugs more than once. They could be negative and in no particular order, just to keep you on your toes!

Your final output should be a list of these duplicate numbers. The order? Doesn't matter! Maybe they were just in the wrong place at the wrong time.

All clear? Time's a-wasting, let's crack on, space cowboy!

'''

def repeating_elements(nums) :
# {
    # implement this
    result = set()
    
    for i in nums :
    # {
        if (nums.count(i) > 1) :
        # {
            result.add(i)
        # }

        else :
        # {
            None
        # }

    # }

    return result

# }

print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # expected output : [8, 7]
# print(repeating_elements([-1, 2, 3, -1, 2, 3]))   # expected output : [-1, 2, 3]
# print(repeating_elements([1, 2, 3, 4, 5]))        # expected output : []

'''

********
BONEYARD
********

# print(i, nums.count(i))

tmp = nums.count(nums[2])
    print(tmp)

'''