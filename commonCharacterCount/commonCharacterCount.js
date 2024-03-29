/*

Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer

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

function solution(s1, s2) 
{
    s1 = alphabetizeString(s1);
    s1 = countCharacterInstances(s1, string2DSansDuplicate(s1));
    s2 = alphabetizeString(s2);
    s2 = countCharacterInstances(s2, string2DSansDuplicate(s2));
    
    return compare2DStrings(s1, s2);
}

s1 = "aabcc";
s2 = "adcaa";

console.log(solution(s1, s2));

/*

********
BONEYARD
********


    // console.log(s1);
    // console.log(s2);

// console.log("s1[i][0]: ", s1[i][0], " s2[j][0]: ", s2[j][0]);

// s3 = alphabetizeString(s2);

// console.log(solution(s1, s2));
// console.log(countCharacterInstances(s3, string2DSansDuplicate(s3)));

// console.log(tmp [1][0]);
// console.log(s, " ", s2d);

            else if (j == s.length - 1)
            {
                // tmp++;
                // console.log("*");
                // s2d[i][1] = tmp;
                // console.log("tmp: ", tmp, "s[j]: ", s[j], " s2d[i][0]: ", s2d[i][0]);
            }

// console.log(s);

    // tmp.push(s[0], 0);

    
        // console.log("tmp [i][1]: ", tmp [i][1], " s[i]: ", s[i]);
        // console.log("s[i]: ", s[i]);

if (s2.length > s1.length)
    {
        result = ccc(s1, s2);
    }

    else
    {
        result = ccc(s2, s1);
    }

function removeDuplicates(s)
{
    tmp = [...new Set(s)].join("");

    return tmp;
}

// s1 = "taaaco";
// s2 = "abc";

/// ccc: common character count
function ccc1(s1, s2)
{
    var i = 0;
    var j = 0;
    var cnt = 0;

    for (i; i < s1.length; i++)
    {
        

        j = 0;
        
        for (j; j < s2.length; j++)
        {            
            console.log("i: ", i, " j: ", j, "s1[i]: ", s1[i], " s2[j]: ", s2[j]);
            
            if (s1[i] == s2[j])
            {
                cnt++;
            }

            else
            {
                // 
            }
        }
    }

    return cnt;

}

console.log(s1.length, " ", s2.length);

// printCharofString(s1);
// removeDuplicates(s1);

console.log("i: ", i, " j: ", j, "s1[i]: ", s1[i], " s2[j]: ", s2[j]);

*/