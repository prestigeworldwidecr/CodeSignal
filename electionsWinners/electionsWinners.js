/*

Elections are in progress!

Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.

Example

For votes = [2, 3, 5, 2] and k = 3, the output should be
solution(votes, k) = 2.

The first candidate got 2 votes. Even if all of the remaining 3 candidates vote for him, he will still have only 5 votes, i.e. the same number as the third candidate, so there will be no winner.
The second candidate can win if all the remaining candidates vote for him (3 + 3 = 6 > 5).
The third candidate can win even if none of the remaining candidates vote for him. For example, if each of the remaining voters cast their votes for each of his opponents, he will still be the winner (the votes array will thus be [3, 4, 5, 3]).
The last candidate can't win no matter what (for the same reason as the first candidate).
Thus, only 2 candidates can win (the second and the third), which is the answer.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer votes

A non-empty array of non-negative integers. Its ith element denotes the number of votes cast for the ith candidate.

Guaranteed constraints:
4 ≤ votes.length ≤ 105,
0 ≤ votes[i] ≤ 104.

[input] integer k

The number of voters who haven't cast their vote yet.

Guaranteed constraints:
0 ≤ k ≤ 105.

[output] integer

*/

function votesPlusK(votes, k)
{
    var tmp = [...votes];

    // console.log(tmp);

    for (var i = 0; i < tmp.length; i++)
    {
        tmp [i] = tmp [i] + k;
    }

    // console.log("$", tmp, " k: ", k);

    return tmp;

}

function winnerCount(votes)
{
    var max = Math.max(...votes);
    var cnt = 0;

    // console.log("!", " max: ", max, " @votes: ", votes);

    for (var i = 0; i < votes.length; i++)
    {
        if (votes[i] == max)
        {
            // console.log("i: ", i, " max: ", max, " votes[i]", votes[i]);
            cnt++;
        }

        else
        {
            // 
        }

    }

    return cnt;
}

function electionsWinners(votes, k)
{
    var max = Math.max(...votes);
    var cnt = 0;
    var cntMax = 0; // count of candidates w/votes equal to max
    var tmp = votesPlusK(votes, k);
    console.log("#", tmp);
    var tmp1 = winnerCount(tmp);

    // console.log(votes, max);

    for (var i = 0; i < votes.length; i++)
    {
        tmp = votes[i] + k;

        if (max < tmp)
        {
            cnt++;
        }

        else
        {
            //
        }

    }

    if (tmp1 > 1 && k == 0)
    {
        // console.log("%");
        return 0;
    }

    else if (tmp1 == 1 && k == 0)
    {
        return 1;
    }

    else
    {
        return cnt;
    }

}

function solution(votes, k) 
{
    return electionsWinners(votes, k);
}

var votes = [2, 3, 5, 2];
var k = 3;  // the output should be solution(votes, k) = 2
votes = [1, 3, 3, 1, 1];    // 0
k = 0;
votes = [1, 1, 1, 1] // 0
k = 0;
votes = [5, 1, 3, 4, 1];    // 1
k = 0;
votes = [2, 3, 5, 2];   // 2
k = 3;
votes = [3, 1, 1, 3, 1] // 2
k = 2;


console.log(electionsWinners(votes, k));
// console.log(isElectionTie(votes, k));

/*

********
BONEYARD
********

// If two or more candidates receive the same (maximum) number of votes
// assume there is no winner at all.
function isElectionTie(votes, k)
{
    var max = Number.MIN_SAFE_INTEGER;
    var maxCnt = 0;

    // console.log(tmp);
    max = Math.max([...tmp]);

    for (var i = 0; i < tmp.length; i++)
    {
        if (tmp [i] == max)
        {
            maxCnt++;

            if (maxCnt > 1)
            {
                return true;
            }

            else
            {
                result = false;
            }
        }

        else
        {
            result = false;
        }

    }

    return result;

}

        else if (tmp == max)
        {
            cntMax++;
        }

    if (cntMax > 1)
    {
        return 0;
    }

    else if (cntMax == 1)
    {
        return 1;
    }

    else
    {
        return cnt;
    }

*/