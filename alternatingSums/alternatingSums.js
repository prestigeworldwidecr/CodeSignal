/*

Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

Example

For a = [50, 60, 60, 45, 70], the output should be
solution(a) = [180, 105].

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 105,
45 ≤ a[i] ≤ 100.

[output] array.integer

*/

function alternatingSums(a)
{
    var i = 0;
    var isEven = false;
    var evenSum = 0;
    var oddSum = 0;
    var result = [0, 0];

    for(i; i < a.length; i++)
    {
        isEven = (i + 1) % 2;

        if (isEven)
        {
            evenSum = evenSum + a[i];
        }

        else
        {
            oddSum = oddSum + a[i];
        }
    }

    result [0] = evenSum;
    result [1] = oddSum;

    return result;
}

function solution(a) 
{
    return alternatingSums(a);
}

/*

********
BONEYARD
********

a = [50, 60, 60, 45, 70];   // solution(a) = [180, 105]

alternatingSums(a);

    // console.log("i: ", i, " even? ", isEven);
    // console.log("evenSum: ", evenSum, " oddSum: ", oddSum);
    // console.log(result);

*/