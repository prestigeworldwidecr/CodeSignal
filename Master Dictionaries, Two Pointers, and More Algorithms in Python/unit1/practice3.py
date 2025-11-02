'''

You are given two arrays, Array A and Array B, each containing n integers where n can range from 
1
1 to 
100000
100000, inclusive. All elements of both arrays are integers that can range from 
−
10
10
−10 
10
  to 
10
10
10 
10
 , inclusive.

Your task is to create a function optimizedReplace that returns a new array, C. For each index i, C[i] should contain a specific value from Array A - A[j], determined by the condition that B[i] is the closest number to B[j] from Array B.

This means that Array C will have the same length as A and B. Array C[i] will contain the value corresponding to the jth index from Array A, where the value at the jth index in Array B is closest to the value at the ith index of Array B.

Assume that there is no ambiguity. The Array B is given in a way that no two elements in Array B have the same minimal absolute difference with B[i].

Remember, the number of elements, n, and the range of the elements, imply that brute force solutions will not be efficient. You should aim to leverage optimized algorithms and techniques to solve this task efficiently.

Example

Suppose we have Array A = [10, 20, 30, 40, 50] and Array B = [7, 5, 1, 2, 4].

The function optimizedReplace(A, B) should work as follows:

For B[0] = 7, the closest number in Array B is 5 at index 1. Hence, C[0] = A[1] = 20.

For B[1] = 5, the closest number in Array B is 4 at index 4. Thus, C[1] = A[4] = 50.

For B[2] = 1, the closest number in Array B is 2 at index 3. Hence, C[2] = A[3] = 40.

For B[3] = 2, the closest number in Array B is 1 at index 2. So, C[3] = A[2] = 30.

Lastly, for B[4] = 4, the closest number in Array B is 5 at index 1. We have C[4] = A[1] = 20.

Thus, the function optimizedReplace([10, 20, 30, 40, 50], [7, 5, 1, 2, 4]) should return [20, 50, 40, 30, 20].

Try pairing each value in B with its original index, then sort these pairs by the value in B.
After sorting, for each element, its closest neighbor will be either the previous or next element in the sorted list.
Use the original indices to map back to A.
How might you use this idea to avoid slow .index() calls?

No worries! You’re close to the right idea, but your current approach is still using .index() inside a loop, which is too slow for large arrays.

Here’s a step-by-step nudge:

Try pairing each value in B with its original index:
For example, make a list like [(7, 0), (5, 1), (1, 2), ...].
Sort this list by the value (not the index).
Now, for each element in the sorted list, its closest neighbor is either the previous or next element in the sorted list.
For each original index, set C[original_index] = A[neighbor's original index].
Can you try building that paired and sorted list? Let me know if you want a code snippet for just that part!

You're on the right track with pairing and sorting, but your main bug is in how you fill the result array. Right now, you're assigning to C[i], but i is the position in the sorted list, not the original index.

Try this:

After sorting, for each element in the sorted list, use its original index to assign the result:
For each k in the sorted list, let orig_idx = B_enum[k][1].
Find the closest neighbor (either k-1 or k+1), and get its original index as well.
Set C[orig_idx] = A[neighbor's original index].
Can you update your loop to use the original indices this way?

Nice job getting steps 1 and 2 done! You’ve got the paired and sorted list. Now, let’s focus on step 3 and 4, where most of your bugs are.

Here’s what’s going wrong:

You’re filling C[i], but i is the position in the sorted list, not the original index.
You should fill C[orig_idx], where orig_idx is the original index from your sorted pair.
When finding neighbors, always use the sorted list, and compare the values, not the indices.
Try this structure inside your loop:

For each position k in the sorted list:
Let val, orig_idx = B_enum[k]
If k == 0, the only neighbor is k+1
If k == n-1, the only neighbor is k-1
Otherwise, compare the distance to k-1 and k+1 and pick the closer one
Set C[orig_idx] = A[neighbor's orig_idx]
Can you try updating your loop to use this approach?

'''

def create_paired_array(arr) :
# {
    result = [] * len(arr)
    
    for index, value in enumerate(arr) :
    # {
        result.append((value, index))
    # }

    # print(result)

    return result
# }

def optimizedReplace(A, B) :
# {
    # TODO: implement the function
    C = [0] * len(A)
    B_enum = create_paired_array(B)
    B_enum.sort()
    neighbor_index = 0

    for i in range(len(B_enum)) :
    # {
        # print(e[1])
        # C.append(A[e[1]])
        if (i == 0) :
        # {
            neighbor_index = i + 1
        # }

        elif (i == len(B_enum) - 1):
        # {
            neighbor_index = i - 1
        # }

        else :
        # {
            if (B_enum[i][0] - B_enum[i - 1][0] < B_enum[i + 1][0] - B_enum[i][0]) :
            # {
                neighbor_index = B_enum[i - 1][1]
            # }

            else :
            # { 
                neighbor_index = B_enum[i + 1][1]
            # }

        # }

        C[B_enum[i][1]] = A[B_enum[neighbor_index][1]]
    # }
    
    # print(B_enum)
    # print(C)
    return C

# }

A = [10, 20, 30, 40, 50]
B = [7, 5, 1, 2, 4]
# Thus, the function optimizedReplace([10, 20, 30, 40, 50], [7, 5, 1, 2, 4]) should return [20, 50, 40, 30, 20].

print(optimizedReplace(A, B))

'''

***** BONEYARD *****

n = len(B_enum)
for i in range(n):
    val, orig_idx = B_enum[i]
    # Check neighbors
    if i == 0:
        neighbor_idx = i + 1
    elif i == n - 1:
        neighbor_idx = i - 1
    else:
        left_diff = abs(val - B_enum[i - 1][0])
        right_diff = abs(val - B_enum[i + 1][0])
        neighbor_idx = i - 1 if left_diff < right_diff else i + 1
    # Use the neighbor's original index to get value from A
    C[orig_idx] = A[B_enum[neighbor_idx][1]]

from operator import itemgetter, attrgetter

# Using itemgetter
sorted_by_age = sorted(data, key=itemgetter('age'))

sorted_B = B.copy()
sorted_B.sort()
C = [0] * len(A)
i = 0
closest_neighbor_B_index = 0
sorted_B_left_neighbor_diff = 0
sorted_B_right_neighbor_diff = 0

# print("A = [10, 20, 30, 40, 50]")
# print("B = [7, 5, 1, 2, 4]")
# print("B[i]\tsorted_B_index\tsorted[sorted_B_index]")
# print("closest_neighbor_B_index\tsorted_B_left_neighbor_diff\tsorted_B_right_neighbor_diff")

while (i < len(B)) :
# {
    sorted_B_index = sorted_B.index(B[i])

    if (sorted_B_index == 0) :
    # {
        closest_neighbor_B_index = B.index(sorted_B[1])
        # print(sorted_B[1], B.index(sorted_B[1]))
    # }

    elif (sorted_B_index == len(B) - 1) :
    # {
        # print('!')
        closest_neighbor_B_index = B.index(sorted_B[len(B) - 2])
        # print(sorted_B[len(B) - 2], B.index(sorted_B[len(B) - 2]))
    # }

    else :
    # {
        sorted_B_left_neighbor_diff = sorted_B[sorted_B_index] - sorted_B[sorted_B_index - 1]
        sorted_B_right_neighbor_diff = sorted_B[sorted_B_index + 1] - sorted_B[sorted_B_index]

        print("sorted_B_left_neighbor_diff\tB[i]\tsorted_B_index\tsorted_B[sorted_B_index] sorted_B[sorted_B_index - 1] sorted_B[sorted_B_index + 1] closest_neighbor_B_index")
        # print(sorted_B_left_neighbor_diff, "\t\t\t\t", B[i], "\t", sorted_B_index, "\t\t", sorted_B[sorted_B_index], "\t\t\t\t", sorted_B[sorted_B_index - 1], "\t\t\t\t\t", sorted_B[sorted_B_index + 1])

        if (sorted_B_left_neighbor_diff < sorted_B_right_neighbor_diff) :
        # {
            closest_neighbor_B_index = sorted_B_index - 1
        # }

        else :
        # {
            closest_neighbor_B_index = sorted_B_index + 1
        # }

        # print(sorted_B_left_neighbor_diff, "\t\t\t\t", B[i], "\t", sorted_B_index, "\t\t", sorted_B[sorted_B_index], "\t\t\t", sorted_B[sorted_B_index - 1], "\t\t\t\t", sorted_B[sorted_B_index + 1], "\t\t\t\t", closest_neighbor_B_index)

    # }

    # print(B[i], "\t", sorted_B_index, "\t\t", sorted_B[sorted_B_index])
    # print(closest_neighbor_B_index, "\t\t\t\t", sorted_B_left_neighbor_diff, "\t\t\t\t", sorted_B_right_neighbor_diff)

    C[i] = A[closest_neighbor_B_index]
    i = i + 1

# }

return C

# print('#')
            
# print('!')
# closest_neighbor_index_sorted_B = 1

# print('@')
# closest_neighbor_index_sorted_B = len(B) - 2


closest_neighbor_sorted_B_index = 0
closest_neighbor_sorted_B_value = 0
    

# closest_neighbor_index_sorted_B
# sorted_B_left_neighbor_index = sorted_B_index - 1
# sorted_B_right_neighbor_index = sorted_B_index + 1

# print(i, B[i], closest_neighbor_index_sorted_B)

# print(sorted_B[closest_neighbor_index_sorted_B])

# closest_neighbor_value_B = min(abs(sorted_B[closest_neighbor_index_sorted_B] - sorted_B[closest_neighbor_index_sorted_B - 1])), abs(sorted_B[closest_neighbor_index_sorted_B] - sorted_B[closest_neighbor_index_sorted_B + 1])

# print(closest_neighbor_value_B)
        
# sorted_A = A.copy()
# sorted_A.sort()

# left = 

# for i in range(len(B)) :
# tmp = B[i]
# print(i, tmp, len(B))

import sys

def index_smallest_neighbor(arr, n) :
# {
    min_diff = sys.maxsize
    sorted_arr = arr.copy()
    sorted_arr.sort()

    if ()

    return smallest_neighbor
# }

def index_closest_neighbor(arr, n) :
# {
    # closet_neighbor = 0
    # print(arr, n)
    index_closest_neighbor = arr.index(index_smallest_neighbor(arr, n))
    
    # print(index_closest_neighbor)
# }

nums.sort()

for i in range(len(arr) - 1) :
# {
    cur_diff = abs(arr[i + 1] - arr[i])
    print('#', cur_diff)
    
    if (cur_diff < min_diff) :
    # {
        min_diff = cur_diff
        # min_index = i
    # }

    else :
    # {
        None
    # }

# }

print('##', min_diff)

'''