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
    var tmp = 0;
}

function isLucky4digit(n)
{
    
}

function isLucky5digit(n)
{
    
}

function solution(n) 
{
    var tmp = "";

    tmp = n.toString();

    // console.log(tmp);

    if (tmp.length == 2)
    {
        isLucky2digit(n);
    }

    else if (tmp.length == 4)
    {
        isLucky4digit(n);
    }

    else if (tmp.length == 6)
    {
        isLucky6digit(n);
    }

    else
    {
        return false;
    }
}

n1 = 1230;
n2 = 239017;

solution(n1);

/*

********
BONEYARD
********

*/