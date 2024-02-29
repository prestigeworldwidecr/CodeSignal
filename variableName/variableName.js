/*

Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;

For name = "qq-q", the output should be
solution(name) = false;

For name = "2w2", the output should be
solution(name) = false.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string name

Guaranteed constraints:
1 ≤ name.length ≤ 10.

[output] boolean

true if name is a correct variable name, false otherwise.

*/

function allValidCharacters(name)
{
    let tmp = -1;
    let result = "";
    
    for (let i = 0; i < name.length; i++)
    {
        tmp = name.charCodeAt(i);

        if (48 <= tmp && tmp <= 57 ||   // 0-9
            65 <= tmp && tmp <= 90 ||   // A-Z
            97 <= tmp && tmp <= 122 ||  // a-z
            tmp == 95)  // _
        {
            result = true;
        }

        else
        {
            return false;
        }
    }

    return result;
}

function solution(name) 
{
    let result = "";
    tmp = name.charCodeAt(0);

    if (65 <= tmp && tmp <= 90 ||   // A-Z
        97 <= tmp && tmp <= 122 ||  // a-z
        tmp == 95)  // _
    {
        result = allValidCharacters(name);
    }

    else
    {
        result = false;
    }

    return result;
}


name1 = "var_1__Int"; // the output should be solution(name) = true;
name2 = "qq-q";   // the output should be solution(name) = false;
name3 = "2w2";    //the output should be solution(name) = false.

// console.log(name1.charCodeAt(1));

console.log(solution(name3));

/*

********
BONEYARD
********

*/