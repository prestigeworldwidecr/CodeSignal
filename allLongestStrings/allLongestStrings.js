// allLongestStrings.js

/*

Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.

*/

function maxLengthString(inputArray)
{
    var i = 0;
    var tmp = null;
    var max = -999999;
    
    for (i; i < inputArray.length; i++)
    {
        tmp = inputArray[i].length;

        if (tmp > max)
        {
            max = tmp;
        }

        else
        {
            // 
        }
    }

    return max;

}

function solution(inputArray) 
{
    var i = 0;
    var mls = maxLengthString(inputArray);
    var result = [];

    for (i; i < inputArray.length; i++)
    {
        // console.log(inputArray[i]);

        if (inputArray[i].length == mls)
        {
            result.push(inputArray[i]);
        }

        else
        {
            //
        }

    }

    return result;
}

// console.log(solution(["aba", "aa", "ad", "vcd", "aba"]));
console.log(solution(["aba", "aa", "ad", "vcd", "aba"]));


/*

********
BONEYARD
********

// var i = inputArray.length

    // console.log(i);
    // console.log(inputArray[0].length);
    // console.log(inputArray[0].length);
    // console.log(Math.max(inputArray));

Math.max
.length


*/