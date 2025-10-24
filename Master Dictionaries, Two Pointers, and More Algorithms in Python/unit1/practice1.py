'''

In the realm of Integerland, there exist two towns named Town A and Town B. The towns are positioned along a straight road, at points corresponding to different integers. The fascinating fact about Integerland is that the locations of the towns could change. They can take any integer value between 1 and 500.

Your mission, should you choose to accept it, is to create a very special kind of map - a function or method, so to speak - that can calculate the total value of all the points (integer numbers) along the road between Town A and Town B, both towns included.

You might find towns A and B at the same location (i.e., a equals b) or Town A could be located before or after Town B along the road.

Just to give you an idea of what you're getting into, let's consider an instance when Town A is at point 1 (i.e., a=1) and Town B is at point 5 (so b=5). Here, the summation of all the points from Town A to Town B inclusive, which are 1, 2, 3, 4, 5, comes up to 15. We hope your map (or function) could calculate this total in similar situations.

Of course, in the best interests of Integerland and the occasional travellers, we'd like you to optimize this map. It is essential that it works as efficiently as possible. Your understanding of complexity analysis and various ways of optimizing this task will certainly come in handy.

Best of luck on your endeavour!

Constraints

Both a and b are integers.
1 ≤ a, b ≤ 1000000000.

'''

def solution(a, b) :
# {
    # TODO: write your code here
    result = 0
    tmp1 = a * (a + 1) // 2
    tmp2 = b * (b + 1) // 2
    
    if (b > a) :
    # {
        result = tmp2 - tmp1 + a
    # }

    else :
    # {
        result = tmp1 - tmp2 + b
    # }

    return result

# }

a = 1
b = 5

print(solution(a, b))

'''

***** BONEYARD *****

# i = b - a
# return n (n + 1) / 2

result = a

while (a < b) :
# {
    a = a + 1
    result = result + a
# }
    

'''