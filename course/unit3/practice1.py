'''

Hold onto your tail, Voyager! We're in the midst of an integers war, separated into two integer lists! We have to find the common integers in both lists. Remember, we only need the unique ones. Your mission is to compute a new set of common_integers with those common “heroes”, in a descending honor roll.

No number repeats nor resists the gravitational pull! Make sure you deliver in the right format:

Each set can contain up to 
1
0
4
10 
4
  integers, ranging from 
−
1
0
6
−10 
6
  to 
1
0
6
10 
6
  inclusive.
Output should be a list of unique integers existing in both sets in descending order.

'''

def intersecting_elements(set1, set2) :
# {
    result = sorted(list(set1 & set2))
    print(result[::-1])
# }

print(intersecting_elements({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}))
# Expected output: [10, 9, 8, 7, 6, 5]

# print(intersecting_elements({-1, -2, -3, -4, -5}, {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}))
# Expected output: [-1, -2, -3, -4, -5]

# print(intersecting_elements({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10}))
# Expected output: []

'''

********
BONEYARD
********

Good try, but that's not exactly right. Your solution is a bit more complex than needed. Try using the intersection operator & to find common elements between the sets. Then, sort the result in descending order. Need any help with that? 🤔

tmp1 = set1 - set2
    tmp2 = set2 - set1
    tmp3 = set(list(set1) + list(set2))
    result = sorted(list(tmp3 - tmp2 - tmp1))
    
    print (result[::-1])


https://www.analyticsvidhya.com/blog/2020/02/joins-in-pandas-master-the-different-types-of-joins-in-python/

# tmp1 = list(set1)
    # tmp2 = list(set2)
    # tmp = tmp1 + tmp2

    # print(tmp)


    # implement this

    # print (list(set2 in set1))
    # pass
    # for i in range(len(list((set1)))) :
    # {
    #    print(i)
    # }

    # tmp = list(set.items())

    

'''