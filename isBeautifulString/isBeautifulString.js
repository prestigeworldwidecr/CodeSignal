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

function alphabetCount()
{
    var cnt = [ ['a', 0],
                ['b', 0],
                ['c', 0],
                ['d', 0],
                ['e', 0],
                ['f', 0],
                ['g', 0],
                ['h', 0],
                ['i', 0],
                ['j', 0],
                ['k', 0],
                ['l', 0],
                ['m', 0],
                ['n', 0],
                ['o', 0],
                ['p', 0],
                ['q', 0],
                ['r', 0],
                ['s', 0],
                ['t', 0],
                ['u', 0],
                ['v', 0],
                ['w', 0],
                ['x', 0],
                ['y', 0],
                ['z', 0] ];

    return cnt;

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

function isBeautifulString(alpha2D)
{
    var prev = alpha2D[0][1];
    var cur = alpha2D[0][1];
    var result = false;

    // console.log(alpha2D[0][1]);
    
    for (var i = 0; i < alpha2D.length; i++)
    {
        cur = alpha2D[i][1];
        console.log("cur: ", cur, " prev: ", prev);
        
        if (cur > prev)
        {
            return false;
        }

        else
        {
            prev = cur;
            result = true;
        }
        
    }
    
    return result;

}

function solution(inputString) 
{
    return isBeautifulString(countCharacterInstances(alphabetizeString(inputString), alphabetCount()));
}

inputString = "bbbaacdafe"  // the output should be solution(inputString) = true.
// This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.
// inputString = "aabbb"       // the output should be solution(inputString) = false.
// Since there are more bs than as, this string is not beautiful.
// inputString = "bbc"         // the output should be solution(inputString) = false.

// console.log(alphabetCount());
// console.log(isBeautifulString(countCharacterInstances(alphabetizeString(inputString), alphabetCount())));

/*

********
BONEYARD
********

*/