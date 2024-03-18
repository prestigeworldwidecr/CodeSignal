/*

Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string st

A string consisting of lowercase English letters.

Guaranteed constraints:
3 ≤ st.length ≤ 10.

[output] string

*/

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

function removeDuplicates(s)
{
    var tmp = [...new Set(s)].join("");

    return tmp;
}

function alphabetizeString(s)
{
    var i = 0;
    var tmp = "";

    tmp = s.split("");
    tmp = tmp.sort();
    tmp = tmp.join("");

    return tmp;
}

function indexMaxS2D(s2d)
{
    var indexMax = Number.MIN_SAFE_INTEGER;
    var max = Number.MIN_SAFE_INTEGER;

    for (var i = 0; i < s2d.length; i++)
    {
        var cur = i;
        
        if (max <= s2d[i][1])
        {
            max = s2d[i][1];
            indexMax = cur;
        }

        else
        {
            //
        }

    }

    return indexMax;

}

// function equalize s2d

function buildPalindrome(s, s2d)
{
    var result = "";

    if (s.length % 2 == 0)
    {
        // console.log(indexMaxS2D(s2d));
    }

    else
    {
        // console.log(indexMaxS2D(s2d));
    }

    return result;

}

function solution(st) 
{

}

var st = "abcdc"    // the output should be solution(st) = "abcdcba"
var tmp1 = alphabetizeString(st);
var tmp2 = string2DSansDuplicate(st);
var tmp3 = countCharacterInstances(tmp1, tmp2);

buildPalindrome(st, tmp3);

/*

********
BONEYARD
********

// console.log("odd");
 // console.log(s.length, s2d);
        // console.log("even");
        // console.log(s2d);
        // max of letters


// console.log(countCharacterInstances(st), string2DSansDuplicate(st));

*/