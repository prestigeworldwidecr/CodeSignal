'''

Alright, Voyager, here's your next mission. Your objective is to identify all the elements in a list of integers that are repeating their ugly mugs more than once. They could be negative and in no particular order, just to keep you on your toes!

Your final output should be a list of these duplicate numbers. The order? Doesn't matter! Maybe they were just in the wrong place at the wrong time.

All clear? Time's a-wasting, let's crack on, space cowboy!

'''

def repeating_elements(nums) :
# {
    # implement this
    # result = set()
    seen = set()
    duplicates = set()
    
    for i in nums :
    # {
        # print(i)
        if (i in seen) :
        # {
            duplicates.add(i)
        # }

        else :
        # {
            seen.add(i)
        # }

    # }

    return duplicates

# }

print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # expected output : [8, 7]
# print(repeating_elements([-1, 2, 3, -1, 2, 3]))   # expected output : [-1, 2, 3]
# print(repeating_elements([1, 2, 3, 4, 5]))        # expected output : []

'''

********
BONEYARD
********

Great start! Your solution works, but using nums.count(i) inside the loop makes it less efficient since it checks the count for each element repeatedly.

Consider using two sets: one to track seen elements and another for duplicates. This way, you can achieve better performance. How might you implement this? 🐾

Sure thing! Here's a small hint to get you started:

Create two sets:

One set to keep track of elements you've seen.
Another set to store elements that are duplicates.
Iterate through the list:

If an element is already in the "seen" set, add it to the "duplicates" set.
If it's not in the "seen" set, add it there.
Return the list of duplicates

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

# print(i, nums.count(i))

tmp = nums.count(nums[2])
    print(tmp)

'''