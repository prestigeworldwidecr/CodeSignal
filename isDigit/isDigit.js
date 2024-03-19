/*

Determine if the given character is a digit or not.

Example

For symbol = '0', the output should be
solution(symbol) = true;
For symbol = '-', the output should be
solution(symbol) = false.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] char symbol

A character which is either a digit or not.

Guaranteed constraints:
Given symbol is from ASCII table.

[output] boolean

true if symbol is a digit, false otherwise.

*/

function solution(symbol) 
{
    // console.log(symbol);
    var s = "";
    var tmp = 0;
    
    s = symbol;
    s = symbol.toString();
    tmp = s.charCodeAt(0);
    
    console.log(tmp);

    return 48 <= tmp && tmp <= 57;
}

solution(0);

/*

********
BONEYARD
********



*/