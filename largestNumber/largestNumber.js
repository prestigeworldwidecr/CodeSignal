/*

Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
solution(n) = 99.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 9.

[output] integer

The largest integer of length n.

*/

function solution(n) 
{
    let result = "";

    for (let i = 0; i < n; i++)
    {
        result = result + "9";
    }

    // console.log(result);
    return Number(result);
}

// solution(4);

/*

********
BONEYARD
********

*/