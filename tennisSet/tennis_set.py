"""

In tennis, the winner of a set is based on how many games each player wins. The first player to win 6 games is declared the winner unless their opponent had already won 5 games, in which case the set continues until one of the players has won 7 games.

Given two integers score1 and score2, your task is to determine if it is possible for a tennis set to be finished with a final score of score1 : score2.

Example

For score1 = 3 and score2 = 6, the output should be
solution(score1, score2) = true.

Since player 1 hadn't reached 5 wins, the set ends once player 2 has won 6 games.

For score1 = 8 and score2 = 5, the output should be
solution(score1, score2) = false.

Since both players won at least 5 games, the set would've ended once one of them won the 7th one.

For score1 = 6 and score2 = 5, the output should be
solution(score1, score2) = false.

This set will continue until one of these players wins their 7th game, so this can't be the final score.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer score1

Number of games won by the 1st player, non-negative integer.

Guaranteed constraints:
0 ≤ score1 ≤ 10.

[input] integer score2

Number of games won by the 2nd player, non-negative integer.

Guaranteed constraints:
0 ≤ score2 ≤ 10.

[output] boolean

true if score1 : score2 represents a possible score for an ended set, false otherwise.

"""

def solution(score1, score2) :
# {
    a = [score1, score2]

    a = sorted(a)
    score2 = a [0]
    score1 = a [1]
    
    if (score1 == 7 and (score2 == 5 or score2 == 6)) :
    # {
        return True
    # }

    elif (score1 == 6 and score2 <= 4) :
    # {
        return True
    # }

    else :
    # {
        return False
    # }

# }

score1 = 7
score2 = 5

print(solution(score1, score2))

"""

********
BONEYARD
********

"""