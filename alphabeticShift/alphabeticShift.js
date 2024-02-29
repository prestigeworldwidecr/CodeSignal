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
    let cur = -1;
    let result = [];
    result.length = inputString.length;

    for (let i = 0; i < inputString.length; i++)
    {
        let cur = inputString.charCodeAt(i);
        console.log("cur: ", cur, " String.fromCharCode(cur): ", String.fromCharCode(cur));
        
        if (cur == 122)   // z
        {
            result.push("a");
        }

        else if (97 <= cur && cur <= 121)   // a - y
        {
            cur++;
            result.push(String.fromCharCode(cur));
        }

        else
        {
            //
        }
    }

    return result;

}

function solution(inputString) 
{

}

let inputString = "crazy"; // output should be solution(inputString) = "dsbaz".

console.log(alphabeticShift(inputString));

/*

********
BONEYARD
********

// inputString = inputString.split("");
        // let tmp = inputString.split("");
        // console.log("tmp[", i, "]: ", tmp[i], " cur: ", cur, " String.fromCharCode(cur): ", String.fromCharCode(cur));
            // tmp[i] = "a";
            // tmp[i] = String.fromCharCode(cur);

let text = String.fromCharCode(72, 69, 76, 76, 79);

*/