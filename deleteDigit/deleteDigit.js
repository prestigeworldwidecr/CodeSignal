/*

Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
10 ≤ n ≤ 10^6.

[output] integer

*/

function deleteDigit(n)
{
    var tmp = n.toString().split("");
    var cur = Number(tmp [0]);
    var next = Number(tmp [1]);
    var result = "";
    var flag = true;
    
    // console.log(tmp);

    if (tmp.length == 2)
    {
        if (cur > next)
        {
            return cur;
        }

        else
        {
            return next;
        }

    }

    else
    {
        //
    }

    for (var i = 0; i < tmp.length; i++)
    {
        cur = Number(tmp [i]);
        next = Number(tmp [i + 1]);

        if (next > cur && flag)
        {
            flag = false;
        }

        else
        {
            result = result + cur.toString();
        }

    }

    // console.log(Number(result));
    return Number(result);
}


function solution(n) 
{
    return deleteDigit(n);
}

var n = 152;    // the output should be solution(n) = 52
var n = 1001;   // the output should be solution(n) = 101
var n = 10;     // 1

console.log(deleteDigit(n));

/*

********
BONEYARD
********

*/