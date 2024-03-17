/*

A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be solution(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be solution(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be solution(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ inputString.length ≤ 50.

[output] boolean

Return true if the string is beautiful, false otherwise.

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

function compare2DStrings(s1, s2)
{
    var i = 0;
    var j = 0;
    var result = 0;

    for (i; i < s1.length; i++)
    {
        j = 0;

        for (j; j < s2.length; j++)
        {
            if (s1[i][0] == s2[j][0])
            {
                result = result + Math.min(s1[i][1], s2[j][1]);
                j = s2.length; // break
            }

            else
            {
                //
            }
        }
    }

    return result;
}

function solution(inputString) 
{

}

/*

********
BONEYARD
********

*/