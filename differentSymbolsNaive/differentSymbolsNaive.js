/*

Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
solution(s) = 3.

There are 3 different characters a, b and c.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string s

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ s.length ≤ 1000.

[output] integer

*/

function solution(s) 
{
    
    var tmp = [...new Set(s)].join("");

    console.log(tmp.length);

    // return tmp;
}

var s = "cabca";    // the output should be solution(s) = 3.
solution(s);

/*

********
BONEYARD
********



*/