/*

Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 10,
-15 ≤ inputArray[i] ≤ 15.

[output] integer

The maximal absolute difference.

*/

function solution(inputArray) 
{
    var i = 0;
    var pair = [inputArray[0], inputArray[1]];
    var min = Math.min(...pair);
    var max = Math.max(...pair);
    var tmp = -999999;
    var mad = -999999;   // Maximal Adjacent Difference
    
    for (i; i < inputArray.length - 1; i++)
    {
        pair = [inputArray[i], inputArray[i + 1]];
        min = Math.min(...pair);
        max = Math.max(...pair);
        tmp = max - min;

        if (tmp > mad)
        {
            mad = tmp;
        }

        else
        {
            // 
        }

    }

    return mad;

}

/*

********
BONEYARD
********

// console.log("pair: ", pair, " min: ", min, " max: ", max);
    // console.log("pair: ", pair, " min: ", min, " max: ", max, " tmp: ", tmp);
    // console.log(mad);

inputArray = [2, 4, 1, 0];  // 
solution(inputArray);

*/