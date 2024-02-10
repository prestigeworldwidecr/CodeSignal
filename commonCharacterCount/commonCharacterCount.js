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

    // s = alphabetizeString(s);
    s = removeDuplicates(s);

    for (i; i < s.length; i++)
    {
        tmp.push(s[i], 0);
    }

    return tmp;

}

function solution(s1, s2) 
{
    var result = 0;
    
    return result;
}

s1 = "aabcc";
s2 = "adcaa";

// console.log(solution(s1, s2));
console.log(string2D(alphabetizeString(s1)));


/*

********
BONEYARD
********

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