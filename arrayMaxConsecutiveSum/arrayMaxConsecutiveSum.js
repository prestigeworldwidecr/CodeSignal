/*

Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer inputArray

Array of positive integers.

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
1 ≤ inputArray[i] ≤ 1000.

[input] integer k

An integer (not greater than the length of inputArray).

Guaranteed constraints:
1 ≤ k ≤ inputArray.length.

[output] integer

The maximal possible sum.

*/

function maxPower(inputArray, k)
{
    var sum = -1;
    var max = 0;
    var babyK = []; // array containing 0 ... k - 1
    babyK.length = k;

    for (var i = 0; i < babyK.length; i++)
    {
        // console.log("i: ", i, " k: ", k);
        
        babyK[i] = i;
    }

    for (var i = 0; i < inputArray.length; i++)
    {
        // console.log("i: ", i, " j: ", j, " sum: ", sum);
        
        for (var j = i; j < babyK.length; j++)
        {
            
            sum = inputArray[j] + sum;
            console.log("i: ", i, " j: ", j, " sum: ", sum, " inputArray[j]: ", inputArray[j]);
        }
    }

    return max;

}

function solution(inputArray, k) 
{

}


var inputArray = [2, 3, 5, 1, 6];
var k = 2;  // the output should be solution(inputArray, k) = 8.

maxPower(inputArray, k);

/*

********
BONEYARD
********

*/