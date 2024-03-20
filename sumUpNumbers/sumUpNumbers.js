/*

CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
solution(inputString) = 14.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

Guaranteed constraints:
0 ≤ inputString.length ≤ 105.

[output] integer

*/

function cleanNumberASCII(s)
{
    var result = "";

    for (var i = 0; i < s.length; i++)
    {
        var tmp = s.charCodeAt(i);

                // 0-9                      space
        if ( (48 <= tmp && tmp <= 57) || tmp == 32)
        {
            result = result + s.charAt(i);
        }

        else
        {
            //
        }

    }

    return result;

}

function sumUpNumbers(s)
{
    var tmp = cleanNumberASCII(s);
    var tmp = tmp.split(" ");
    var result = 0;

    for (var i = 0; i < tmp.length; i++)
    {
        if (tmp[i] == '')
        {
            //
        }

        else
        {
            result = result + Number(tmp[i]);
        }
    }

    return result;
}

function solution(inputString) 
{
    sumUpNumbers(inputString);
}

var inputString = "2 apples, 12 oranges";   // the output should be solution(inputString) = 14.
inputString = "42+781"; // 823
/*

********
BONEYARD
********

// console.log(Number(tmp[i]));
// console.log("Number.isInteger(result[i]): ", Number.isInteger(result[i]), Number(result[i]));
        // console.log(Number(result[i]));
        // console.log(tmp[i] == " ");
        

*/