/*

You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other. What is the value of the third integer?

Example

For a = 2, b = 7, and c = 2, the output should be
solution(a, b, c) = 7.

The two equal numbers are a and c. The third number (b) equals 7, which is the answer.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer a

Guaranteed constraints:
1 ≤ a ≤ 109.

[input] integer b

Guaranteed constraints:
1 ≤ b ≤ 109.

[input] integer c

Guaranteed constraints:
1 ≤ c ≤ 109.

[output] integer

*/

function extraNumber(a, b, c)
{
    let result = a;

    if (a == b)
    {
        result = c;
    }

    else if (a == c)
    {
        result = b;
    }

    else
    {
        result = a;
    }

    return result;

}

function solution(a, b, c) 
{
    return extraNumber(a, b, c);
}

let a = 2;
let b = 7;
let c = 2;      // the output should be solution(a, b, c) = 7.

console.log(extraNumber(a, b, c));

/*

********
BONEYARD
********



*/