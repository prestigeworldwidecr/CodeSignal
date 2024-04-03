/*

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You're given two integers, n and m. Find position of the rightmost bit in which they differ in their binary representations (it is guaranteed that such a bit exists), counting from right to left.

Return the value of 2position_of_the_found_bit (0-based).

Example

For n = 11 and m = 13, the output should be
solution(n, m) = 2.

1110 = 10112, 1310 = 11012, the rightmost bit in which they differ is the bit at position 1 (0-based) from the right in the binary representations.
So the answer is 21 = 2.

For n = 7 and m = 23, the output should be
solution(n, m) = 16.

710 = 1112, 2310 = 101112, i.e.

00111
10111
So the answer is 24 = 16.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
0 ≤ n ≤ 2^30.

[input] integer m

Guaranteed constraints:
0 ≤ m ≤ 2^30,
n ≠ m.

[output] integer

*/

function differentRightMostBit(n, m)
{
    let pos = 0;
    let result = 0;

    for (let i = 0; i < n.length; i++)
    {
        if (n[i] != m[i])
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

    return differentRightMostBit(n, m);
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

let n = 11;
let m = 13;     // 2
n = 7;
m = 23;     // the output should be solution(n, m) = 16.

// console.log(determineZeros(n, m));
// console.log(wtv);

/*

********
BONEYARD
********

// console.log(n, m);
    // console.log(n.length, pos);
    // console.log(result);
// console.log(n[i]);
        
    // let cnt = 0;

    // console.log(n, m);

    // send sorted array
    // determine max length
    // add empty zeroes to the shorter string

function createDescendingArray(n, m)
{

}

*/