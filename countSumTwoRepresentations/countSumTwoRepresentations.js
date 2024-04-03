/*

Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2, and r = 4, the output should be
solution(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

A positive integer.

Guaranteed constraints:
5 ≤ n ≤ 109.

[input] integer l

A positive integer.

Guaranteed constraints:
1 ≤ l ≤ r.

[input] integer r

A positive integer.

Guaranteed constraints:
l ≤ r ≤ 109,
r - l ≤ 106.

[output] integer

*/

function createInclusiveArray(l, r)
{
    let a = Array();

    for (let i = l; i <= r; i++)
    {
        a.push(i);
    }

    return a;
}

function countSumTwoRepresentations(a, n)
{
    let b = Array();

    for (let i = 0; i < a.length; i++)
    {
        let tmp = n - a [i];
        
        if (a.includes(tmp))
        {
            let tmp1 = "";
            
            if (a [i] < tmp)
            {
                tmp1 = a [i] + "" + tmp;
            }

            else
            {
                tmp1 = tmp + "" + a [i];
            }
            
            // console.log(tmp1);
            b.push(tmp1);

        }

        else
        {
            // 
        }

    }

    result = [...new Set(b)];
    // console.log(result);
    return result.length;

}


function solution(n, l, r) 
{
    return countSumTwoRepresentations(createInclusiveArray(l, r), n);
}

let n = 6;
let l = 2;
let r = 4;      // the output should be solution(n, l, r) = 2.
// n = 93;
// l = 24;
// r = 58;

// countSumTwoRepresentations(createInclusiveArray(l, r), n);


/*

********
BONEYARD
********

// console.log(createInclusiveArray(l, r).includes(24));
// test();

// console.log("!");
    // console.log(a);
// let result = "";
            // tmp1.sort();
            // ]).toString();
            // if (!b.includes(tmp1))
            // {
                // b.push(tmp1);
            // }
            
            // else
            // {
                //
            // }
        // console.log (tmp1);

function test()
{
    tmp = [[2, 4], [3, 3], [4, 2]];
    
    uniq = [...new Set(tmp)];

    console.log(uniq);
}

function createInclusiveArray(l, r)
{
    // console.log("!");
    let a = Array();

    for (let i = l; i <= r; i++)
    {
        a.push(i);
    }

    // console.log(a);
    return a;
}

function countSumTwoRepresentations(a, n)
{
    let b = [...a];
    let cnt = 0;

    b.reverse();

    console.log(a, b);

    for (let i = 0; i < Math.ceil(a.length / 2); i++)
    {
        console.log("!");
        
        let sum = a [i] + b [i];

        if (sum == n)
        {
            console.log(a [i], b [i], n);
            cnt++;
        }

        else
        {
            //
        }
    }

    console.log(cnt);
    
    return cnt;
}

*/