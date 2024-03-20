/*

Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
solution(s) = "2a3bc".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string s

String consisting of lowercase English letters.

Guaranteed constraints:
4 ≤ s.length ≤ 15.

[output] string

Encoded version of s.

*/

function lineEnconding(s)
{
    var cur = s.charAt(0);
    var next = s.charAt(1);
    var tmp = new Array();
    var cnt = 0;
    var result = "";

    for(var i = 0; i < s.length; i++)
    {
        // tmp.push(s.charAt(i));
        cur = s.charAt(i);
        next = s.charAt(i + 1);
        cnt++;

        if (next != cur)
        {
            if (cnt == 1)
            {
                //
            }
            
            else
            {
                tmp.push(cnt);
            }

            cnt = 0;
            tmp.push(cur);
        }

        else
        {
            //
        }

    }

    result = tmp.toString().replaceAll(",", "");

    return result;
}

function solution(s) 
{
    return lineEnconding(s);
}

var s = "aabbbc";   // the output should be solution(s) = "2a3bc".

/*

********
BONEYARD
********

lineEnconding(s);

tmp1 = string2DSansDuplicate(s);
    tmp2 = countCharacterInstances(s, tmp1);

    return createSillyString(tmp2);

function lineEnconding(s)
{
    // console.log(s);

    var cur = s.charAt(0);
    var next = s.charAt(1);
    var result = "";
    var cnt = 0;

    for (var i = 0; i < s.length; i++)
    {
        cur = s.charAt(i);
        next = s.charAt(i + 1);

        console.log("cur: ", cur, " next: ", next, " cnt: ", cnt);

        if (cur == next)
        {
            console.log("!");
            cnt++;
        }

        else
        {
            cnt++;
            console.log("@cur: ", cur, " next: ", next, " cnt: ", cnt);
            result = cnt + cur;
            cnt = 0;
        }

        console.log("# cur: ", cur, " next: ", next, " cnt: ", cnt);

    }

    console.log(result);
    return result;
}

tmp1 = string2DSansDuplicate(s);
tmp2 = countCharacterInstances(s, tmp1);

// console.log(tmp2);
createSillyString(tmp2);

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

    "aabcc"
    x   y
    a   0
    b   0
    c   0

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

function createSillyString(s2d)
{
    // console.log("!");

    var result = "";

    for (var i = 0; i < s2d.length; i++)
    {
        if (s2d[i][1] == 1)
        {
            result = result + s2d[i][0];
        }
        
        else
        {
            result = result + s2d[i][1] + s2d[i][0];
        }

    }

    // console.log(result);

    return result;
}


*/