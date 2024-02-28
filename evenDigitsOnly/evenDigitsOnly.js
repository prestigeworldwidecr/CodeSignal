/*

Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 109.

[output] boolean

true if all digits of n are even, false otherwise.

*/

function evenDigitsOnly(n)
{
    let tmp = n.toString();
    let result = false;

    for (let i = 0; i < tmp.length; i++)
    {
        if (Number(tmp [i]) % 2 != 0)
        {
            return false;
        }

        else
        {
            result = true;
        }
    }

    return result;
}

function solution(n) 
{
    return evenDigitsOnly(n);
}

// console.log(tmp);
// let n = 248622;  // the output should be solution(n) = true;
let n = 642386;  // the output should be solution(n) = false.

console.log(evenDigitsOnly(n));

/*

********
BONEYARD
********

*/