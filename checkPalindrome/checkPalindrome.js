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
    return isOdd(inputString);
}

function isOdd(n)
{
    if (n % 2 == 0)
    {
        return true;
    }

    else
    {
        return false;
    }
}

solution("aabaa");
solution("abac");
solution("a");