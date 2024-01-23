// makeArrayConsecutive2.js

/*

Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.

[input] array.integer statues

An array of distinct non-negative integers.

Guaranteed constraints:
1 ≤ statues.length ≤ 10,
0 ≤ statues[i] ≤ 20.

[output] integer

The minimal number of statues that need to be added to existing statues such that it contains every integer size from an interval [L, R] (for some L, R) and no other sizes.

*/

function solution(statues)
{
    statues = statues.sort((a,b) => a-b);       // (a,b) => a-b
    cnt = 0;
    dif = 0;

    console.log(statues);

    for(i = 0; i < statues.length - 1; i++)
    {
        if (statues[i] == statues[i + 1])
        {
            //
        }

        else
        {
            dif = statues[i + 1] - statues[i] - 1;
            cnt = cnt + dif;
        }

        // console.log("i: ", i, " statues[i]: ", statues[i], " statues[i + 1]: ", statues[i + 1], " dif: ", dif, " cnt: ", cnt);

    }

    return cnt;
}

s1 = [6, 2, 3, 8];                      // 3
s2 = [0, 3];                            // 2
s3 = [5, 4, 6];                         // 0
s4 = [6, 3];                            // 2
s5 = [1];                               // 0
s6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];   // 0
s7 = [4, 2, 7, 18];                     // 13

// console.log(solution(s1));   // 3
// console.log(solution(s2));   // 2
// console.log(solution(s3));   // 0
// console.log(solution(s4));   // 2
// console.log(solution(s5));   // 0
// console.log(solution(s6));      //
console.log(solution(s7));      //

/*

********
BONEYARD
********


/* 
    statues         cnt
    [6, 2, 3, 8]    3
    [0, 3]          2
    [5, 4, 6]       0
    [6, 3]          2
    [1]             0

    // console.log(statues.sort());
    // console.log("i: ", i, " j: ", j, " k: ", k, " cnt: ", cnt);
    // console.log("statues.length: ", statues.length);        
    // console.log("i: ", i, " j: ", j, " k: ", k, " dif: ", dif, " cnt: ", cnt);

*/