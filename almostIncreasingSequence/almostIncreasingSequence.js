// almostIncreasingSequence.js

/*

Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
solution(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

*/

function solution1(sequence)
{
    cnt = 0;            // count out of sequence
    currCnt = 0;        // count when currentMax overwhelmed
    currentMax = -999999;

    for (i = 0; i < sequence.length; i++)
    {
        if (sequence [i] >= sequence [i + 1])
        {
            cnt++;
        }

        else if (cnt > 1 || currCnt > 1)
        {
            return false;
        }

        else if (sequence [i + 1] <= currentMax)
        {
            // 
        }

        else
        {
            currentMax = sequence [i + 1];
            currCnt++;
        }

        console.log("i: ", i, " sequence [i]: ", sequence [i], " sequence [i + 1]: ", sequence [i + 1], " cnt: ", cnt,  " currCnt: ",  currCnt, " currentMax: ", currentMax);
    }

    return true;
}

// different strategy using prevMax, currMax
function solution2(sequence)
{
    prevMax = -999999;
    currentMax = -999999;

    for (i = 0; i < sequence.length; i++)
    {
        if (i == 0)
        {
            console.log("*1");
            
            if (sequence [i] < sequence [i + 1])
            {
                prevMax = sequence [i + 1];
                currentMax = sequence [i + 1];
            }

            else
            {
                prevMax = sequence [i];
                currentMax = sequence [i];
            }
        }

        else if ( (sequence [i] >= sequence [i + 1]) &&
                (sequence [i] >= currentMax) &&
                (sequence [i] >= prevMax) )
        {
            console.log("*2");
            return false;
        }

        else
        {
            console.log("*3");
            prevMax = currentMax;
            currentMax = sequence [i + 1];
        }

        console.log("i: ", i, " sequence [i]: ", sequence [i], " sequence [i + 1]: ", sequence [i + 1], " currentMax: ", currentMax, " prevMax: ", prevMax);

        /*

        if (sequence [i] >= sequence [i + 1])
        {
            cnt++;
        }

        
        else if (sequence [i + 1] <= currentMax)
        {
            // 
        }

        else
        {
            currentMax = sequence [i + 1];
        }

        */

    }

    return true;
}

s1 = [1, 3, 2, 1];                          // false
s2 = [1, 3, 2];                             // true
s3 = [1, 2, 1, 2];                          // false
s4 = [1, 2, 3, 4, 5, 3, 5, 6];              // false
s5 = [40, 50, 60, 10, 20, 30]               // false
s6 = [1, 2, 5, 3, 5];                       // 
s7 = [1, 2, 3, 4, 99, 5, 6];                // 
s8 = [123, -17, -5, 1, 2, 3, 12, 43, 45]    // 

console.log(solution1(s3));

/*

********
BONEYARD
********

// [1, 3, 2, 1]     // false
// [1, 3, 2]        // true

// one element outta order, cnt++
// > 1, outta order return false

*/