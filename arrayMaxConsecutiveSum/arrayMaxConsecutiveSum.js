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
    var max = Number.MIN_SAFE_INTEGER;
    var sum = 0;
    var tmp = [...inputArray];

    for (var i = 0; i < inputArray.length; i++)
    {
        if (sum > max)
        {
            max = sum;
        }

        else
        {
            // 
        }
        
        tmp = tmp.slice(i, i + k);
        // console.log("tmp: ", tmp, " inputArray: ", inputArray, " sum: ", sum);
        sum = 0;

        for (var j = 0; j < tmp.length; j++)
        {
            sum = sum + tmp[j];
        }

        tmp = [...inputArray];

    }

    // console.log(max);
    return max;

}

function solution(inputArray, k) 
{
    return maxPower(inputArray, k);
}


var inputArray = [2, 3, 5, 1, 6];
var k = 2;  // the output should be solution(inputArray, k) = 8.

maxPower(inputArray, k);

/*

********
BONEYARD
********

// var babyK = []; // array containing 0 ... k - 1
    // babyK.length = k;
    for (var i = 0; i < babyK.length; i++)
    {
        // console.log("i: ", i, " k: ", k);
        
        babyK[i] = i;
    }
        
        // consoleinputArray
        
        // console.log("i: ", i, " j: ", j, " sum: ", sum);
        
        if 

        for (var j = 0; j < babyK.length; j++)
        {
            // console.log("!i: ", i, " j: ", j, " sum: ", sum, " inputArray[j]: ", inputArray[j]);
            sum = inputArray[i] + sum;
            // console.log("@i: ", i, " j: ", j, " sum: ", sum, " inputArray[j]: ", inputArray[j]);
        }

*/