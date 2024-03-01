/*

Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
solution(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
solution(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.string inputArray

A non-empty array of strings of lowercase letters.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 15.

[output] boolean

Return true if the strings can be reordered in such a way that each neighbouring pair of strings differ by exactly one character (false otherwise).

*/

function asciiStringSum(str)
{
    let sum = 0;

    for (let i = 0; i < str.length; i++)
    {
        sum = sum + str.charCodeAt(i);
    }

    return sum;
}


// 1, 2...n
// tmp1 shall represent 1, tmp2 then tmp1 will be 2 and so on...
function isAsciiConsecutive(inputArray)
{
    let tmp1 = -1;
    let tmp2 = -1;
    let result = false;

    for (let i = 0; i < inputArray.length - 1; i++)
    {
        tmp1 = asciiStringSum(inputArray[i]);
        tmp2 = asciiStringSum(inputArray[i + 1]);

        if (tmp1 + 1 != tmp2)
        {
            return false;
        }

        else
        {
            result = true;
        }
    }

    return result;

}

function stringRearrange(inputArray)
{
    let cnt = 0;    // each neighbouring pair of strings differ by exactly one character
    let tmp1 = "";
    let tmp2 = "";
    let result = false;

    for (let i = 0; i < inputArray.length - 1; i++)
    {
        cnt = 0;
        tmp1 = inputArray[i].split("");
        tmp2 = inputArray[i + 1].split("");

        for (let j = 0; j < tmp1.length; j++)
        {
            // console.log("tmp1: ", tmp1, " tmp2: ", tmp2, " i: ", i, " j: ", j, " tmp1[j]: ", tmp1[j], " tmp2[j]: ", tmp2[j], " cnt: ", cnt);
            
            if (cnt > 1)
            {
                return false;
            }
            
            else if (tmp1 [j] == tmp2 [j])
            {
                result = true;
            }

            else
            {
                cnt++;
            }
        }
    }

    return result;
}

function solution(inputArray) 
{
    stringRearrange(inputArray.sort());
}

// let inputArray = ["aba", "bbb", "bab"]  // the output should be solution(inputArray) = false
let inputArray = ["ab", "bb", "aa"];    // the output should be solution(inputArray) = true

// console.log(asciiStringSum(inputArray[0]));
// console.log(asciiStringSum(inputArray[1]));
// console.log(asciiStringSum(inputArray[2]));

// console.log(inputArray.sort());

// console.log(isAsciiConsecutive(inputArray.sort()));
console.log(stringRearrange(inputArray.sort()));

/*

********
BONEYARD
********

can i use ASCII values?
1 sort -> send along
2 consecutive ascii sum ^ same?
3 sort substring
4 letter by letter check

*/