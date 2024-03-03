/*

Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
solution(inputString) = '1';
For inputString = "q2q-q", the output should be
solution(inputString) = '2';
For inputString = "0ss", the output should be
solution(inputString) = '0'.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A string containing at least one digit.

Guaranteed constraints:
3 ≤ inputString.length ≤ 10.

[output] char

*/

function solution(inputString) 
{
    let text = "123456789";
    let pattern = /[0-9]/g;
    console.log(text.search(pattern));
}

let inputString = "var_1__Int"; // the output should be solution(inputString) = '1';
let inputString = "q2q-q";   // the output should be solution(inputString) = '2';
let inputString = "0ss";    // the output should be solution(inputString) = '0'.

/*

********
BONEYARD
********

let text = "123456789";
let pattern = /[0-9]/g;
text.search(pattern)

*/