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

'''

def optimizedReplace(A, B) :
# {
    # TODO: implement the function
    sorted_B = B.copy()
    sorted_B.sort()
    C = [0] * len(A)
    i = 0

    while (i < len(B) - 1) :
    # {
        closest_neighbor_index_sorted_B = sorted_B.index(B[i])

        # print(i, B[i], closest_neighbor_index_sorted_B)

        print(sorted_B[closest_neighbor_index_sorted_B])

        # closest_neighbor_value_B = min(abs(sorted_B[closest_neighbor_index_sorted_B] - sorted_B[closest_neighbor_index_sorted_B - 1])), abs(sorted_B[closest_neighbor_index_sorted_B] - sorted_B[closest_neighbor_index_sorted_B + 1])

        # print(closest_neighbor_value_B)

        i = i + 1
    # }

    # print(sorted_A, sorted_B, C)
# }

A = [10, 20, 30, 40, 50]
B = [7, 5, 1, 2, 4]

print(optimizedReplace(A, B))

'''

***** BONEYARD *****


        
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