/*

Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.

*/

function alphabetizeString(s)
{
    var i = 0;
    var tmp = "";

    tmp = s.split("");
    tmp = tmp.sort();
    tmp = tmp.join("");

    return tmp;
}

function removeDuplicates(s)
{
    var tmp = [...new Set(s)].join("");

    return tmp;
}

/*

    "aabcc"
    x   y
    a   0
    b   0
    c   0

*/
function string2DSansDuplicate(s)
{
    var i = 0;
    var tmp = [];

    s = removeDuplicates(s);

    for (i; i < s.length; i++)
    {
        tmp.push([s[i], 0]);
    }

    return tmp;

}

// input: alphabetized string, 2D array containing corresponding characters non-dup
// output: same 2D array w/character counts in column 2
function countCharacterInstances(s, s2d)
{
    var i = 0;
    var j = 0;
    var tmp = 0;

    for (i; i < s2d.length; i++)
    {
        tmp = 0;
        j = 0;
        
        for (j; j < s.length; j++)
        {
            if (s[j] == s2d[i][0])
            {
                tmp++;
                s2d[i][1] = tmp;
            }

            else
            {
                //
            }

        }
    }

    return s2d;
}

function eligibleRearrange(inputString)
{
    let i = 0;
    let cnt = 0;    // count of characters w/odd count
    
    for (i; i < inputString.length; i++)
    {
        if (cnt > 1)
        {
            return false;
        }
        
        else if (inputString[i][1] % 2 == 0)
        {
            // 
        }

        else
        {
            cnt++;
        }
    }

    return true;
}

function solution(inputString) 
{

}

inputString = "aabb"; // solution(inputString) = true
inputString = alphabetizeString(inputString);
inputString = countCharacterInstances(inputString, string2DSansDuplicate(inputString));

console.log(eligibleRearrange(inputString));
// console.log(inputString);
// console.log(4 % 2);

/*

********
BONEYARD
********

*/