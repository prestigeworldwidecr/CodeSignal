/*

Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";

For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";

For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";

For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".

Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.

Guaranteed constraints:
0 ≤ inputString.length ≤ 50.

[output] string

Return inputString, with all the characters that were in parentheses reversed.

*/

function innerMostSubstring(inputString)
{
    var i = 0;
    var left = -1; // leftParenLocation
    var right = -1; // firstRightParenLocation
    var tmp = "";
    
    while (i < inputString.length)
    {
        if (inputString[i] == '(' && right == -1)
        {
            left = i;
        }

        else if(inputString[i] == ')' && right == -1)
        {
            right = i;
        }
        
        else 
        {

        }
        
        i++;
    }

    if (right == -1)
    {
        return inputString;
    }

    else
    {
        tmp = inputString.substring(0, left) + reverseStringAtom(inputString.substring(left + 1, right)) + inputString.substring(right + 1, inputString.length);

        return innerMostSubstring(tmp);
    }

}

function reverseStringAtom(inputString)
{
    return inputString.split("").reverse().join("");
}

function solution(inputString) 
{
    return innerMostSubstring(inputString);
}

/*

********
BONEYARD
********

// console.log("left: ", left, " right: ", right, " tmp: ", tmp);

// inputString1 = "(bar)" // solution(inputString) = "rab";    ok
// inputString2 = "foo(bar)baz" // solution(inputString) = "foorabbaz";    ok
// inputString3 = "foo(bar)baz(blim)" // solution(inputString) = "foorabbazmilb";  ok
// inputString4 = "foo(bar(baz))blim" // solution(inputString) = "foobazrabblim";

// console.log("final: ", innerMostSubstring(inputString4));
// innerMostSubstring(inputString4);

// console.log(inputString.split("").reverse().join(""));
// reverseStringAtom(inputString1);
// console.log(inputString1.substring(1,3));

// console.log(readReverseString(inputString1, 0));

// tmp = inputString.substring(0, left) + reverseStringAtom(inputString.substring(left + 1, right)) + inputString.substring(right + 1, inputString.length);

    // return (tmp, left);

function readReverseString(inputString, left)
{
    // console.log("inputString: ", inputString, " left: ", left);
    // receiving inputString as empty or '0'
    
    if (left == -1) // || inputString == '0')
    {
        return inputString;
    }

    else
    {
        return readReverseString(innerMostSubstring(inputString), left);
    }
}

// console.log("*: ", tmp, " left: ", left, " right: ", right);

    // console.log(inputString.substring(0,2));     ok
    // console.log(inputString.substring(1, 3));    ok
    // console.log(inputString.substring(0, left)); ok
    // console.log(inputString.substring(left + 1, right));    // ok
    // console.log(reverseStringAtom(inputString.substring(left + 1, right))); // ok
    // console.log(inputString.substring(right + 1, inputString.length));  // ok

// console.log(inputString, " left: ", left, " right: ", right, " i: ", i);

// use split to remove parens

    for (i; i < inputString.length; i++)
    {

    }

// .reverse()
// console.log(inputString.reverse());

*/