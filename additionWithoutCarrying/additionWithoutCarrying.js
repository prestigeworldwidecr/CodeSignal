/*

A little child is studying arithmetic. They have just learned how to add two integers, written one below another, column by column. But the child always forgets about the important part - carrying.

Given two integers, your task is to find the result that the child will get.

Note: The child had learned from this site, so feel free to check it out too if you are not familiar with column addition.

Example

For param1 = 456 and param2 = 1734, the output should be
solution(param1, param2) = 1180.

   456
  1734
+ ____
  1180
The child performs the following operations from right to left:

6 + 4 = 10 but the child forgets about carrying the 1 and just writes down the 0 in the last column
5 + 3 = 8
4 + 7 = 11 but the child forgets about the leading 1 and just writes down 1 under 4 and 7.
There is no digit in the first number corresponding to the leading digit of the second one, so the child imagines that 0 is written before 456. Thus, they get 0 + 1 = 1.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer param1

A non-negative integer.

Guaranteed constraints:
0 ≤ param1 < 10^5.

[input] integer param2

A non-negative integer.

Guaranteed constraints:
0 ≤ param2 < 6 · 10^4.

[output] integer

The result that the little child will get by using column addition without carrying.

*/

function addZeros(d, len)
{    
    for (let i = 0; i < len; i++)
    {
        d = "0" + d;
    }

    return d;
}

function determineZeros(n, m)
{
    n = n.toString();
    m = m.toString();
    
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
        // console.log
    }

    return additionWithoutCarrying(n, m);

}

function additionWithoutCarrying(param1, param2)
{
    let len = -1;
    let result = "";

    for (let i = 0; i < param1.length; i++)
    {
        let tmp1 = parseInt(param1[i]) + parseInt(param2[i]);
        tmp1 = tmp1.toString();
        len = tmp1.length - 1;
        result = result + tmp1[len];
    }
    return result;
}

function solution(param1, param2) 
{

}

let param1 = 456;
let param2 = 1734;  // the output should be solution(param1, param2) = 1180.

console.log(determineZeros(param1, param2));

/*

********
BONEYARD
********


    // console.log(result);
    // console.log(param1, param2);
    // console.log(param1[0] + param2[1]);
    
        // console.log(tmp1[len]);
//         console.log(tmp1);
        // result = result + tmp;
        // console.log(tmp);
// console.log(d, len);
        // console.log(d);
    // console.log(n.length, m.length);
// console.log(b);
n = n.toString(2);
    m = m.toString(2);

    // console.log(n, m);


*/