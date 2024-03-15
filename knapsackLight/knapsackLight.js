/*

You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

Example

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
solution(value1, weight1, value2, weight2, maxW) = 10.

You can only carry the first item.

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
solution(value1, weight1, value2, weight2, maxW) = 16.

You're strong enough to take both of the items with you.

For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
solution(value1, weight1, value2, weight2, maxW) = 7.

You can't take both items, but you can take any of them.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer value1

Guaranteed constraints:
2 ≤ value1 ≤ 20.

[input] integer weight1

Guaranteed constraints:
2 ≤ weight1 ≤ 10.

[input] integer value2

Guaranteed constraints:
2 ≤ value2 ≤ 20.

[input] integer weight2

Guaranteed constraints:
2 ≤ weight2 ≤ 10.

[input] integer maxW

Guaranteed constraints:
1 ≤ maxW ≤ 20.

[output] integer

*/

function grabbingHands(value1, weight1, value2, weight2, maxW) 
{
    var totalValue = value1 + value2;
    var totalWeight = weight1 + weight2;

    if (totalWeight <= maxW)
    {
        return totalValue;
    }

    else if (maxW < weight1 && maxW < weight2)
    {
        return 0;
    }

    else if (weight1 <= maxW && weight2 <= maxW)
    {
        if (value1 > value2)
        {
            return value1;
        }

        else
        {
            return value2;
        }
    }

    else if (weight1 <= maxW && maxW < weight2)
    {
        return value1;
    }

    else
    {
        return value2;
    }

}

function solution(value1, weight1, value2, weight2, maxW) 
{
    return grabbingHands(value1, weight1, value2, weight2, maxW);
}

var value1 = 10;
var weight1 = 5;
var value2 = 6;
var weight2 = 4;
var maxW = 8;   // solution(value1, weight1, value2, weight2, maxW) = 10

var value1 = 10;
var weight1 = 5;
var value2 = 6;
var weight2 = 4;
var maxW = 9;   // solution(value1, weight1, value2, weight2, maxW) = 16

var value1 = 5;
var weight1 = 3;
var value2 = 7;
var weight2 = 4;
var maxW = 6;   // solution(value1, weight1, value2, weight2, maxW) = 7

console.log(solution(value1, weight1, value2, weight2, maxW));

/*

********
BONEYARD
********

*/