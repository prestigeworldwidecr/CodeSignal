/*

You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you construct an array of all the integers from a to b inclusive. You need to count the number of 1s in the binary representations of all the numbers in the array.

Example

For a = 2 and b = 7, the output should be
solution(a, b) = 11.

Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111], which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer a

Guaranteed constraints:
0 ≤ a ≤ b.

[input] integer b

Guaranteed constraints:
a ≤ b ≤ 10.

[output] integer

*/

function buildInclusiveArray(a, b)
{
    let tmp = Array();

    for (let i = a; i <= b; i++)
    {
        tmp.push(i.toString(2));
    }

    return tmp;
}

function rangeBitCount(a)
{
    let cnt = 0;

    for (let i = 0; i < a.length; i++)
    {
        let tmp = a[i];
        
        for (let j = 0; j < tmp.length; j++)
        {
            if (tmp.charAt(j) == 1)
            {
                cnt++;
            }

            else
            {
                //
            }
        }
    }

    return cnt;
}

function solution(a, b) 
{
    return rangeBitCount(buildInclusiveArray (a, b));
}

let a = 2;
let b = 7;      // the output should be solution(a, b) = 11.

// rangeBitCount(buildInclusiveArray (a, b));

/*

********
BONEYARD
********

// console.log(i);
    // console.log(tmp);
// console.log(cnt);
// console.log(a);
        // console.log(tmp);
                // console.log(a[cnt][i]);

*/