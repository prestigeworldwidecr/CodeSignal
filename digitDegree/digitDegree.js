/*

Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
solution(n) = 0;
For n = 100, the output should be
solution(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
5 ≤ n ≤ 109.

[output] integer

*/

function digitDegree(n, cnt)
{
    tmp = n.toString();
    
    if (tmp.length == 1)
    {
        return 0 + cnt;
    }

    else
    {
        return 1 + digitDegree(sumIndividualDigit(n), 0);
    }

}

function sumIndividualDigit(n)
{
    var tmp = n.toString();
    var sum = 0;

    for (var i = 0; i < tmp.length; i++)
    {
        sum = sum + Number(tmp[i]);
    }

    return sum;
}

function solution(n) 
{
    return digitDegree(n, 0);
}


var n = 5;  // the output should be solution(n) = 0;
// var n = 100 // the output should be solution(n) = 1.
// var n = 91  // the output should be solution(n) = 2.

// console.log(sumIndividualDigit(n));


/*

********
BONEYARD
********

*/