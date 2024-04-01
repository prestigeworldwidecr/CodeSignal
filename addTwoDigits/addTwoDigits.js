/*

You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
solution(n) = 11.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

A positive two-digit integer.

Guaranteed constraints:
10 ≤ n ≤ 99.

[output] integer

The sum of the first and second digits of the input number.

*/

function solution(n) 
{
    let tmp = n.toString().split("");
    let result = Number(tmp [0]) + Number(tmp [1]);
    
    return result;
}

// solution(29);

/*

********
BONEYARD
********

*/