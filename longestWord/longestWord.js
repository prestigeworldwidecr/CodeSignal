/*

Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
solution(text) = "steady".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string text

Guaranteed constraints:
4 ≤ text.length ≤ 50.

[output] string

The longest word from text. It's guaranteed that there is a unique output.

*/

function cleanWord(s)
{
    var result = "";
    
    // console.log("result:", result);
    result = s.replaceAll(",", "");
    result = result.replaceAll("!", "");
    result = result.replaceAll("@", "");
    result = result.replaceAll("#", "");
    result = result.replaceAll("$", "");
    result = result.replaceAll("%", "");
    result = result.replaceAll("^", "");
    result = result.replaceAll("&", "");
    result = result.replaceAll("*", "");
    result = result.replaceAll("(", "");
    result = result.replaceAll(")", "");
    result = result.replaceAll("-", "");
    result = result.replaceAll("+", "");
    result = result.replaceAll("[", "");
    result = result.replaceAll("]", "");
    result = result.replaceAll("{", "");
    result = result.replaceAll("}", "");
    result = result.replaceAll(".", "");
    result = result.replaceAll("<", "");
    result = result.replaceAll(">", "");
    result = result.replaceAll("?", "");
    result = result.replaceAll("`", "");
    result = result.replaceAll("~", "");

    return result;
}

function cleanWordASCII(s)
{
    var result = "";

    for (var i = 0; i < s.length; i++)
    {
        var tmp = s.charCodeAt(i);

                // A-Z 65-90                    a-z 97-122              space
        if ( (65 <= tmp && tmp <= 90) || (97 <= tmp && tmp <= 122) || tmp == 32)
        {
            result = result + s.charAt(i);
        }

        else
        {
            //
        }

    }

    return result;

}

function longestWord(s)
{
    var tmp = cleanWord(s);
    tmp = tmp.split(" ");
    var max = Number.MIN_SAFE_INTEGER;
    var result = "";

    for (var i = 0; i < tmp.length; i++)
    {
        if (max < tmp[i].length)
        {
            max = tmp[i].length;
            result = tmp[i];
        }

        else
        {
            //
        }

    }

    return result;

}

function solution(text) 
{
    return longestWord(text);
}

var text = "Ready, steady, go!";    // the output should be solution(text) = "steady".

// console.log(longestWord(text));
console.log(cleanWordASCII(text));

/*

********
BONEYARD
********

// console.log(s);
// console.log(s.charAt(i));

*/