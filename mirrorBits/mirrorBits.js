/*

Reverse the order of the bits in a given integer.

Example

For a = 97, the output should be
solution(a) = 67.

97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.

For a = 8, the output should be
solution(a) = 1.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer a

Guaranteed constraints:
5 ≤ a ≤ 105.

[output] integer

*/

function mirrorBits(n)
{
    let tmp = n.toString(2);

    tmp = tmp.split("");
    tmp = tmp.reverse();
    tmp = tmp.join(",");
    tmp = tmp.replaceAll(",", "");

    // console.log(parseInt(tmp, 2));
    return parseInt(tmp, 2);
}

function solution(a) 
{
    return mirrorBits(a);
}

let a = 8;      // the output should be solution(a) = 1.

// mirrorBits(a);

/*

********
BONEYARD
********

*/