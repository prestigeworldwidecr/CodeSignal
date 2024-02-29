/*

Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.

*/

function alphabeticShift(inputString)
{
    for (let i = 0; i < inputString.length; i++)
    {
        let tmp = inputString.charCodeAt(i);
        
        if (tmp == 122)   // z
        {
            inputString[i] = "a";
        }

        else if (97 <= tmp && tmp <= 121)   // a - y
        {
            tmp++;
            inputString[i] = String.fromCharCode(tmp);
        }

        else
        {
            //
        }
    }
}

function solution(inputString) 
{

}

let inputString = "crazy"; // output should be solution(inputString) = "dsbaz".



/*

********
BONEYARD
********

let text = String.fromCharCode(72, 69, 76, 76, 79);

*/