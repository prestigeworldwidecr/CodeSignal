// snake.js

/*

One of your new coworkers has submitted code with variable names in snake case, where multiword names are separated by underscores (such as my_counter). Your company's convention is to use only lower camel case, where multiword variable names are concatenated, capitalizing the first letter of every word except the first (e.g. myCounter).

Your team is tasked with taking the source code src from your coworker, and returning code with the all the names in snake case converted into lower camel case. More specifically:

Variable names may start with one or more underscores, and these should be preserved. For example _the_variable should become _theVariable
Variable names may end with trailing underscores, and these should be preserved. For example, the_variable__ should become theVariable__.
To keep the problem simple, you are not restricted to variable names, but instead should replace all instances of snake case.
Example

For src = "This is the doc_string for __secret_fun", the output should be
solution(src) = "This is the docString for __secretFun".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string src

All variables in src are in lowercase English letters. It's guaranteed that in the variable names there can be only one _ between words.

Guaranteed constraints:
0 ≤ src.length ≤ 105.

[output] string

Return the source code src with all instances of snake case converted to lower camel case, preserving any leading or trailing underscores.

[JavaScript] Syntax Tips

// Prints help message to the console
// Returns a string
function helloWorld(name) {
    console.log("This prints to the console when you Run Tests");
    return "Hello, " + name;
}

snake_case to camelCase

if starts w/underscore, preserve
if ends w/underscore, preserve

example:

input
-----
"This is the doc_string for __secret_fun"

output
------
"This is the docString for __secretFun"

*/

function solution(src) 
{
    tmp = "";
    prev = '';  // previous character

    for (i = 0; i < src.length; i++)
    {
        tmp = tmp + src [i];

        // if starts w/underscore, preserve
        if (i == 0)
        {
            
        }

        // if ends w/underscore, preserve
        else if (i = src.length)
        {

        }

        else
        {

        }
    }

    console.log(tmp);
}

function printSource(src)
{
    underscoreCnt = 0;
    
    for (i = 0; i < src.length; i++)
    {
        if (src.charCodeAt(i) == 95)
        {
            underscoreCnt++;
        }

        else
        {
            0;
        }
    }

    // console.log(underscoreCnt);
}

src = "This is the doc_string for __secret_fun";
solution(src);

/*

BONEYARD
--------

// tmp = tmp + src.charCodeAt(i);
// console.log(src[i]);

// console.log(src);
    // printSource(src);
    // let char = String.fromCharCode(65);
    // alert(str[i]);

    

// console.log(src.charCodeAt(0)); ** output is ascii
// 

// console.log(i);
// string1.localeCompare(string2)
// return str.length === 1 && str.match(/[a-z]/i);
// let n = str.charCodeAt(0);

// console.log(src.charCodeAt(15));

*/