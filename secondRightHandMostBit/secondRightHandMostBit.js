/*

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Presented with the integer n, find the 0-based position of the second rightmost zero bit in its binary representation (it is guaranteed that such a bit exists), counting from right to left.

Return the value of 2^position_of_the_found_bit.

Example

For n = 37, the output should be
solution(n) = 8.

37 (sub) 10 = 100101 (sub) 2. The second rightmost zero bit is at position 3 (0-based) from the right in the binary representation of n.
Thus, the answer is 23 = 8.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
4 ≤ n ≤ 2^30.

[output] integer

*/

function secondRightMostHandBit(n)
{
    let pos = 0;
    let tmp = n.toString(2);
    let cnt = 0;

    for (let i = tmp.length - 1; i >= 0; i--)
    {
        if (tmp [i] == 0)
        {
            cnt++;

            if (cnt == 2)
            {
                pos = i;
            }

            else
            {
                //
            }
        }

        else
        {

        }

    }

    tmp = tmp.length - pos - 1;
    tmp = Math.pow(2, tmp);
    // console.log(tmp);
    return tmp;

}

function solution(n) 
{
    return secondRightMostHandBit(n);
}

let n = 37;     // the output should be solution(n) = 8.

// console.log(solution(n));
// secondRightMostHandBit(n);

/*

********
BONEYARD
********

// console.log(tmp[i]);
        // console.log(tmp.length);
// console.log(Math.pow(Number(n.toString(2).length - 3), 2));
    // let tmp = Math.pow(2, n.toString(2).length - 3);

    // tmp = Math.pow(2, tmp);
    // console.log(tmp);
switch(n.toString(2).length)
    {
        case 3:
        return 1;
        case 4:
        return 2;
        case 5:
        return 4;
        case 6:
        return 8;
        case 7:
        return 16;
        case 8:
        return 32;
    }

*/
  