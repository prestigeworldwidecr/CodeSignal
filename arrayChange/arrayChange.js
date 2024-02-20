/*

You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-105 ≤ inputArray[i] ≤ 105.

[output] integer

The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.

*/

/*
    a "move" is an increment of one on any given number
    in the example, 3rd element '3' needs an increase of 2
*/

function makeStrictlyIncreasing(inputArray)
{
    var i = 0;
    var inc = 0;    // necessary increment ("move")
    var max = inputArray[i];
    var result = 0;

    for (i; i < inputArray.length - 1; i++)
    {
        max = inputArray[i] > max ? inputArray[i] : max;
         
        if (inputArray[i] < inputArray[i + 1])
        {
            //
        }

        else
        {
            inc = max - inputArray[i + 1] + 1;
            inputArray[i + 1] = max + 1;            
            result = result + inc;
        }
    }

    return result;
}

function solution(inputArray) 
{
    return makeStrictlyIncreasing(inputArray);
}

/*

********
BONEYARD
********

// inputArray = [1, 1, 1];  // solution(inputArray) = 3
// console.log(makeStrictlyIncreasing(inputArray));

// var a = 0;
            // var tmp = [];   // array from inputArray(0, i + 1)
            // a = 0;
            // tmp = inputArray.slice(0, i + 2); // slice omits end value. need end and the one after
            // max = Math.max(...tmp);
            // a = max + 1;    // temporary variable to hold the new value of inputArray[i + 1]
            // inputArray[i + 1] = a;    // update the inputArray
            // console.log("max: ", max, " inputArray[i]: ", inputArray[i], "inputArray[i + 1]: ", inputArray[i + 1]);

inputArray = [1, 1, 1];  // solution(inputArray) = 3
makeStrictlyIncreasing(inputArray);

// start is kind of bogus here since it will always be zero coming from makeStrictlyIncreasing
function IntSubArray (inputArray, start, end)
{
    var length = end - start + 1;
    var tmp  = new Int32Array(length);
    tmp = [...inputArray];
    tmp.length = length;

    return tmp;
}


// tmp = IntSubArray(inputArray, 0, i + 1);
            // console.log("*1: ", tmp, " *2: ", inputArray.slice(0, i + 2));
            // console.log("*1: ", tmp, " *2: ", inputArray.slice(0, i + 1));

// inputArray = [1, 2, 3, 4, 5];
// IntSubArray(inputArray, 1, 3);
// console.log(inputArray.slice(0, 3));

function subArray(inputArray, start, end)
{
    var i = start;
    var tmp = new Int32Array(end - start + 1);

    for (i; i <= end; i++)
    {        
        tmp[i] = parseInt(inputArray[i]);
    }
    
    return tmp;

}



// 19-feb-2024 12.39
// speed up the subArray
// substring back to int

inputArray = [1, 1, 1];  // solution(inputArray) = 3
makeStrictlyIncreasing(inputArray);

console.log("inc: ", inc, " result: ", result);

    // var a = 0;  // inputArray[i]
    // var b = 0;  // inputArray[i + 1]

        // a = inputArray[i];
        // b = inputArray[i + 1];

console.log("$tmp: ", tmp);

// console.log("i: ", i, " elem: ", parseInt(inputArray[i]), " start: ", start, " end: ", end);

console.log("inputArray: ", inputArray, " start: ", start, " end: ", end, " tmp.length: ", tmp.length);

// console.log("inputArray: ", inputArray, " start: ", start, " end: ", end, " inputArray.length: ", inputArray.length);

    for (i; i < end; i++)
    {
        console.log("inputArray[i]: ", inputArray[i]);
    }

 // console.log("inputArray: ", inputArray, " inputArray.toString(): ", inputArray.toString());
            // tmp = inputArray.toString().substr(0, b);
            // for (j = i + 1; j > 0; j--)
            // {

            // }
                // inc = j - k + 1;
                // result = result + inc;
    // var j = 0;
    // var strictlyIncreasing = true;
    
****WORKING****
function makeStrictlyIncreasing(inputArray)
{
    var i = 0;
    var a = 0;
    var inc = 0;    // necessary increment ("move")
    var max = -999999;  // Math.max(inputArray);
    var result = 0;
    var tmp = [];   // array from inputArray(0, i + 1)

    for (i; i < inputArray.length - 1; i++)
    {
        a = 0;
         
        if (inputArray[i] < inputArray[i + 1])
        {
            //
        }

        else
        {
            // tmp = inputArray.slice(0, i + 2); // slice omits end value. need end and the one after
            max = Math.max(...tmp);
            a = max + 1;    // temporary variable to hold the new value of inputArray[i + 1]
            inc = max - inputArray[i + 1] + 1;
            inputArray[i + 1] = a;    // update the inputArray
            result = result + inc;
        }
    }

    return result;
}


*/