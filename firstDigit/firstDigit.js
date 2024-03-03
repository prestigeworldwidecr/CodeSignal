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
    let index = inputString.search(/\d/);

    return inputString[index];
}

// let inputString = "var_1__Int"; // the output should be solution(inputString) = '1';
// inputString = "q2q-q";   // the output should be solution(inputString) = '2';
inputString = "0ss";    // the output should be solution(inputString) = '0'.

solution(inputString);

/*

********
BONEYARD
********

// var numberRegex = /^\d+$/;
    
    // Validate numbers
    // result = inputString.indexOf(numberRegex);   // Returns true
    // result = numberRegex.test('Hey12122022x');   // Returns false

var numberRegex = /^\d+$/;
// Validate numbers
numberRegex.test('12122022'); // Returns true
numberRegex.test('Hey12122022x'); // Returns false

// Extract a number from a string
var numberRegexG = /\d$/g;
'Your message was viewed 203 times'.match(numberRegexG); // returns ['203']

let text = "123456789";
let pattern = /[0-9]/g;
text.search(pattern)

let digit = /\d$/g;

    console.log(inputString.match(/\d$/g));

*/