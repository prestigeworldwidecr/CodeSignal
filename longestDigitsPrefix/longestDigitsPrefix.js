/*

Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

Guaranteed constraints:
3 ≤ inputString.length ≤ 100.

[output] string

*/

function gotDigits(inputString)
{
    var tmp = inputString.split('');
    // var result = 0;
    var result = "";
    
    // console.log(tmp);

    for (var i = 0; i < tmp.length; i++)
    {
        // console.log(tmp[i]);

        if (Number(tmp[i]) || tmp[i] == "0")
        {
            // result++;
            result = result + tmp[i];
        }

        else
        {
            i = Number.MAX_SAFE_INTEGER;
        }

    }

    // console.log(result);
    return result;

}

function solution(inputString) 
{
    return gotDigits(inputString);
}


var inputString = "123aa1";  // solution(inputString) = "123"
var inputString = "0123456789"; // "0123456789"

// gotDigits(inputString);

/*

********
BONEYARD
********

tmp1 = tmp1.toString();
if (0 <= Number(tmp) && Number(tmp) < 256)
tmp1 = tmp.split('').reverse();

*/