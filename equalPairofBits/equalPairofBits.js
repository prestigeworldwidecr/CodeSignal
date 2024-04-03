/*

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You're given two integers, n and m. Find position of the rightmost pair of equal bits in their binary representations (it is guaranteed that such a pair exists), counting from right to left.

Return the value of 2^position_of_the_found_pair (0-based).

Example

For n = 10 and m = 11, the output should be
solution(n, m) = 2.

10 (sub) 10 = 1010 (sub) 2, 11 (sub) 10 = 1011(sub) 2, the position of the rightmost pair of equal bits is the bit at position 1 (0-based) from the right in the binary representations.
So the answer is 2^1 = 2.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
0 ≤ n ≤ 2^30.

[input] integer m

Guaranteed constraints:
0 ≤ m ≤ 2^30.

[output] integer

*/


function equalRightMostBit(n, m)
{
    let pos = 0;
    let result = 0;

    for (let i = 0; i < n.length; i++)
    {
        if (n[i] == m[i])
        {
            pos = i;
        }

        else
        {
            //
        }

    }

    result = n.length - pos - 1;
    result = Math.pow(2, result);

    // console.log(result);
    
    return result;
}

function determineZeros(n, m)
{
    n = n.toString(2);
    m = m.toString(2);

    // console.log(n, m);

    if (n.length < m.length)
    {
        n = addZeros(n, m.length - n.length);
    }

    else if (m.length < n.length)
    {
        m = addZeros(m, n.length - m.length);
    }

    else
    {
        //
    }

    // console.log(n, m);

    return equalRightMostBit(n, m);
}

function addZeros(b, len)
{
    for (let i = 0; i < len; i++)
    {
        b = "0" + b;
    }

    // console.log(b);
    return b;
}

function solution(n, m) 
{
    return determineZeros(n, m);
}

let n = 10;
let m = 11;     // the output should be solution(n, m) = 2.

/*

********
BONEYARD
********

*/