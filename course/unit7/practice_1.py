'''

Alright, my friend! Time to put on your coding cap!

Imagine you are in a corporate setting and you have a list of employee votes represented as integers like 
[
a
1
,
a
2
,
.
.
.
,
a
n
]
[a 
1
​
 ,a 
2
​
 ,...,a 
n
​
 ]. These integers actually represent the IDs of your fellow employees. And yes, people can indeed vote for themselves!

An employee gets elevated to the exclusive board member position only if they bag at least n / 3 votes, with n being the total number of votes. Your task: find out the ID of this popular employee. If no one hits the vote mark, return -1. If multiple employees received at least n / 3 votes, return any of them!

The votes are delivered to you in list format. As an illustration, [1, 2, 3, 3, 3] means employees 1 and 2 voted for themselves, and employee 3 received three votes. Hang tight-there can be edge cases, such as no votes or everybody voting for themselves.

Your end goal is to return the lucky candidate's ID if they secure a seat on the board. If no one qualifies, return -1. Got it, superstar? Now it's time to put your coding prowess to the test and sort out this corporate election pronto!

'''

def elect_board_member(votes) :
# {
    # implement this
    count_dict = {}
    # results = []

    for element in votes :
    # {  
        count_dict[element] = count_dict.get(element, 0) + 1
        # print(element, count_dict[element])

        if count_dict[element] > len(votes) // 3 :
        # {
            return element
            # results.append(element)
        # }

        else :
        # {
            None
        # }

    # }

    return -1

# }

print(elect_board_member([1, 2, 3, 3, 3]))  # Expected output: 3
print(elect_board_member([1, 2, 3, 4, 5]))  # Expected output: -1
print(elect_board_member([1, 1, 1, 2, 2, 3, 3, 3]))  # Expected output: 1

'''

********
BONEYARD
********


    if (len(results) > 0) :
    # {
        return list(set(results))
    # }

    else :
    # {
        return -1
    # }

'''