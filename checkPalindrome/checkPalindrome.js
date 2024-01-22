// checkPalindrome.js

/*

Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.

*/

function solution(inputString) 
{
    i = 0;
    j = inputString.length - 1;

    for (i; i < inputString.length; i++)
    {
        if (inputString [i] != inputString [j])
        {
            return false;
        }

        else
        {
            j--;
        }
    }

    return true;
}

function isOdd(n)
{
    if (n % 2 == 0)
    {
        return false;
    }

    else
    {
        return true;
    }
}

console.log(solution("aabaa"));
console.log(solution("abac"));
console.log(solution("abccba"));
console.log(solution("racecar"));