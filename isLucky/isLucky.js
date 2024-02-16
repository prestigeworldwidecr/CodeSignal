/*

Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 10^6.
10 ≤ n < 999999
2, 4 or 6 digits

[output] boolean

true if n is a lucky ticket number, false otherwise.

*/

// integer -> array of numbers

function isLucky2digit(n)
{
    var tmp = null;

    tmp = [parseInt(n[0]), parseInt(n[1])];

    return (tmp [0] == tmp [1]);
}

function isLucky4digit(n)
{
    var tmp = null;

    // console.log(tmp);

    tmp = [parseInt(n[0]), parseInt(n[1]), parseInt(n[2]), parseInt(n[3])];

    return (tmp [0] + tmp [1]) == (tmp [2] + tmp [3]);
}

function isLucky6digit(n)
{
    var tmp = null;

    tmp = [parseInt(n[0]), parseInt(n[1]), parseInt(n[2]), parseInt(n[3]), parseInt(n[4]), parseInt(n[5])];

    return (tmp [0] + tmp [1] + tmp [2]) == (tmp [3] + tmp [4] + tmp [5]);
}

function solution(n) 
{
    var result = false;
    var tmp = "";

    tmp = n.toString();

    if (tmp.length == 2)
    {
        result = isLucky2digit(tmp);
    }

    else if (tmp.length == 4)
    {
        result = isLucky4digit(tmp);
    }

    else if (tmp.length == 6)
    {
        result = isLucky6digit(tmp);
    }

    else
    {
        return false;
    }

    // console.log(result);
}

n1 = 1230;
n2 = 239017;
n3 = 31;

solution(n2);

/*

********
BONEYARD
********

*/